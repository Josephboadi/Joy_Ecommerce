# Generated by Django 3.0.3 on 2020-04-09 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_delete_carousel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title1', models.CharField(max_length=30)),
                ('overview1', models.CharField(max_length=100)),
                ('image1', models.ImageField(upload_to='')),
                ('title2', models.CharField(max_length=30)),
                ('overview2', models.CharField(max_length=100)),
                ('image2', models.ImageField(upload_to='')),
                ('title3', models.CharField(max_length=30)),
                ('overview3', models.CharField(max_length=100)),
                ('image3', models.ImageField(upload_to='')),
            ],
        ),
    ]
