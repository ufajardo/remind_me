# Generated by Django 2.2.1 on 2019-05-08 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remindme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
