# Generated by Django 4.2.8 on 2024-03-31 01:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainApp', '0009_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductComments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='kullanici yorumu')),
                ('city', models.CharField(blank=True, max_length=30, null=True, verbose_name='Sehir')),
                ('time_stamp', models.DateTimeField(auto_now_add=True, verbose_name='yorum kayit tarihi')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='mainApp.products')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]