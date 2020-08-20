# Generated by Django 2.2.13 on 2020-07-22 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cockpit', '0006_auto_20200722_1614'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referenceserviceanalytic',
            old_name='microfilm_mp',
            new_name='microfilm_use_mp',
        ),
        migrations.RenameField(
            model_name='referenceserviceanalytic',
            old_name='microfilm_patron_inside',
            new_name='microfilm_use_patron_inside',
        ),
        migrations.RenameField(
            model_name='referenceserviceanalytic',
            old_name='microfilm_patron_outside',
            new_name='microfilm_use_patron_outside',
        ),
        migrations.RenameField(
            model_name='referenceserviceanalytic',
            old_name='microfilm_retired_mp',
            new_name='microfilm_use_retired_mp',
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='book_on_loan',
            field=models.IntegerField(default=0, verbose_name='Ödünç verilen kitap sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='book_on_loan_mp',
            field=models.IntegerField(default=0, verbose_name='Vekillere ödünç verilen kitap sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='book_on_loan_patron_inside',
            field=models.IntegerField(default=0, verbose_name='Personele ödünç verilen kitap sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='book_on_loan_retired_mp',
            field=models.IntegerField(default=0, verbose_name='Emekli vekillere ödünç verilen kitap sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='book_renew',
            field=models.IntegerField(default=0, verbose_name='Süresi uzatılan kitap sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='book_withdraw',
            field=models.IntegerField(default=0, verbose_name='İade edilen kitap sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='inside_patron_count_book_use',
            field=models.IntegerField(default=0, verbose_name='Kitap ödünç verilen kurum içi kullanıcı  sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='microfilm_income',
            field=models.FloatField(default=0, verbose_name='Mikrofilmden tahsil edilen TL.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='mp_count_for_book_use',
            field=models.IntegerField(default=0, verbose_name='Kitap ödünç verilen vekil sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='open_access_session_count',
            field=models.IntegerField(default=0, verbose_name='Açık erişim sistemi oturum açmış kullanıcı sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='photocopy_a3_formal',
            field=models.IntegerField(default=0, verbose_name='A3 boyutunda ücreti ödenmiş fotokopi sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='photocopy_a4_formal',
            field=models.IntegerField(default=0, verbose_name='A4 boyutunda resmi fotokopi sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='photocopy_a4_paid',
            field=models.IntegerField(default=0, verbose_name='A4 boyutunda ücreti ödenmiş fotokopi sayısı.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='photocopy_income',
            field=models.FloatField(default=0, verbose_name='Fotokopiden tahsil edilen TL.'),
        ),
        migrations.AddField(
            model_name='referenceserviceanalytic',
            name='retired_mp_count_book_use',
            field=models.IntegerField(default=0, verbose_name='Kitap ödünç verilen emekli vekil sayısı.'),
        ),
    ]