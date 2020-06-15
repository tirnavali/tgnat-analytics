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
    record_date = models.DateTimeField()

    def __str__(self):
        return str(self.record_date)

    def is_minus_value_entered(self):
        return (int(self.user_from_out)       < 0 or 
            int(self.user_from_inside)    < 0 or
            int(self.online_user_inside)  < 0 or
            int(self.online_user_outside) < 0 or
            int(self.borrowed_books)      < 0 or
            int(self.retired_books)       < 0 or
            int(self.photocopy)           < 0)
