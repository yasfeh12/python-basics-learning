#classes allow us to deffine our own data type.

class friend:
    def __init__(self, name, age, hobby, skillset, why_were_friends,):
        self.name=name
        self.age=age
        self.hobby=hobby
        self.skillset=skillset
        self.why_were_friends=why_were_friends
        
        #class function maybe do more reasearch into this for practice 
    def bestie(self):
        if self.why_were_friends=="fate":
            return True
        else:
            return False
        
        
