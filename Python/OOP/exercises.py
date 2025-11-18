import time;

class Clock:
    def __init__(self):
        self.hour = 0;
        self.minute = 0;
        self.second = 0;
    
    def goTime(self):
        for h in range(0, 24):
            self.hour = h;
            for m in range(0,60):
                self.minute = m;
                for s in range(0,60):
                    self.second = s;
                    time.sleep(1)
                    print(f'{self.hour}h - {self.minute}min - {self.second}s')

clock = Clock()
clock.goTime()