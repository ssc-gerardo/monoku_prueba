# Generated by Django 3.1.6 on 2021-02-18 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0003_banda_similares'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='similares',
            field=models.ManyToManyField(blank=True, related_name='_banda_similares_+', to='musica.Banda'),
        ),
    ]