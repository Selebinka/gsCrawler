# Generated by Django 2.2.3 on 2019-07-18 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleResultModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=255)),
                ('link', models.URLField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='GoogleResult',
        ),
    ]