# Generated by Django 3.0.6 on 2020-06-04 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0006_auto_20200604_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lp',
            name='LP_img',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to=''),
        ),
    ]