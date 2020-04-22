from django.db import models

# Create your models here.


# class Post_Client(models.Model):
#     i = models.CharField(max_length=200)

#     def __str__(self):
#         return self


# class On_The(models.Model):
#     on_the = models.CharField(max_length=200)

#     def __str__(self):
#         return self


# class Time_Day(models.Model):
#     time_day = models.CharField(max_length=200)

#     def __str__(self):
#         return self


# class Post(models.Model):
#     post_client = models.ForeignKey(Post_Client, on_delete=models.CASCADE)
#     on_the = models.ForeignKey(On_The, on_delete=models.CASCADE)
#     time_day = models.ForeignKey(Time_Day, on_delete=models.CASCADE)
