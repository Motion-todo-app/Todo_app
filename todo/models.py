from django.db import models
from django.utils.translation import gettext_lazy as _  # renaming variables
# Create your models here.

class Category(models.Model):
    name = models.CharField(_('Category Name'), max_length=200,
                            blank=False,
                            null=True,
                            help_text='Add categories to your task.')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Status(models.Model):
    name = models.CharField(_('Status Name'), max_length=200,
                            blank=False,
                            null=True,
                            help_text='Add status of your task.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

class Task(models.Model):
    name = models.CharField(_('What\'s to be done'), max_length=250,
                            blank=False,
                            null=True,
                            help_text='Add your todo task.')
    date = models.DateField(_('Pick a date'),
                            null=True,
                            blank=False,
                            help_text='Click the box and select date.')
    time = models.DateField(_('Pick a time'),
                            null=True,
                            blank=False,
                            help_text='Click the box and select time.')
    category = models.ForeignKey(
                                 Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=False,
                                 help_text='Click the dropdown and select your category.')
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        help_text='Click the dropdown and select your category.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todo'