# Generated by Django 3.1.4 on 2021-03-01 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=20)),
                ('name', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
