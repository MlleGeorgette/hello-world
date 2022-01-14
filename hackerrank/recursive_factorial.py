"""
Iteration vs recursion

When we problem solve using recursion, we create a function that breaks down the problem to the smallest bits then
calls itself in order to solve each bit of the problem.

While recursion may be simpler to code, it can take up a lot of memory by repeatedly opening function calls to solve
each bit of the problem thus it is not ideal to use recursion when dealing with really large values for example
finding the factorial of 100,000

Source: https://www.youtube.com/watch?v=wMNrSM5RFMc """


# Iteration
def iterative_factorial(n):
    if n < 0:
        return -1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial


# Recursion
def recursive_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * recursive_factorial(n - 1)


# To test both functions
print(iterative_factorial(10))
print(recursive_factorial(10))
