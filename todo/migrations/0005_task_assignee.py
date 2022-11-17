# Generated by Django 4.1.3 on 2022-11-17 10:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0004_task_user_alter_task_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.ManyToManyField(related_name='assignee', to=settings.AUTH_USER_MODEL),
        ),
    ]
