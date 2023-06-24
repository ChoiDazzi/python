class Animal:
    def __init__(self):
        # print("생성자")
        self.flag_sound = True
        
    def die(self):
        self.flag_sound = False
        
    def __del__(self):
        # print("소멸자")
        pass
    def __str__(self):
        return "소리능력" + str(self.flag_sound) 
        
class Human(Animal):
    def __init__(self):
        # 부모 상속 
        super().__init__()
        self.community_skill = 0
    def study(self, hour):
        self.community_skill += hour
        
if __name__ == '__main__':
    a = Human()
    print(a.community_skill)
    print(a.flag_sound)
    a.die()
    a.study(5)
    print(a.community_skill)
    print(a.flag_sound)
    