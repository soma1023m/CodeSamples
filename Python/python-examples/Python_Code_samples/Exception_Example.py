def getPrice():
    while True:
        try:
            money=int(input("Enter a number"))
            if(money>100):
                raise Exception("Too Much Money")
            return money
        except Exception as ex:
            print("Exception occured {0}".format(ex))
        
def main():
    moneyR=getPrice()
    print("Money entered {0}".format(moneyR))
    
if __name__ == "__main__":
    main()

    