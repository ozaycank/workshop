# Generated by Django 4.0.3 on 2022-04-22 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.CharField(max_length=20)),
                ('latitude', models.CharField(max_length=20)),
                ('radius', models.CharField(max_length=20)),
            ],
        ),
    ]
