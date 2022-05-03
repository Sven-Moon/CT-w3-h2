# Write a recursion function to perform the fibonacci sequence up to the number passed in.

# Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8

def fib(n):
    if n > 1:
        return fib(n-1) + fib(n-2)
    else: 
        return 1
    
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(10))
print(fib(20))
print(fib(21))
print(fib(22))
