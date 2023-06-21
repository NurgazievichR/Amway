# Generated by Django 4.2.1 on 2023-05-07 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='title')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]