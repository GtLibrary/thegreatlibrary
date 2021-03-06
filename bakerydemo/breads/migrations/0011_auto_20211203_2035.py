# Generated by Django 3.2.9 on 2021-12-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breads', '0010_auto_20211203_2031'),
    ]

    operations = [
        migrations.AddField(
            model_name='breadpage',
            name='startpoint',
            field=models.TextField(blank=True, help_text='the startpoint of this piece'),
        ),
        migrations.AlterField(
            model_name='breadpage',
            name='maxbooksupply',
            field=models.TextField(blank=True, help_text='the max number of books this smart book has. -1 == infinity'),
        ),
    ]
