class Observer:    #observer   behavioural
    def update(self, state):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, state):
        for observer in self._observers:
            observer.update(state)

class Sensor(Subject):
    def __init__(self, threshold):
        super().__init__()
        self._threshold = threshold

    def read_data(self, light_level):
        if light_level < self._threshold:
            self.notify("ON")
        else:
            self.notify("OFF")

class Lamp(Observer):
    def update(self, state):
        if state == "ON":
            print("Lamp is turned ON")
        else:
            print("Lamp is turned OFF")

if __name__ == "__main__":
    sensor = Sensor(threshold=5)
    lamp = Lamp()

    sensor.attach(lamp)

    sensor.read_data(3)  # Low light level, should turn the lamp ON
    sensor.read_data(7)  # High light level, should turn the lamp OFF
