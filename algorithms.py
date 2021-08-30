def decisionAlgorithm(rw1, rw2, rw3, rw4):
	points = 0
	if len(rw1) > 1:
		if len(rw1) == 2:
			if rw1[0] == rw1[1]:
				points += 1
		elif len(rw1) == 3:
			if rw1[0] == rw1[1]:
				points += 1
			elif rw1[1] == rw1[2]:
				points += 1
		elif len(rw1) == 4:
			if rw1[0] == rw1[1]:
				points += 1
				if rw1[2] == rw1[3]:
					points += 1
			elif rw1[1] == rw1[2]:
				points += 1
			elif rw1[2] == rw1[3]:
				points +=1
	if len(rw2) > 1:
		if len(rw2) == 2:
			if rw2[0] == rw2[1]:
				points += 1
		elif len(rw2) == 3:
			if rw2[0] == rw2[1]:
				points += 1
			elif rw2[1] == rw2[2]:
				points += 1
		elif len(rw2) == 4:
			if rw2[0] == rw2[1]:
				points += 1
				if rw2[2] == rw2[3]:
					points += 1
			elif rw2[1] == rw2[2]:
				points += 1
			elif rw2[2] == rw2[3]:
				points +=1
	if len(rw3) > 1:
		if len(rw3) == 2:
			if rw3[0] == rw3[1]:
				points += 1
		elif len(rw3) == 3:
			if rw3[0] == rw3[1]:
				points += 1
			elif rw3[1] == rw3[2]:
				points += 1
		elif len(rw3) == 4:
			if rw3[0] == rw3[1]:
				points += 1
				if rw3[2] == rw3[3]:
					points += 1
			elif rw3[1] == rw3[2]:
				points += 1
			elif rw3[2] == rw3[3]:
				points +=1
	if len(rw4) > 1:
		if len(rw4) == 2:
			if rw4[0] == rw4[1]:
				points += 1
		elif len(rw4) == 3:
			if rw4[0] == rw4[1]:
				points += 1
			elif rw4[1] == rw4[2]:
				points += 1
		elif len(rw4) == 4:
			if rw4[0] == rw4[1]:
				points += 1
				if rw4[2] == rw4[3]:
					points += 1
			elif rw4[1] == rw4[2]:
				points += 1
			elif rw4[2] == rw4[3]:
				points +=1
	return points