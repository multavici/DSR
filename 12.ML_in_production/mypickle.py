import pickle


class Car:
    def __init__(self, brand, model, horsepower):
        self.brand = brand
        self.model = model
        self.horsepower = horsepower

    def __str__(self):
        return "{} {} {}PS".format(self.brand, self.model, self.horsepower)

    # def __getstate__(self):
    #     state = self.__dict__
    #     return state

    def __setstate__(self, state):
        if 'horsepower' not in state:
            state['horsepower'] = 'n/a'
        self.__dict__.update(state)


def create_and_persist():
    cars = [Car('Opel', 'Kadett') for i in range(5)]
    with open('cars.pkl', 'wb') as f:
        pickle.dump(cars, f)


def load_and_display():
    with open('cars.pkl', 'rb') as f:
        cars = pickle.load(f)
    for car in cars:
        print(str(car))


#create_and_persist()
load_and_display()
