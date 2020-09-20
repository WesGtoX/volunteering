from django.db import models


class Action(models.Model):
    name = models.CharField('Nome', max_length=80, blank=False, null=False)
    institution = models.CharField('Instituição', max_length=100, blank=False, null=False)
    address = models.CharField('Endereço', max_length=255, blank=False, null=False)
    neighborhood = models.CharField('Bairro', max_length=100, blank=False, null=False)
    city = models.CharField('Cidade', max_length=100, blank=False, null=False)
    description = models.CharField('Descrição', max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'
        ordering = ['id', 'name', 'institution']
