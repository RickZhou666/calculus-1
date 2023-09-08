from math import sqrt
import numpy as np
from matplotlib import pyplot as plt


def func1(x):
    return (-(x**2) + 3 * x - 1) / 5


def func2(x):
    return ((x**2) - 5) / 2


def func3(x):
    return (x**2 + x - 42) / (x - 6)


def func4(x):
    return abs(x - 3) / (x - 3)


def func5(x):
    return -2 * abs(3*x) / 3*x


def func6(x):
    return (x**2 + 7 * x + 9) / (x**2 - 25)


def func7(x):
    return (x**2 - 4) / (x + 2) ** 2


def func8(x):
    return ((x-2)**2)

# ===============func1()=================================
# x1 = np.linspace(-2, -1.0001, 100)
# x2 = np.linspace(-0.9999, 0, 100)
# plt.plot(x1, func1(x1), color='red')
# plt.plot(x2, func1(x2), color='green')


# ===============func2()=================================
# x1 = np.linspace(-1, 1, 100)
# x1 = np.linspace(-1, -.0001, 100)
# x2 = np.linspace(.0001, 1, 100)
# plt.plot(x1, func1(x1), color='red')
# plt.plot(x2, func1(x2), color='green')

# ===============func3()=================================
# x1 = np.linspace(5, 5.9999, 50)
# x2 = np.linspace(6.0001, 7, 50)
# plt.plot(x1, func3(x1), color='red')
# plt.plot(x2, func3(x2), color='green')


# ===============func4()=================================
# x1 = np.linspace(1, 2.9999, 50)
# x2 = np.linspace(3.0001, 4, 50)
# plt.plot(x1, func4(x1), color='red')
# plt.plot(x2, func4(x2), color='green')


# ===============func5()=================================
# x1 = np.linspace(-1, -.01, 10)
# x2 = np.linspace(.01, 1, 10)
# plt.plot(x1, func5(x1), color='red')
# plt.plot(x2, func5(x2), color='green')


# ===============func6()=================================
# x1 = np.linspace(-5.5, -5.0001, 100)
# x2 = np.linspace(-4.9999, -4.5, 100)
# plt.plot(x1, func6(x1), color='red')
# plt.plot(x2, func6(x2), color='green')

# ===============func7()=================================
# x1 = np.linspace(-2.5, -2.0001, 100)
# x2 = np.linspace(-1.9999, -1.5, 100)
# plt.plot(x1, func7(x1), color='red')
# plt.plot(x2, func7(x2), color='green')

# ===============func8()=================================
x1 = np.linspace(0, 1.9999, 100)
x2 = np.linspace(2.0001, 4, 100)
plt.plot(x1, func8(x1), color='red')
plt.plot(x2, func8(x2), color='green')


def array_print(x1, x2):
    list1, list2 = [], []
    for i in x1:
        list1.append(func8(i))
    for i in x2:
        list2.append(func8(i))
    print(list1)
    print(list2)


def matplot_print():
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("find the limit functions")
    plt.legend()
    plt.show()


array_print(x1, x2)

matplot_print()
# print(func2(0))
