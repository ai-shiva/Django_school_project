# Generated by Django 3.2.4 on 2021-07-14 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Parent Name')),
                ('relation', models.CharField(choices=[('father', 'Father'), ('mother', 'Mother'), ('guardian', 'Guardian')], max_length=20, verbose_name='Student Relation')),
            ],
        ),
    ]
