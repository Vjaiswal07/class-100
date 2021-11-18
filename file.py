class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color=color
        self.model=model
        self.company=company
        self.speed_limit=speed_limit
    def start(self):
        print("start")
    def stop(self):
        print("stop")
    def accelerate(self):
        print("accelrating")
honda=Car("civic","red","honda","50")
print(honda.color)
honda.start()
 