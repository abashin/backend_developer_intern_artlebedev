# Generated by Django 3.2.19 on 2023-10-06 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20231006_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='terminationStatement',
            field=models.CharField(blank=True, max_length=256, verbose_name='Основание прекращения действия лицензии'),
        ),
    ]