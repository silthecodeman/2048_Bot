from algorithms import decisionAlgorithm

def testUp(roow1, roow2, roow3, roow4):
	column1 = [roow1[0],roow2[0],roow3[0],roow4[0]]
	column2 = [roow1[1],roow2[1],roow3[1],roow4[1]]
	column3 = [roow1[2],roow2[2],roow3[2],roow4[2]]
	column4 = [roow1[3],roow2[3],roow3[3],roow4[3]]
	rw1 = [i for i in column1 if i != ""]
	rw2 = [i for i in column2 if i != ""]
	rw3 = [i for i in column3 if i != ""]
	rw4 = [i for i in column4 if i != ""]
	return decisionAlgorithm(rw1, rw2, rw3, rw4)

def testDown(roow1, roow2, roow3, roow4):
	column1 = [roow1[0],roow2[0],roow3[0],roow4[0]]
	column2 = [roow1[1],roow2[1],roow3[1],roow4[1]]
	column3 = [roow1[2],roow2[2],roow3[2],roow4[2]]
	column4 = [roow1[3],roow2[3],roow3[3],roow4[3]]
	rw1 = [i for i in column1 if i != ""][::-1]
	rw2 = [i for i in column2 if i != ""][::-1]
	rw3 = [i for i in column3 if i != ""][::-1]
	rw4 = [i for i in column4 if i != ""][::-1]
	return decisionAlgorithm(rw1, rw2, rw3, rw4)

def testLeft(roow1, roow2, roow3, roow4):
	rw1 = [i for i in roow1 if i != ""]
	rw2 = [i for i in roow2 if i != ""]
	rw3 = [i for i in roow3 if i != ""]
	rw4 = [i for i in roow4 if i != ""]
	return decisionAlgorithm(rw1, rw2, rw3, rw4)

def testRight(roow1, roow2, roow3, roow4):
	rw1 = [i for i in roow1 if i != ""][::-1]
	rw2 = [i for i in roow2 if i != ""][::-1]
	rw3 = [i for i in roow3 if i != ""][::-1]
	rw4 = [i for i in roow4 if i != ""][::-1]
	return decisionAlgorithm(rw1, rw2, rw3, rw4)

def testUDLR(row1, row2, row3, row4):
    up_test = testUp(row1, row2, row3, row4)
    down_test = testDown(row1, row2, row3, row4)
    left_test = testLeft(row1, row2, row3, row4)
    right_test = testRight(row1, row2, row3, row4)

    return [up_test, down_test, left_test, right_test]