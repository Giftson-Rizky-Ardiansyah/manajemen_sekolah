from django.db import models

class Sekolah(models.Model):
    id = models.AutoField(primary_key=True)
    nama = models.CharField(max_length=255)
    npsn = models.CharField(max_length=255)
    alamat = models.CharField(max_length=255)
    kelurahan = models.CharField(max_length=255, blank=True, null=True)
    kecamatan = models.CharField(max_length=255, blank=True, null=True)
    kabupaten_kota = models.CharField(max_length=255, blank=True, null=True)
    provinsi = models.CharField(max_length=255, blank=True, null=True)
    kode_pos = models.CharField(max_length=10, blank=True, null=True)
    telepon = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=255, blank=True, null=True)
    facebook = models.URLField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'sekolah'

    def __str__(self):
        return self.nama
