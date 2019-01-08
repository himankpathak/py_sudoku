from random import *

def swaprow(a1,a2):
	for b in range(9):
		temp=L[a1][b]
		L[a1][b]=L[a2][b]
		L[a2][b]=temp

def swapcol(b1,b2):
	for a in range(9):
		temp=L[a][b1]
		L[a][b1]=L[a][b2]
		L[a][b2]=temp

def baseshuffle(b):
	for a in range(3):
		l=L[a][b+2]
		L[a][b+2]=L[a][b+1]
		L[a][b+1]=L[a][b]
		L[a][b]=l
	for a in range(6,9):
		l=L[a][b]
		L[a][b]=L[a][b+1]
		L[a][b+1]=L[a][b+2]
		L[a][b+2]=l

def shufflefunc(b):
	acon=randint(0,8)
	adder=1
	for a in range(9):
		if(L[acon][b]==L[a][b+adder]):
			L[a][b+adder]=L[a][b]
			L[a][b]=L[acon][b]
		elif(L[acon][b+adder]==L[a][b]):
			L[a][b]=L[a][b+adder]
			L[a][b+adder]=L[acon][b+adder]
	temp=L[acon][b]
	L[acon][b]=L[acon][b+adder]
	L[acon][b+adder]=temp

def mixshuffle():
	for count in range(999):
		swaprow(randint(0,2),randint(0,2))
		swaprow(randint(3,5),randint(3,5))
		swaprow(randint(6,8),randint(6,8))
		swapcol(randint(0,2),randint(0,2))
		swapcol(randint(3,5),randint(3,5))
		swapcol(randint(6,8),randint(6,8))
		no1=randint(1,9)
		no2=randint(1,9)
		for a in range(9):
			for b in range(9):
				if(L[a][b]==no1):
					L[a][b]=no2
				elif(L[a][b]==no2):
					L[a][b]=no1

def initialize():
	global L
	for a in range(9):
		l=[]
		for b in range(9):
			temp=a+b+1
			if(temp>9):
				temp-=9
			l.append(temp)
		L.append(l)

	swaprow(1,3)
	swaprow(2,6)
	swaprow(5,7)
	# sudoku is created

	baseshuffle(0)
	baseshuffle(3)
	baseshuffle(6)
	# shuffling to create a sudoku with interchangable element in nonets

	for shuffle in range(999):
		shufflefunc(0)
		shufflefunc(3)
		shufflefunc(6)
	# shuffling individual elements in nonets

	mixshuffle()
	# final shuffling to randomize sudoku

def printb(L):
	line=chr(95)
	print("Column =>","1.   2.   3.   4.   5.   6.   7.   8.   9.")
	print("Row")
	for a in range(9):
		print(" ",a+1,".  |",end="")
		for b in range(9):
			print(" ",L[a][b],"",end="")
			print("|",end="")
		print("")
		print(" "*6,"-"*46)


if __name__ == "__main__":

	print("""
	Welcome to SUD0KU v0.1

    Objective: Enter integer number in empty spaces such that each row, column, and
		nonet can contain each number (typically 1 to 9) exactly once.
    	Every sudoku puzzle has only one possible solution. There can be no ambiguity in Sudoku.

    """)

	L=Lnew=[]
	n=0
	always=True
	win=False

	cplayer=input("Enter your name: ")
	cplayer=cplayer.capitalize()
	modeselect=input("If you want infinte try mode then enter \"Yes\" else enter \"No\" : ")
	if(modeselect.upper()=="YES"):
		infinite=True
		print("Infinite try mode selected")
	else:
		infinite=False
		print("Normal mode selected")

	while(always==True):
		difficulty=input("Enter difficulty between 1 to 5 where, 1 is too easy and 5 is too difficult -> ")
		if(difficulty=="1"):
			print("Welcome "+cplayer+", Novice difficulty selected")
			tryno=5
			break
		elif(difficulty=="2"):
			print("Welcome "+cplayer+", Beginner difficulty selected")
			tryno=10
			break
		elif(difficulty=="3"):
			print("Welcome "+cplayer+", Intermediate difficulty selected")
			tryno=15
			break
		elif(difficulty=="4"):
			print("Welcome "+cplayer+", Seasoned difficulty selected")
			tryno=20
			break
		elif(difficulty=="5"):
			print("Welcome "+cplayer+", Expert difficulty selected")
			tryno=25
			break
		else:
			print("Please enter a valid integer")

	initialize()
	printb(L)
