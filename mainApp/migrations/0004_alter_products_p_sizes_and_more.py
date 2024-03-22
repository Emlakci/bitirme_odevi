# Generated by Django 4.2.8 on 2024-03-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_specialstatus_products_p_category_products_p_img_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='p_sizes',
            field=models.ManyToManyField(to='mainApp.size_species', verbose_name='urun bedenleri'),
        ),
        migrations.AlterField(
            model_name='products',
            name='p_special_status',
            field=models.ManyToManyField(blank=True, to='mainApp.specialstatus', verbose_name='ürün özel durumları'),
        ),
    ]
