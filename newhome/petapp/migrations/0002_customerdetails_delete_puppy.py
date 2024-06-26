# Generated by Django 5.0.1 on 2024-03-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('quantity', models.PositiveIntegerField(max_length=50)),
                ('number', models.PositiveIntegerField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='puppy',
        ),
    ]
