from django.db import models
from .base_model import BaseModel
from .type import Type
from .status import Status

class Issue(BaseModel):
    summary = models.CharField(max_length=300,verbose_name="кратакое описание")
    description = models.TextField(null=True, blank=True, verbose_name="полное описание")
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="статус")
    type = models.ForeignKey(Type, on_delete=models.PROTECT,verbose_name="тип")

    def __str__(self):
        return self.summary

    class Meta:
        verbose_name = "задача"
        verbose_name_plural = "задачи"