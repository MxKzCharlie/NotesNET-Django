# Generated by Django 5.0.7 on 2024-08-20 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
