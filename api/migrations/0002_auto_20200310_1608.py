# Generated by Django 2.2.7 on 2020-03-10 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coraltype',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]