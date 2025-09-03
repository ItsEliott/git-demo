class Math():

    def square_root(self , number):
        if number < 0:
            raise ValueError("Veuillez entrer un nombre positif")
        else:
            return number**(1/2)
        
m = Math()

print(m.square_root(12))