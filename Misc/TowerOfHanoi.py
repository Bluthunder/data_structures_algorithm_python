def  towerOfHanoi(numberOfDisks, startPeg=1, endPeg=3):
	if numberOfDisks:
		towerOfHanoi(numberOfDisks-1, startPeg, 6-startPeg-endPeg)
		print(f"Move disk {numberOfDisks} from peg {startPeg} to {endPeg}")
		towerOfHanoi(numberOfDisks-1,6-startPeg-endPeg, endPeg)


if  "__name__==__main__":
	towerOfHanoi(numberOfDisks=4)
	
	
	
	