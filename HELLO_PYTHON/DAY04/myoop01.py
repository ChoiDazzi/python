class Vehicle:
    def __init__(self):
        self.wheel_cnt = 2
    def flex(self):
        self.wheel_cnt = 4

class Car: 
    def hit(self):
        self.autopilot_level += 1 
    
if __name__ == '__main__':
    c = Car()
    print(c.wheel_cnt)
    print(c.autopilot_level)
    c.flex()
    c.hit()
    print(c.wheel_cnt)
    print(c.autopilot_level)
    