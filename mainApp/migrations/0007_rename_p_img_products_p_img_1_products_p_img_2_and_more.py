# Generated by Django 4.2.8 on 2024-03-18 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0006_products_p_brand'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='p_img',
            new_name='p_img_1',
        ),
        migrations.AddField(
            model_name='products',
            name='p_img_2',
            field=models.ImageField(max_length=300, null=True, upload_to='', verbose_name='urun resmi'),
        ),
        migrations.AddField(
            model_name='products',
            name='p_img_3',
            field=models.ImageField(max_length=300, null=True, upload_to='', verbose_name='urun resmi'),
        ),
        migrations.AddField(
            model_name='products',
            name='p_img_4',
            field=models.ImageField(max_length=300, null=True, upload_to='', verbose_name='urun resmi'),
        ),
    ]
