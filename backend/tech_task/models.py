from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.
def validate_gender(value):
    if value not in ['male', 'female', 'not decided']:
        raise ValidationError(_('%(value)s is not gender'), params={'value': value})


class Gender(models.TextChoices):
    MALE = 'M', 'male'
    FEMALE = 'F', 'female'
    UN_DECIDED = 'U', 'undecided'


class Clients(models.Model):
    full_name = models.CharField(max_length=30,
                                 blank=False)
    gender = models.CharField(max_length=1,
                              choices=Gender.choices)
    birth_date = models.DateField(blank=False)
    address = models.CharField(max_length=100,
                               blank=False)
    insurance_id = models.IntegerField(blank=False,
                                       unique=True)

    def __str__(self):
        return f"Full-name: {self.full_name}, Gender: {self.gender}, Birth-date: {self.birth_date}, " \
               f"Address: {self.address}, Insurance-id: {self.insurance_id}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_genders_valid",
                check=models.Q(gender__in=Gender.values),
            )
        ]
