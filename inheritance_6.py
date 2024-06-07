class Transport:
    def move(self):
        pass


class WaterTransport(Transport):
    def float(self):
        pass


class AirTransport(Transport):
    def fly(self):
        pass


class Aviation(AirTransport):
    def carry_passengers(self):
        pass


class Dirigible(AirTransport):
    def navigate(self):
        pass


class GroundTransport(Transport):
    def drive(self):
        pass


class RailwayTransport(GroundTransport):
    def carry_freight(self):
        pass


class CarTransport(GroundTransport):
    def honk(self):
        pass


class BicycleTransport(GroundTransport):
    def ring_bell(self):
        pass


class AnimalPoweredTransport(GroundTransport):
    def walk(self):
        pass


class SpaceTransport(Transport):
    def launch(self):
        pass
