# Generated by Django 3.2.4 on 2021-07-13 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Staff Name')),
                ('experience', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('more_than_5', 'More than 5')], default='1', max_length=20, verbose_name='Experience in years')),
                ('date_of_joined', models.DateField(auto_now_add=True)),
            ],
        ),
    ]