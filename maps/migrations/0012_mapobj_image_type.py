# Generated by Django 2.0.9 on 2018-11-26 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0011_mapobj'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapobj',
            name='image_type',
            field=models.CharField(choices=[('png', 'png')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]
