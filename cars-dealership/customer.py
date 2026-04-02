class Customer:

    def __init__(self, name, phone, id=None):
        self.id = id
        self.name = name
        self.phone = phone
    

    def __str__(self):
        return f"[ID: {self.id}]  Name: {self.name}  Phone: {self.phone}"
    

    def to_tuple(self):
        return(self.name, self.phone)
















