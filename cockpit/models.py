from django.db import models
from django.utils import timezone

# Create your models here.

# class SaglamaReport(models.Model):
#     """ Eski model artık kullanılmıyor. """
#     reporter_identity = models.CharField(max_length=60, blank=True, verbose_name="Raporu hazırlayan personel adı soyadı.")
#     reporter_title = models.CharField(max_length=60, blank=True, verbose_name="Raporu hazırlayan personel ünvanı.")
#     date = models.DateField( verbose_name="Raporun ait olduğu tarih")

#     def __str__(self):
#         return str(self.date)

class AcquisitionReport(models.Model):
    """ 
    @Related_with one_to_many  AcquisitionAnalytic \n
    Sağlama birimi modeli. """
    reporter_identity = models.CharField(max_length=60, blank=True, verbose_name="Raporu hazırlayan personel adı soyadı.")
    reporter_title    = models.CharField(max_length=60, blank=True, verbose_name="Raporu hazırlayan personel ünvanı.")
    posted_book       = models.IntegerField(default=0, verbose_name= "Kütüphaneden gönderilen kitap saıyısı.")
    refactored_items  = models.IntegerField(default=0, verbose_name= "Yeniden düzenlenip envanteri yapılan yayın sayısı.")
    notes             = models.TextField(max_length=1500, blank=True, verbose_name="Ekstra not alanı.")
    date              = models.DateField( verbose_name="Raporun ait olduğu tarih")
    created_at        = models.DateField(auto_now = True, verbose_name= "Kayıdın oluşturulduğu tarih.")


    def __str__(self):
        return str(self.date)


class PubType(models.Model):
    """ 
    @Related_with one_to_many  AcquisitionAnalytic \n
    Sağlama birimi modeline bağlı yayın türleri modeli. """
    publication_type = models.CharField(max_length=60, verbose_name="Yayın türü (Kitap, dergi, gazete)")

    def __str__(self):
        return self.publication_type


class AcquisitionAnalytic(models.Model):
    """ 
    @Related_with many_to_one  AcquisitionReport \n
    @Related_with many_to_one  PubType \n
    Sağlama birimine ait olan çeşitli analitikleri içeren model.
     """
    pub_type              = models.ForeignKey(PubType, on_delete=models.CASCADE, verbose_name="Yayın türü (Kitap, dergi, gazete)")
    report                = models.ForeignKey(AcquisitionReport, on_delete=models.CASCADE, verbose_name="Sağlama raporu:")
    pub_arrived_as_supply = models.IntegerField(default=0, verbose_name="Derlemeden gelen yayın sayısı.")
    pub_arrived_as_gift   = models.IntegerField(default=0, verbose_name="Hediye gelen yayın sayısı.")
    pub_bought            = models.IntegerField(default=0, verbose_name="Satın alınan yayın sayısı.")
    pub_saved_as_supply   = models.IntegerField(default=0, verbose_name="Derlemeden koleksiyona alınan yayın sayısı.")
    pub_saved_as_gift     = models.IntegerField(default=0, verbose_name="Hediyelerden koleksiyona alınan yayın sayısı.")
    #pub_saved_as_bought  = models.IntegerField(default=0, verbose_name="Satın alınıp koleksiyona giren yayın sayısı.")
    pub_saved_as_old      = models.IntegerField(default=0, verbose_name="Eski etiketiyle koleksiyona alınan yayın sayısı.")
    #notes                = models.TextField(max_length=1500, blank=True, verbose_name="Ekstra not alanı.")
    #report_date           = models.DateField(verbose_name="Raporun hazırlandığı tarih (Otomatik oluşturulur.)", default=timezone.now)
    #date                 = models.DateField( verbose_name="Raporun ait olduğu tarih")

    def __str__(self):
        return str(self.date) + " Tarihli rapor"




class ReferenceServiceAnalytic(models.Model):
    """     
    Danışma - referans birimine ait olan çeşitli analitikleri içeren model.
     """
    user_from_out                  = models.IntegerField(default=0, verbose_name="Dışarıdan gelen kullanıcı sayısı.")
    user_from_inside               = models.IntegerField(default=0, verbose_name="İçeriden gelen kullanıcı sayısı.")

    online_user_outside            = models.IntegerField(default=0, verbose_name="Dışarıdan gelen online kullanıcı sayısı.")
    online_user_inside             = models.IntegerField(default=0, verbose_name="İçeriden gelen online kullanıcı sayısı.")
    open_access_session_count      = models.IntegerField(default=0, verbose_name="Açık erişim sistemi oturum açmış kullanıcı sayısı.")

    depo_used_book                 = models.IntegerField(default=0, verbose_name="Depodan çıkartılan kitap sayısı.")
    depo_used_journal              = models.IntegerField(default=0, verbose_name="Depodan çıkartılan dergi sayısı.")
    depo_used_newspaper            = models.IntegerField(default=0, verbose_name="Depodan çıkartılan gazete sayısı.")

    book_on_loan                   = models.IntegerField(default=0, verbose_name="Ödünç verilen kitap sayısı.")
    book_renew                     = models.IntegerField(default=0, verbose_name="Süresi uzatılan kitap sayısı.")
    book_withdraw                  = models.IntegerField(default=0, verbose_name="İade edilen kitap sayısı.")
    
    book_on_loan_mp                = models.IntegerField(default=0, verbose_name="Vekillere ödünç verilen kitap sayısı.")
    book_on_loan_retired_mp        = models.IntegerField(default=0, verbose_name="Emekli vekillere ödünç verilen kitap sayısı.")
    book_on_loan_patron_inside     = models.IntegerField(default=0, verbose_name="Personele ödünç verilen kitap sayısı.")

    mp_count_for_book_use          = models.IntegerField(default=0, verbose_name="Kitap ödünç verilen vekil sayısı.")
    retired_mp_count_book_use      = models.IntegerField(default=0, verbose_name="Kitap ödünç verilen emekli vekil sayısı.")
    inside_patron_count_book_use   = models.IntegerField(default=0, verbose_name="Kitap ödünç verilen kurum içi kullanıcı  sayısı.")

    microfilm_use_mp               = models.IntegerField(default=0, verbose_name="Mikrofilm kullanmış vekil sayısı.")
    microfilm_use_retired_mp       = models.IntegerField(default=0, verbose_name="Mikrofilm kullanmış emekli vekil sayısı.")
    microfilm_use_patron_inside    = models.IntegerField(default=0, verbose_name="Mikrofilm kullanmış kurum içi personel sayısı.")
    microfilm_use_patron_outside   = models.IntegerField(default=0, verbose_name="Mikrofim kullanmış kurum dışı personel sayısı.")
    microfilm_income               = models.FloatField(default = 0, verbose_name="Mikrofilmden tahsil edilen TL.")
    
    photocopy_a4_formal            = models.IntegerField(default=0, verbose_name="A4 boyutunda resmi fotokopi sayısı.")
    photocopy_a3_formal            = models.IntegerField(default=0, verbose_name="A3 boyutunda resmi fotokopi sayısı.")
    photocopy_a4_paid              = models.IntegerField(default=0, verbose_name="A4 boyutunda ücreti ödenmiş fotokopi sayısı.")
    photocopy_a3_paid              = models.IntegerField(default=0, verbose_name="A3 boyutunda ücreti ödenmiş fotokopi sayısı.")
    dijitalized_papers             = models.IntegerField(default = 0, verbose_name="Dijital kopya sayısı.")
    photocopy_income               = models.FloatField(default = 0, verbose_name="Fotokopiden tahsil edilen TL.")

    notes                          = models.TextField(max_length=1500, blank=True, verbose_name="Ekstra not alanı.")
    reporter_identity              = models.CharField(max_length=60, blank=True, verbose_name="Raporu hazırlayan personel adı soyadı.")
    reporter_title                 = models.CharField(max_length=60, blank=True, verbose_name="Raporu hazırlayan personel ünvanı.")
    report_date                    = models.DateField(verbose_name="Raporun hazırlandığı tarih (Otomatik oluşturulur.)", default=timezone.now)
    date                           = models.DateField( verbose_name="Raporun ait olduğu tarih")

   

    def __str__(self):
        return str(self.date) + " Tarihli Kayıt."


    def is_minus_value_entered(self):
        """ 
        returns Boolean\n
        Tam sayı alanlarda negatif değer var ise False döner."""
        return (int(self.user_from_out)            < 0 or 
            int(self.user_from_inside)             < 0 or
            int(self.online_user_inside)           < 0 or
            int(self.online_user_outside)          < 0 or
            int(self.open_access_session_count)    < 0 or
            int(self.depo_used_book)               < 0 or
            int(self.depo_used_journal)            < 0 or
            int(self.depo_used_newspaper)          < 0 or 
            int(self.book_on_loan)                 < 0 or 
            int(self.book_on_loan_mp)              < 0 or
            int(self.book_on_loan_patron_inside)   < 0 or
            int(self.mp_count_for_book_use)        < 0 or
            int(self.retired_mp_count_book_use)    < 0 or
            int(self.inside_patron_count_book_use) < 0 or
            int(self.microfilm_use_mp)             < 0 or
            int(self.microfilm_use_retired_mp)     < 0 or
            int(self.microfilm_use_patron_inside)  < 0 or
            int(self.microfilm_use_patron_outside) < 0 or
            float(self.microfilm_income)           < 0 or
            int(self.photocopy_a4_formal)          < 0 or
            int(self.photocopy_a3_formal)          < 0 or
            int(self.photocopy_a4_paid)            < 0 or
            int(self.photocopy_a3_paid)            < 0 or
            int(self.dijitalized_papers)           < 0 or
            float(self.photocopy_income)           < 0
            )
