from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(120)])
    heartrate = models.IntegerField(default=60, validators=[MinValueValidator(1), MaxValueValidator(300)])

    def __str__(self):
        return f"{self.last_name},{self.first_name} is {self.age} years old"

# from office.models import Patient

## Save entries to DB
# carl = Patient(first_name = 'carl', last_name='Smith', age=30)
# carl.save()
# Patient.objects.create(first_name='susan', last_name='Smith',age=40)
# mylist = [Patient(first_name='adam', last_name='smith', age=40), Patient(first_name='karl', last_name='marx', age=40)]
# Patient.objects.bulk_create(mylist)
    
## Read entries from DB
# Patient.objects.all()
# Patient.objects.get(pk=1) (pk = primary key)
# Patient.objects.filter(last_name='smith').all()
# Patient.objects.filter(last_name='smith').filter(age=40).all()
# from django.db.models import Q
# Patient.objects.filter(Q(last_name='smith') & Q(age=40)).all()
# Patient.objects.filter(last_name__startswith='s').all()
# Patient.objects.filter(age__in=[20, 30, 40]).all()
# Patient.objects.filter(age__gte=39),all()
# Patient.objects.order_by('age').all()
    
## Update Entries
# carl = Patient.objects.get(pk=1)
# carl.last_name = 'django'
# carl.save()
    
## Deleting Entries
# carl = Patient.objects.get(pk=1)
# carl.delete()