# Generated by Django 5.1.3 on 2024-11-13 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Full name')),
                ('bio', models.TextField(verbose_name='Bio')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_uz', models.CharField(max_length=255, null=True)),
                ('title_ru', models.CharField(max_length=255, null=True)),
                ('title_en', models.CharField(max_length=255, null=True)),
                ('description', models.TextField()),
                ('description_uz', models.TextField(null=True)),
                ('description_ru', models.TextField(null=True)),
                ('description_en', models.TextField(null=True)),
                ('cover', models.ImageField(upload_to='covers')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.author')),
            ],
        ),
    ]
