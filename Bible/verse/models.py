from django.db import models

# Create your models here.
class Bible(models.Model):
    book = models.IntegerField(db_column='Book', blank=True, null=True)  # Field name made lowercase.
    chapter = models.IntegerField(db_column='Chapter', blank=True, null=True)  # Field name made lowercase.
    versecount = models.IntegerField(db_column='Versecount', blank=True, null=True)  # Field name made lowercase.
    verse = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'BIBle'
