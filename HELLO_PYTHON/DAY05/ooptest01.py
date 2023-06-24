class LeeJY:
    def __init__(self):
        self.cnt_company = 10
    def hit(self, punch):
        self.cnt_company += punch

class Biden:
    def __init__(self):
        self.hair_color = "white"
    def dye(self):
        self.hair_color = "red"

class Musk:
    def __init__(self):
        self.cnt_Sat = 1000
    def launch(self):
        self.cnt_Sat += 10

#다중상속
class Eunbi(LeeJY,Biden,Musk):  
    def __init__(self):
        LeeJY.__init__(self)
        Biden.__init__(self)
        Musk.__init__(self)
        
if __name__ == '__main__':
    eb = Eunbi()
    print(eb.cnt_company)
    print(eb.hair_color)
    print(eb.cnt_Sat)
    eb.hit(50)
    eb.dye()
    eb.launch()
    print(eb.cnt_company)
    print(eb.hair_color)
    print(eb.cnt_Sat)
    
    
    
    