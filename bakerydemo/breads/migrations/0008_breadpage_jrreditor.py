# Generated by Django 3.2.9 on 2021-12-03 04:24

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('breads', '0007_remove_breadpage_contactid'),
    ]

    operations = [
        migrations.AddField(
            model_name='breadpage',
            name='jrreditor',
            field=djrichtextfield.models.RichTextField(blank=True),
        ),
    ]
