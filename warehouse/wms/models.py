from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length = 25)
    password = models.CharField(max_length = 20)

class Signup(models.Model):
    name = models.CharField(max_length = 25)
    email = models.CharField(max_length = 25)
    phone = models.IntegerField()
    address = models.CharField(max_length = 50)
    password = models.CharField(max_length = 8)

class Add_buildings(models.Model):
    name = models.CharField(max_length = 30)
    area = models.IntegerField()
    floor = models.IntegerField()
    identifier = models.CharField(max_length = 30)
    height = models.IntegerField()
    structure = models.CharField(max_length = 30)
    flooring = models.CharField(max_length = 30)

class Add_racks(models.Model):
    building_id = models.ForeignKey(Add_buildings, on_delete = models.CASCADE)
    rack_name = models.CharField(max_length = 30)
    weight = models.IntegerField()
    nof_bins = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    length = models.IntegerField()

class Add_bin(models.Model):
    bin_id = models.AutoField(primary_key = True)
    rack_id = models.ForeignKey(Add_racks, on_delete = models.CASCADE)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()


class Add_supervisor(models.Model):
    supervisor_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 25)
    email = models.CharField(max_length = 25)
    phone = models.IntegerField()
    address = models.CharField(max_length = 30)
    ssn = models.IntegerField()

class Add_employee(models.Model):
    employee_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length =25)
    phone = models.IntegerField()
    address = models.CharField(max_length =50)
    ssn = models.IntegerField()
    tin = models.IntegerField()
    employee_type = models.CharField(max_length = 20)

class Add_rows(models.Model):
    building_id = models.ForeignKey(Add_buildings, on_delete = models.CASCADE)
    rack_id = models.ForeignKey(Add_racks, on_delete = models.CASCADE)
    name = models.CharField(max_length = 25)
    weight = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    length = models.IntegerField()

class Add_products(models.Model):
    product_id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 25)
    brand = models.CharField(max_length =25)
    model = models.CharField(max_length =25)
    quantity = models.IntegerField()
    weight = models.IntegerField()
    length = models.IntegerField()
    Width = models.IntegerField()
    height = models.IntegerField()

class Add_box(models.Model):
    box_id = models.AutoField(primary_key = True)
    product_id = models.ForeignKey(Add_products, on_delete=models.CASCADE)
    bin_id = models.ForeignKey(Add_bin, on_delete=models.CASCADE)
    note = models.CharField(max_length = 50)
    date = models.DateField()
    time = models.TimeField()
    status = models.IntegerField()
