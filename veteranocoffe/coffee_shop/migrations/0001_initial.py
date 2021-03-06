# Generated by Django 2.0.7 on 2018-08-11 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('map_url', models.URLField(max_length=254)),
                ('facebook_url', models.URLField(max_length=254)),
                ('instgram_url', models.URLField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='news_images/')),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='publication_images/')),
            ],
        ),
    ]
