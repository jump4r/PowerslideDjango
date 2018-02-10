from django.db import models

# Create your models here.
class Submission(models.Model):
    user = models.CharField(max_length=32)
    date = models.DateTimeField('Date Sumbitted')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ", by " + self.user

class Beatmap(models.Model):
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    file_path = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=20)

    def __str__(self):
        return self.submission.name + " [" + self.difficulty + "]"
