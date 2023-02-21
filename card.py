# Name: Maria Azconegui 

class Card:
    def __init__(self, value:range(1,10), suit:str):
        self.value = value
        self.suit = suit
    def __repr__(self): 
        return f"Card(value = {self.value},suit = {self.suit})"
    def __str__(self): 
        return f"{self.value} of {self.suit}"
    def __eq__(self):
        return (self.value, self.suit) == (self.value, self.suit)


    
