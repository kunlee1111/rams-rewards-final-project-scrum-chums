# Generated by Django 2.1.4 on 2018-12-13 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitie',
            name='points',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
