from arithmetic import add, subtract, multiply, divide
import sys

calcArray = []

def calculateResult():

	def reInsert():
		inputList.insert(currIdx - 2, str(value))

	inputList = calcArray[0].split(' ')
	while len(inputList) >= 3:

		currIdx = 0
		for elems in inputList:
			if elems in '+-/*':
				firstOperand = inputList.pop(currIdx - 2)
				secondOperand = inputList.pop(currIdx - 2)
				currOperator = inputList.pop(currIdx - 2)
				if currOperator == '+':
					value = add(firstOperand, secondOperand)
					reInsert()
				elif currOperator == '*':
					value = multiply(firstOperand, secondOperand)
					reInsert()
				elif currOperator == '-':
					value = subtract(firstOperand, secondOperand)
					reInsert()
				else:
					value = divide(firstOperand, secondOperand)
					reInsert()

			currIdx += 1

	print('\nsolution', float(inputList[0]), '\n' )
	
def getInput():
	while True:
		try:
			if len(calcArray) != 0:
				clearSolution = input('would you like to clear previous solution? "y" or "n": ')
				if clearSolution == 'y':
					calcArray.clear()
				else:
					newInput = input('\nPlease enter the rest of your expression: ')
					newCalcArray = calcArray[0] + " " + newInput
					calcArray.clear()
					calcArray.append(newCalcArray)
					checkInfo = input('\nDone entering your expression? Type "y" to calculate otherwise type "n" to continue entering: ')
					if checkInfo == "y":
						calculateResult()



			calculation = input('\nPlease enter your calculation in reverse polish notation or press q to quit: ')
		except ValueError:
			print("Sorry, let's try that input again")
			continue

		if calculation == 'q':
			sys.exit()

		if calculation.isalpha():
			print("\nPlease provide a valid expression to calculate (Maybe try entering numbers!)")
			continue

		else:
			calcArray.append(calculation)

			checkInfo = input('\nDone entering your expression? Type "y" to calculate otherwise type "n" to continue entering: ')

			if checkInfo == "y":
				calculateResult()
			else:
				while True:
					newInput = input('\nPlease enter the rest of your expression: ')
					newCalcArray = calcArray[0] + " " + newInput
					calcArray.clear()
					calcArray.append(newCalcArray)
					checkInfo = input('\nDone entering expression? Type "y" to calculate otherwise type "n" to continue entering: ')
					if checkInfo == "y":
						calculateResult()
						break
					else:
						continue