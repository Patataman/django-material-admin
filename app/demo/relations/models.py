from django.db import models
from django.utils.translation import gettext_lazy as _


class Relation(models.Model):
    documents = models.ManyToManyField('documents.Document')
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Relation')
        verbose_name_plural = _('Relations')
        db_table = 'relations'
        ordering = ('id',)