from arithmetic import add, subtract, multiply, divide

print('Welcome to the reverse polish calculator')
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
		break
if calculation[-1] == '+':
	print(add(calculation[0], calculation[2]))
elif calculation[-1] == '-':
	print(subtract(calculation[0], calculation[2]))
elif calculation[-1] == '*':
	print(multiply(calculation[0], calculation[2]))
elif calculation[-1] == '/':
	print(divide(calculation[0], calculation[2]))
else:
	print('Sorry, try again')
