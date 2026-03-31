class Car():

    def __init__(self, make, model, year, price, mileage, id=None):
        self.make = make
        self.model = model
        if year > 0:
            self.year = year
        else:
            raise ValueError("Year must be positive like 1922")
        
        if price > 0:
            self.price = year
        else:
            raise ValueError("Price must be positive like 1922")
        
        self.mileage = mileage
        self.id = id
    

    def __str__(self):
        return f"[ID: {self.id}] {self.year} {self.make} {self.model} | ${self.price:,.2f} | {self.mileage} km"
    

    def to_tuple(self):
        return(self.make, self.model, self.year, self.price, self.mileage)
    


     



