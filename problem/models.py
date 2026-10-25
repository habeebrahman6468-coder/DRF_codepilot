from django.db import models

from exams.models import Assessment

from accounts.models import User

# Create your models here.

"""
createnewapp > problem 

Question
-id 
-title CHF()
-description TF()
-score PIF()
-assesment FK(Assesment,ondelete=models.Cascade)
-smapleinput TF(null=True)
-sampleoutput TF()
-createdat
-updatedat
-createdby
"""

class Question(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    score = models.PositiveIntegerField

    assesment =models.ForeignKey(Assessment,ondelete=models.CASCADE)

    smaple_input = models.TextField(null=True)

    sampleoutput = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title