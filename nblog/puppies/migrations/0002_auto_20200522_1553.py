# Generated by Django 3.0.2 on 2020-05-22 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puppies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='puppy',
            old_name='updated_ad',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='puppy',
            name='breed',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='puppy',
            name='color',
            field=models.CharField(max_length=255),
        ),
    ]
