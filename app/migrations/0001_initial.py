# Generated by Django 4.2.6 on 2023-10-13 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=40)),
                ('name', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
            ],
        ),
    ]