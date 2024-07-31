from django.db import models
from sekolah.models import Sekolah
from siswa.models import Siswa
from tahunajaran.models import TahunAjaran

class Guru(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=10, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    nomor_hp = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    alamat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'guru'


class KepalaSekolah(models.Model):
    id = models.BigAutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    jenis_kelamin = models.CharField(max_length=10, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    nomor_hp = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    alamat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'kepalasekolah'

