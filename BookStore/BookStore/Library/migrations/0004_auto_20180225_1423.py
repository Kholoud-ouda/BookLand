# Generated by Django 2.0.2 on 2018-02-25 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0003_auto_20180224_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='pic',
            field=models.ImageField(default='Authors/No_picture_available.png', null=True, upload_to='Authors'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pic',
            field=models.ImageField(default='Books/No_picture_available.png', null=True, upload_to='Books'),
        ),
    ]
