# Generated by Django 4.1.5 on 2023-01-13 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PRODUCTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.CharField(max_length=100)),
                ('discounted_price', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('comp', models.TextField(default='')),
                ('category', models.CharField(choices=[('ts', 'T-SHIRTS'), ('ho', 'HOODIES'), ('bo', 'BOOKS'), ('jo', 'JOURNAL'), ('po', 'PROFIT DIARY'), ('ga', 'GAMES'), ('ne', 'NEWSPAPER')], max_length=2)),
                ('prod_img', models.ImageField(upload_to='product')),
            ],
        ),
    ]