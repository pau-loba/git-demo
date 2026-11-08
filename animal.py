import sys

def default():
    print("hello")

def dog():
    print("woof")   
 
def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "dog":
            dog()
        else:
            default()

if __name__ == "__main__":
    main()