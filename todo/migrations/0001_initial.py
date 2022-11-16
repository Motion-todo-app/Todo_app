# Generated by Django 4.1.3 on 2022-11-16 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Add categories to your task.', max_length=200, null=True, verbose_name='Category Name')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Add your todo task.', max_length=250, null=True, verbose_name="What's to be done")),
                ('date', models.DateField(help_text='Click the box and select date.', null=True, verbose_name='Pick a date')),
                ('time', models.DateField(help_text='Click the box and select time.', null=True, verbose_name='Pick a time')),
                ('category', models.ForeignKey(help_text='Click the dropdown and select your category.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='todo.category')),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todo',
            },
        ),
    ]