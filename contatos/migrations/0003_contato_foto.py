# Generated by Django 4.1.5 on 2023-01-31 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contatos", "0002_contato_mostar"),
    ]

    operations = [
        migrations.AddField(
            model_name="contato",
            name="foto",
            field=models.ImageField(blank=True, upload_to="fotos/%Y/%m/%d"),
        ),
    ]
