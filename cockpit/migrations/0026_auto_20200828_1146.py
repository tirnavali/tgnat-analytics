# Generated by Django 2.2.13 on 2020-08-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cockpit', '0025_auto_20200828_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acquisitionreport',
            name='created_at',
            field=models.DateField(verbose_name='Kayıdın oluşturulduğu tarih.'),
        ),
    ]