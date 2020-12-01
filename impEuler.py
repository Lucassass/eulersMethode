from simpleeval import SimpleEval
import math

# The formula is a string so i can evaluate it using simple eval.
formula = "y*(1-pow(y,2))"

# Initial values.
x = 0
y = 0.5

# Max calc.
MAX = 5

# Step rate.
h = 0.05

# Functions which it recognize in the eval.
supported_functions = {"pow": math.pow}

# I use simpleeval to eval using these params.
evaluat = SimpleEval(names={"x": x, "y": y}, functions=supported_functions)

# Where i store the results. 
results = []
results.append([x, y])

# Evaluates the passed formula using passed variables.
def step1(x, y, formula):
	return evaluat.eval(formula)

# Calculates the y*(n+1) using the formula and passed variables.
def step2(x, y, h, formula):
	return y + h * step1(x, y, formula)

# Calculates the y(n+1) using the formula and passed variables.
def step3(x, y, h, formula):
	return y + h * (step1(x, y, formula) + step1(x + h, step2(x, y, h, formula), formula)) / 2

# Print results.
def printResults(results):
	print("\n***RESULTS***")
	for r in results:
		print(r[0], "\t", r[1])
	print()

while x <= MAX:
	y = step3(x, y, h, formula)
	x += h

                    #  Here i define the specific amount of digits i want.
	values = [float("{0:.2f}".format(x)), float("{0:.2f}".format(y))]
	results.append(values)

printResults(results)