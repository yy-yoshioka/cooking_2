# Generated by Django 3.1.2 on 2020-11-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201110_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='featuredpost',
            name='featured_id',
            field=models.IntegerField(default=0),
        ),
    ]
