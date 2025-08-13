from appetizer.main import Appetizer

def hello() -> str:
    print("Hello from customer!")
    for appetizer in Appetizer:
        print(appetizer)

if __name__ == "__main__":
    hello()
