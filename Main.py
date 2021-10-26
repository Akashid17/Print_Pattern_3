
def Display(iNo):

    if iNo < 0:
        iNo = -iNo

    ch = 'A'

    for x in range (iNo):
        print(ch,end="\t")
        ch = chr(ord(ch)+1)

def main():
    iValue = int(input("Enter Number\n"))
    Display(iValue)

    print()

if __name__ == "__main__":
    main()