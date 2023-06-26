# Generated by Django 3.1.3 on 2023-06-26 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='entreprise',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Entreprise'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='fonction',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Fonction'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='photo_profile',
            field=models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='Photo profile'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='telephone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Téléphone'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
