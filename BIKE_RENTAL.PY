class bikeShop:
    def __init__(self,stock):
        self.stock = stock

    def displayBike(self):
        print("TOTAL BIKES",self.stock)

    def rentforBike(self,quantity):

        if quantity <= 0:
            print("ENTER THE POSITIVE VALUE OR GREATER THAN ZERO")

        elif quantity > self.stock:
            print("ENTER THE VALUE LESS THAN STOCK")

        else:
            self.stock = self.stock - quantity
            print("TOTAL PRICES", quantity*100)
            print("TOTAL BIKES",self.stock)

while True:
    obj = bikeShop(100)
    userchoice = int(input(''' 

    1 DISPLAY STOCKS
    2 RENT A BIKE
    3 EXIT
    '''))

    if userchoice ==1:
        obj.displayBike()

    elif userchoice ==2:
        n = int(input("ENTER THE QUANTITY: ---"))
        obj.rentforBike(n)

    else:
        break


    
