# Generated by Django 3.1.7 on 2021-03-31 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210331_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.CharField(default=2, max_length=255, verbose_name='warranty'),
            preserve_default=False,
        ),
    ]
