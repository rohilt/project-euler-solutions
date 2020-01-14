'''
I will compute the Fibonacci numbers, and add every third number starting with 2, 
to sum up only the even numbers. 
'''
fib = [1, 2]
while (fib[len(fib)-1] < 4000000):
    x = fib[len(fib)-1] + fib[len(fib)-2]
    fib.append(x)
fib.pop()
i = 1
sum = 0
while i < len(fib):
    sum += fib[i]
    i += 3
print(sum)