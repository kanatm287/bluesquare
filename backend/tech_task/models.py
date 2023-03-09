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


class Client(models.Model):
    full_name = models.CharField(max_length=30,
                                 blank=False)
    gender = models.CharField(max_length=1,
                              choices=Gender.choices)
    birth_date = models.DateField(blank=False)
    address = models.CharField(max_length=100,
                               blank=False)

    def __str__(self):
        return f"Full-name: {self.full_name}"

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_genders_valid",
                check=models.Q(gender__in=Gender.values),
            )
        ]


class InsuranceType(models.TextChoices):
    LIFE = 'L', 'life-insurance'
    MEDICAL = 'M', 'medical-insurance'
    AUTO = 'A', 'auto-insurance'


class Insurance(models.Model):
    insurance_id = models.IntegerField(blank=False,
                                       unique=True)
    insurance_type = models.CharField(max_length=1,
                                      choices=InsuranceType.choices)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_insurance_type_valid",
                check=models.Q(insurance_type__in=InsuranceType.values),
            )
        ]
