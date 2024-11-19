from django.db import models

# Create your models here.
class SaveData(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    def __str__(self):
        return self.text