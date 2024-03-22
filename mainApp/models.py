from django.db import models

# Create your models here.

#+ Product Category Table
class Category(models.Model):
    category_name = models.CharField('kategori adi', max_length=50, unique=True)

    def __str__(self):
        return self.category_name
    
#+ Product Season Category Table
class Season_category(models.Model):
    season_name = models.CharField('Mevsim adi', max_length=50, unique=True)

    def __str__(self):
        return self.season_name

#+ Product Size Table
class Size_species(models.Model):
    size_names = models.CharField('Beden cesitleri', max_length=50, unique=True)
        
    def __str__(self):
        return self.size_names

#+ Product Brand Table
class Brands(models.Model):
    size_names = models.CharField('Urun Markasi', max_length=50, unique=True)

    def __str__(self):
        return self.size_names
    
#+ Product Special States
class SpecialStatus(models.Model):
    states = models.CharField('Ozel durum', max_length=50, unique=True)

    def __str__(self):
        return self.states
    
#+ Product Table Model
class Products(models.Model):
    p_name = models.CharField('urun adi', max_length=50)
    p_price = models.DecimalField('urun fiyati', max_digits=10, decimal_places=2)
    p_information = models.TextField('urun detayi')
    p_category = models.ForeignKey(Category, verbose_name='urun kategorisi', null=True, on_delete=models.CASCADE)
    p_season_category = models.ForeignKey(Season_category, verbose_name='urun mevsimi', null=True, on_delete=models.CASCADE)
    p_sizes = models.ManyToManyField(Size_species, verbose_name='urun bedenleri')
    p_brand = models.ForeignKey(Brands, verbose_name="urun markasi", on_delete=models.CASCADE, null=True)
    p_special_status = models.ManyToManyField(SpecialStatus, verbose_name='ürün özel durumları', blank=True)
    p_img_1 = models.ImageField('urun resmi', upload_to='', max_length=300, null=True)
    p_img_2 = models.ImageField('urun resmi', upload_to='', max_length=300, null=True, blank=True)
    p_img_3 = models.ImageField('urun resmi', upload_to='', max_length=300, null=True, blank=True)
    p_img_4 = models.ImageField('urun resmi', upload_to='', max_length=300, null=True, blank=True)

    def __str__(self):
        return self.p_name

#+ Person Contact Table Model
class Contact(models.Model):
    name = models.TextField("isim", max_length=50)
    surname = models.TextField("soy isim", max_length=50)
    email = models.EmailField("email", max_length=254)
    phone = models.CharField("telefon numarasi", max_length=50)
    message = models.TextField("mesaj notu")
    time_stamp = models.DateTimeField('yorum kayit tarihi', auto_now_add=True, null=True)

    def __str__(self):
        return self.name