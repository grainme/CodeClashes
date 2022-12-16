#sum the digits of a given number untill its length is equal to 1:
--->#Implementation
def main():
    n=int(input())
    if n==0:
        print(0)
    elif n%9==0:
        print(9)
    else:
        print(n%9)
if __name__ == '__main__':
    main()
