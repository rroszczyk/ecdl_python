def power(a, b):
  print(a ** b)

def fib(n):
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a + b
  print()

if __name__ == "__main__":
  print(f"To jest jakiś moduł {__name__}")
