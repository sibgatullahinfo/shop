# Generated by Django 5.0.6 on 2024-06-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('limupapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(blank=True, max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(blank=True, max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.ManyToManyField(blank=True, null=True, to='limupapp.subcategory'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='sub_sub_category',
            field=models.ManyToManyField(blank=True, null=True, to='limupapp.subsubcategory'),
        ),
    ]
