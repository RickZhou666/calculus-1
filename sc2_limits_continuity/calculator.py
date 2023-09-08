# matplot: https://www.tutorialspoint.com/how-to-plot-a-function-defined-with-def-in-python-matplotlib
# plot mutiple in same graph: https://www.geeksforgeeks.org/plot-multiple-plots-in-matplotlib/
from math import sqrt
import numpy as np
from matplotlib import pyplot as plt

def func1(x):
    return abs(x - 2.0) / (x - 2.0)

def func2(x):
    return 1 / (x - 2.0)

def func3(x):
    return 1 / abs(x - 3.0)
    # return 1 / (x - 3.0)


def func4(x):
    return 1 / x


def func5(x):
    return np.sqrt(x**2)/ x

def func6(x):
    return np.log10(x - 1)

def func7(x):
    return 2*x - 3

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

# ===============func1()=================================
# |x - 2|/ (x - 2)
# x1 = np.linspace(0, 1.999999, 1000)
# x2 = np.linspace(2.000001, 4, 1000)
# plt.plot(x1, func1(x1), color='red')
# plt.plot(x2, func1(x2), color='green')

# ===============func2()=================================
# 1/ (x - 2)
# x1 = np.linspace(1, 1.999999, 50)
# x2 = np.linspace(2.000001, 3, 50)
# plt.plot(x1, func2(x1), color='red')
# plt.plot(x2, func2(x2), color='green')

# ===============func3()=================================
# 1/ |x - 3|
# x1 = np.linspace(2, 2.999999, 50)
# x2 = np.linspace(3.000001, 4, 50)
# plt.plot(x1, func3(x1), color='red')
# plt.plot(x2, func3(x2), color='green')


# ===============func4()=================================
# 1/ x 
# x1 = np.linspace(-0.0005, -0.0001, 100)
# x2 = np.linspace(0.0001, 0.0005, 100)
# plt.plot(x1, func4(x1), color='red')
# plt.plot(x2, func4(x2), color='green')



# ===============func5()=================================
# √x**2/ x 
# x1 = np.linspace(-0.0005, -0.0001, 1000)
# x2 = np.linspace(0.0001, 0.0005, 1000)
# plt.plot(x1, func5(x1), color='red')
# plt.plot(x2, func5(x2), color='green')


# ===============func6()=================================
# √x**2/ x 
# x1 = np.linspace(0, 0.99, 100)
# x2 = np.linspace(1.01, 2, 100)
# plt.plot(x1, func6(x1), color='red')
# plt.plot(x2, func6(x2), color='green')


# ===============func7()=================================
# √x**2/ x 
x1 = np.linspace(2, 3.9999, 100)
x2 = np.linspace(4.0001, 6, 100)
plt.plot(x1, func6(x1), color='red')
plt.plot(x2, func6(x2), color='green')


plt.xlabel("x")
plt.ylabel("y")
plt.title("find the limit functions")
plt.legend()
plt.show()

# func1(1.9)
# func1(1.999)
# func1(1.9999)
# func1(1.99999)
# func1(1.999999)

# func1(2.1)
# func1(2.11)
# func1(2.111)
# func1(2.1111)
# func1(2.11111)


# print(sqrt(3.9))
