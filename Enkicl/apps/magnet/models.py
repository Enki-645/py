# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Magnet(models.Model):
    """
    磁力
    """
    title = models.CharField(max_length=255, verbose_name='磁力标题', blank=True, null=True)
    magnet = models.CharField(max_length=255, verbose_name='磁力链接', blank=True, null=True)
    data_list = models.TextField(blank=True, verbose_name='磁力内容', null=True)
    create_time = models.DateField(blank=True, verbose_name='创建时间', null=True)
    file_count = models.CharField(max_length=255, verbose_name='文件数量', blank=True, null=True)
    file_size = models.CharField(max_length=255, verbose_name='文件大小', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'magnet'
        verbose_name = "磁力"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
