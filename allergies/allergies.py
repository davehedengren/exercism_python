class Allergies:
    def __init__(self,n):
        allergy_poss = ['eggs','peanuts','shellfish','strawberries',
                        'tomatoes','chocolate','pollen','cats']
        #This compression loop is stolen from cjchallis
        self.list = [allergy_poss[i] for i in range(len(allergy_poss)) 
                     if (2**i) & n]

    def is_allergic_to(self,a):
        return a in self.list
