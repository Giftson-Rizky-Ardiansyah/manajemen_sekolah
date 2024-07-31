# tahunajaran/models.py
from django.db import models

class TahunAjaran(models.Model):
    tahun_ajaran = models.CharField(max_length=10)

    class Meta:
        db_table = 'tahunajaran'

