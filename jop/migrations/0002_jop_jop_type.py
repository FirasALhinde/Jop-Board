# Generated by Django 3.2 on 2023-01-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop',
            name='jop_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default=' ', max_length=50),
            preserve_default=False,
        ),
    ]
