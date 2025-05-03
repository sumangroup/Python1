class vehicle:
    def __init__(self,model,mileage,price):
        self.model=model
        self.mileage=mileage
        self.price=price

    def show_details(self):
        print(self.model)
        print(self.mileage)
        print(self.price)

class bike(vehicle):
    def __init__(self,model,mileage,price,tyre,cc):
        super().__init__(model,mileage,price)
        self.tyre=tyre
        self.cc=cc

    def show_details(self):
        super().show_details()
        print(self.tyre)
        print(self.cc)

class car(bike,vehicle):
    def rating(self):
        print('5 star')


bajaj = bike("Dominar",40,145000,2,500)
bajaj.show_details()

print()
tata = car("Safari",25,2500000,4,2000)
tata.show_details()
tata.rating()
        
