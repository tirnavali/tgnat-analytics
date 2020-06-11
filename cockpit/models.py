from django.db import models

# Create your models here.
class ReferenceServiceAnalytic(models.Model):
    user_from_out = models.IntegerField(default=0)
    user_from_inside = models.IntegerField(default=0)

    online_user_outside = models.IntegerField(default=0)
    online_user_inside = models.IntegerField(default=0)

    borrowed_books = models.IntegerField(default=0)
    retired_books = models.IntegerField(default=0)

    photocopy = models.IntegerField(default=0)
    record_date = models.DateTimeField('date data entered')

    def __str__(self):
        return str(self.record_date)