from ast import operator
from arithmetic import add, subtract, multiply, divide

calcArray = []

def calculateResult():
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
					inputList.insert(currIdx - 2, str(value))
				if currOperator == '*':
					value = multiply(firstOperand, secondOperand)
					inputList.insert(currIdx - 2, str(value))
				if currOperator == '-':
					value = subtract(firstOperand, secondOperand)
					inputList.insert(currIdx - 2, str(value))
				if currOperator == '/':
					value = divide(firstOperand, secondOperand)
					inputList.insert(currIdx - 2, str(value))

			currIdx += 1

	print('\nsolution', float(inputList[0]), '\n' )

def getInput():
	while True:
		try:
			calculation = input('Please ener your calculation in reverse polish notation: ')
		except ValueError:
			print("Sorry, let's try that input again")
			continue

		if calculation.isalpha():
			print("Please provide a valid expression to calculate (Maybe try entering numbers!)")
			continue

		if calculation[-1] not in ('+-/*'):
			print("Please make sure the calculation is in reverse polish notation (needs to end in + - / or *)")
			continue
		else:
			calcArray.append(calculation)

			checkInfo = input('Done entering info? Type "y" to calculate otherwise type "n" to continue entering: ')

			if checkInfo == "y":
				calculateResult()
			else:
				continue


			












	# if calculation[-1] == '+':
	# 	print(add(calculation[0], calculation[2]))
	# elif calculation[-1] == '-':
	# 	print(subtract(calculation[0], calculation[2]))
	# elif calculation[-1] == '*':
	# 	print(multiply(calculation[0], calculation[2]))
	# elif calculation[-1] == '/':
	# 	print(divide(calculation[0], calculation[2]))
	# else:
	# 	print('Sorry, try again')