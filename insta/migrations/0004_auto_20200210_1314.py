# Generated by Django 2.1 on 2020-02-10 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20200210_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
