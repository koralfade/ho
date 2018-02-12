# Generated by Django 2.0.2 on 2018-02-03 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=128)),
                ('number_kids', models.IntegerField()),
                ('number_adult', models.IntegerField()),
                ('data', models.DateTimeField()),
                ('message', models.CharField(max_length=256)),
            ],
        ),
    ]
