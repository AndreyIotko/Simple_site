# Generated by Django 3.2.4 on 2022-06-06 17:35

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='certificates/%Y/%m/%d')),
                ('link', models.URLField(unique=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Certificate',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=128)),
                ('telegram', models.URLField()),
                ('img', models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='img/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, default='placeholder.png', null=True, upload_to='thumbnail/%Y/%m/%d')),
                ('headline', models.CharField(max_length=256)),
                ('sub_headline', models.CharField(blank=True, max_length=256, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('git', models.URLField(blank=True, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('tags', models.ManyToManyField(blank=True, to='base.Tag')),
            ],
        ),
    ]
