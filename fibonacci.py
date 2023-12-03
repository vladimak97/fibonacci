# Write a Python function to generate the first n terms of the Fibonacci sequence.

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence[:n]

n = 10
fib_terms = fibonacci(n)
print(f"First {n} terms of Fibonacci sequence: {fib_terms}")