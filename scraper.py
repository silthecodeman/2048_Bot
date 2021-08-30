from bs4 import BeautifulSoup

def getPositions(html):
    rw1 = ["", "", "", ""]
    rw2 = ["", "", "", ""]
    rw3 = ["", "", "", ""]
    rw4 = ["", "", "", ""]

    soup = BeautifulSoup(html, 'html.parser')
    tiles = soup.find_all("div", class_="tile-container")[0].find_all('div')
    classes = [j.split(" ")[1:3] for j in [str(i).split("\"")[1] for i in tiles] if j != 'tile-inner']
    for i in classes:
        number = int(i[0].split('-')[1])
        posRight = int(i[1].split('-')[2])
        posDown = int(i[1].split('-')[3])

        if posDown == 1:
            rw1[posRight - 1] = str(number)
        if posDown == 2:
            rw2[posRight - 1] = str(number)
        if posDown == 3:
            rw3[posRight - 1] = str(number)
        if posDown == 4:
            rw4[posRight - 1] = str(number)
            
    if soup.find_all('div', class_='game-message')[0].find_all('p')[0].text == 'Game over!':
        return 'exit', 'exit', 'exit', 'exit'
    return rw1, rw2, rw3, rw4
