
def factorial(n):
    if n == 2:
        return n
    else:

        return n * factorial(n-1)


results = factorial(5)
print(results)