# Generated by Django 4.0.3 on 2022-05-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mitglieder',
            fields=[
                ('vname', models.CharField(max_length=255)),
                ('nname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('mitgliedsnr', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
