# reverse-polish-calculator

An in progress reverse polish calculator that runs on your cli.

To run the program, fork and clone the repo, cd into the directory and run python3 calc.py, this will start the calculator!

The calculator accepts valid reverse polish notation, for example 4 + 3 would be written as 4 3 +

The calculator provides instructions as you interact, please follow the provided instructions to avoid as many bugs as possible, this is still a work-in-progress! :)

*Solution

The goal of the solution was to save the user input in a list, then loop through the list until it comes across an operater. When the program finds an operator it removes the operater and the two previous list indexes (the operands for the calculation to be performed on) and perform the calculation based on the operator. The program then inserts the result of that calculation back into the list to be included in further calculations. Aside from some bugs you may come across, this program, as its written, will likely also suffer from performance issues when trying to evaluate huge expressions due to the fact that it is starting over at the beginning of the list every time it completes a calculation, given more time I would come up with a more efficient solution to better handle large expressions, for smaller expressions that isn't as much a concern.
