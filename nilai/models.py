# nilai/models.py
from django.db import models

class Nilai(models.Model):
    id_siswa = models.IntegerField()
    id_guru = models.IntegerField()
    id_tahun = models.IntegerField()
    mata_pelajaran = models.CharField(max_length=255)
    nilai = models.CharField(max_length=10)

    class Meta:
        db_table = 'nilai'  # Pastikan nama tabel di sini sesuai
