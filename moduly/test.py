import sys
from fibo import fib

if __name__ == "__main__":
    print("Uruchamiamy moduł główny")
    fib(int(sys.argv[1]))