from django.db import models


class Voluntary(models.Model):
    first_name = models.CharField('Nome', max_length=80, blank=False, null=False)
    last_name = models.CharField('Sobrenome', max_length=100, blank=False, null=False)
    neighborhood = models.CharField('Bairro', max_length=80, blank=False, null=False)
    city = models.CharField('Cidade', max_length=100, blank=False, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Voluntário'
        verbose_name_plural = 'Voluntários'
        ordering = ['id', 'first_name', 'last_name']
