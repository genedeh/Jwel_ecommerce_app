# Generated by Django 3.2.6 on 2021-10-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0004_auto_20211022_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewelry',
            name='star',
            field=models.FloatField(),
        ),
    ]