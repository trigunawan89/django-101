from django.db import models
import uuid
from django.template.defaultfilters import slugify
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

my_choices = (
    ('one', 'number one'),
    ('two', 'number two')
)

class TestModel(models.Model):
    boolean = models.BooleanField(default=True, verbose_name='this is a boolean field')
    char = models.CharField(verbose_name='New name', max_length=220, unique=True, help_text='added help text')
    date = models.DateField(default=timezone.now)
    decimal = models.DecimalField(max_digits=5, decimal_places=2)
    email = models.EmailField(max_length=200)
    file = models.FileField(upload_to='uploads', blank=True)
    image = models.ImageField(upload_to='uploads', blank=True)
    integer = models.IntegerField()
    positive_small_int = models.PositiveSmallIntegerField()
    slug = models.SlugField(blank=True)
    text = models.TextField()
    url = models.URLField(max_length=200)
    uuid1 = models.UUIDField(default=uuid.uuid4)
    uuid2 = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    date_and_time = models.DateTimeField()
    choice = models.CharField(max_length=10, choices=my_choices)
    # field added after some time
    new_field = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    # 3rd party
    phone_number = PhoneNumberField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.text[:30])
        super().save(*args, **kwargs)