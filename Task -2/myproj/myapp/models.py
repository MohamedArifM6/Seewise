from django.db import models

class Machine(models.Model):
    machine_name = models.CharField(max_length=100)
    machine_serial_no = models.CharField(max_length=50)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.machine_name

class ProductionLog(models.Model):
    cycle_no = models.CharField(max_length=20)
    unique_id = models.CharField(max_length=50)
    material_name = models.CharField(max_length=100)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.FloatField()  
    ideal_cycle_time = models.FloatField()  
    actual_output = models.IntegerField()   
    good_products = models.IntegerField()   
    total_products = models.IntegerField()  

    def calculate_oee(self):
        
        available_time = 24 * 3  
        available_operating_time = self.total_products * self.ideal_cycle_time
        unplanned_downtime = available_time - available_operating_time
        availability = (available_time - unplanned_downtime) / available_time

      
        performance = (self.ideal_cycle_time * self.actual_output) / available_operating_time

       
        quality = (self.good_products / self.total_products)

    
        oee = availability * performance * quality * 100
        return oee
    def save(self, *args, **kwargs):
        self.oee = self.calculate_oee()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.cycle_no} - {self.material_name}"
