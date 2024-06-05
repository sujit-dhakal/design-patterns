class Observer:
    def Update(self,temperature,humidity):
        pass

class Subject:
    def RegisterObserver(self,observer):
        pass
    def RemoveObserver(self,observer):
        pass
    def notifyObservers(self):
        pass

class WeatherStation(Subject):
    def __init__(self):
        self.observers = []

    def RegisterObserver(self, observer):
        self.observers.append(observer)

    def RemoveObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self,temperature,humidity):
        for observer in self.observers:
            observer.Update(self.temperature,self.humidity)
    def setMeasurements(self,temperature,humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.notifyObservers(self.temperature,self.humidity)

class WeatherObserver(Observer):

    def display(self):
        print(f"temperature: {self.temperature} humidity: {self.humidity}")
    def Update(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

ws = WeatherStation()
wo = WeatherObserver()

ws.RegisterObserver(wo)
ws.setMeasurements(25,70)