from django.db import models

# Create your models here.

class books(models.Model):
    book_isbn = models.CharField(unique = True, max_length=80)
    book_title = models.CharField(max_length=250)
    book_author = models.CharField(max_length=250)
    publisher = models.CharField(max_length=250)
    imagine_url_s = models.CharField(max_length=500)
    imagine_url_m = models.CharField(max_length=500)
    imagine_url_l = models.CharField(max_length=500)

class book_ratings(models.Model):
    user_id = models.IntegerField(default = 0)
    book_isbn = models.CharField(max_length=80)
    book_rating = models.IntegerField(default = 0)


