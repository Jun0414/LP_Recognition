# Generated by Django 3.0.6 on 2020-06-04 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_auto_20200604_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='lpForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LP_name', models.CharField(max_length=10)),
                ('LP_img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='LP',
        ),
    ]