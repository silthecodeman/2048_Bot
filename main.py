from selenium.webdriver.common.keys import Keys
from scraper import getPositions
from startSequence import initiate, complete
from scraper import getPositions
from testing import testUDLR
from backups import findBackupDecision
import random
import time

# pretty streight forward, moving the game board based on BestPossibility
def gameMove(driver, BestPossibility):
    game = driver.find_element_by_tag_name('body')

    if BestPossibility == 'Up':
        game.send_keys(Keys.ARROW_UP)
    if BestPossibility == 'Down':
        game.send_keys(Keys.ARROW_DOWN)
    if BestPossibility == 'Left':
        game.send_keys(Keys.ARROW_LEFT)
    if BestPossibility == 'Right':
        game.send_keys(Keys.ARROW_RIGHT)


if __name__ == '__main__':
    while True:
        #start the webpage up 
        driver = initiate()
        in_session = True

        while in_session:
            #get the positions of the rows
            row1, row2, row3, row4 = getPositions(driver.page_source)

            if row1 == 'exit':
                in_session = False

            #test the possible points gained by moving up, down, left or right
            movements = ('Up', 'Down', 'Left', 'Right')
            possibilities = testUDLR(row1, row2, row3, row4)

            #if no possible points are gained, try testing for possible points after randomly moving board positions
            if possibilities == [0,0,0,0]:
                BestPossibility = findBackupDecision()

                #if the findBackupDecision function turns up nothing, randomly pick a direction
                if BestPossibility == 0:
                    BestPossibility = movements[random.randint(0,3)]

            #if there was a route(s) that was found pick the highest and move based on that
            else:
                BestPossibility = movements[possibilities.index(max(possibilities))]

            #move the board based on best decision
            gameMove(driver, BestPossibility)

        complete(driver)
