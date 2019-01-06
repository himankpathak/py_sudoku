from random import *
from string import *

L=[]

def swaprow(a1,a2):
	for b in range(9):
		temp=L[a1][b]
		L[a1][b]=L[a2][b]
		L[a2][b]=temp

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
	adder=randint(1,2)
	for a in range(9):
		if(L[acon][b]==L[a][b+adder]):
			L[a][b+adder]=L[a][b]
			L[a][b]=L[acon][b]
		elif(L[acon][b+adder]==L[a][b]):
			L[a][b]=L[a][b+adder]
			L[a][b+adder]=L[acon][b+adder]
	l=L[acon][b]
	L[acon][b]=L[acon][b+adder]
	L[acon][b+adder]=l

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
	# shuffling to create a sudoku with interchangable element

	for shuffle in range(99):
		shufflefunc(0)
		shufflefunc(3)
		shufflefunc(6)


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

	initialize()
	printb(L)
