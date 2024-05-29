class Engine:
    def __init__(self, engine):
        self.engine = engine


class Transmission:
    def __init__(self, transmission):
        self.transmission = transmission


class Body:
    def __init__(self, body):
        self.body = body


class Car:
    def __init__(self, brand, model, color, engine, transmission, body):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine = engine
        self.transmission = transmission
        self.body = body

    def __str__(self):
        return f"{self.brand} {self.model} ({self.color}), Engine: {self.engine.engine}, Transmission: " \
               f"{self.transmission.transmission}, Body: {self.body.body}"


class CarBuilder:
    def __init__(self):
        self.car = Car("", "", "", None, None, None)

    def set_brand(self, brand):
        self.car.brand = brand
        return self

    def set_model(self, model):
        self.car.model = model
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine(self, engine_type):
        self.car.engine = Engine(engine_type)
        return self

    def set_transmission(self, transmission_type):
        self.car.transmission = Transmission(transmission_type)
        return self

    def set_body(self, body_type):
        self.car.body = Body(body_type)
        return self

    def build(self):
        return self.car


class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_car(self):
        return (
            self.builder
            .set_brand("Toyota")
            .set_model("Corolla")
            .set_color("Red")
            .set_engine("V6")
            .set_transmission("Automatic")
            .set_body("Sedan")
            .build()
        )


sedan_builder = CarBuilder()
director = CarDirector(sedan_builder)
sedan = director.construct_car()
print("Создан седан:", sedan)
