from django.db import models




class Logs(models.Model):
    month = models.CharField(max_length=300, verbose_name="Yil/oy/kun  vaqtlari")
    day = models.CharField(max_length=300, verbose_name="kun  vaqtlari")
    time = models.CharField(max_length=300, verbose_name=" vaqtlari")
    host = models.CharField(max_length=300, verbose_name="host nomi")
    proxy = models.CharField(max_length=300, verbose_name="proxy nomi")
    ip = models.CharField(max_length=300, verbose_name="ip nomi")
    datetime = models.CharField(max_length=300, verbose_name="  vaqtlari")
    type = models.CharField(max_length=300, verbose_name="type turi")
    type_ip = models.CharField(max_length=300, verbose_name=" type ipp addreslari")
    response = models.CharField(max_length=300, verbose_name="qaytgan javoblar_")


    def __str__(self):
        return self.response


    class Meta:
        verbose_name = "Xatolik chiqgan logslar_"


