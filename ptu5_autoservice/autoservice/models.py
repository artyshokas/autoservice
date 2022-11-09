from django.db import models

class Car_model(models.Model):
    make = models.CharField('Make', max_length=100, help_text='Enter car make')
    model = models.CharField('Model', max_length=100, help_text='Enter car model')
    year = models.IntegerField('year')
    engine = models.CharField('Engine', max_length=20)


    def __str__(self) -> str:
        return f"{self.make} {self.model} {self.year} {self.engine}"


class Client(models.Model):
    name = models.CharField('First name', max_length=100)
    surname = models.CharField('Last name', max_length=100)

    def __str__(self) -> str:
        return f"{self.name} {self.surname}"


class Car(models.Model):
    number = models.CharField('number', max_length=10, help_text='Enter car reg. number')
    car_name = models.ForeignKey(Car_model, on_delete=models.CASCADE, null=True, blank=True)
    vin = models.CharField('VIN', max_length=17, help_text='Enter VIN')
    owner = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.car_name}, {self.number}, {self.vin}"



class Service(models.Model):
    name = models.CharField('Service name', max_length=100, help_text='Enter service name')
    car = models.ManyToManyField(Car_model)

    def __str__(self) -> str:
        return f"{self.name}"

    def display_cars(self):
        return ', '.join(car.make for car in self.car.all())
    display_cars.short_description= 'Car(s)'

class Price(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField('price', max_digits=18, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.service}: {self.price}"





class Order(models.Model):
    date = models.DateField('Order date', null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    # client_id = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    total = models.ForeignKey(Price, on_delete=models.DO_NOTHING, null=True)

    def __str__(self) -> str:
        return f"{self.car}"


class Order_line(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True)
    pcs = models.IntegerField('PCS.')
    price = models.DecimalField('Price', max_digits=18, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.service}  PCS: {self.pcs}  price {self.price} total: {self.pcs * self.price}"