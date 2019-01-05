from random import *
from string import *

def initialize():
	L=[]
	for a in range(9):
		l=[]
		for b in range(9):
			l.append(a+b+1)
		L.append(l)
	for a in range(9):
		for b in range(9):
			if(L[a][b]>9):
				L[a][b]-=9

	print (L)


if __name__ == "__main__":

	print("""
	Welcome to SUD0KU v0.1

    Objective: Enter integer number in empty spaces such that each row, column, and nonet can contain each number (typically 1 to 9) exactly once.
              Every sudoku puzzle has only one possible solution. There can be no ambiguity in Sudoku.

    """)
