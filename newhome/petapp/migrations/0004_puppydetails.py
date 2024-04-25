# Generated by Django 5.0.1 on 2024-03-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0003_alter_customerdetails_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='puppydetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('breed', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('vaccination', models.CharField(max_length=50)),
                ('number', models.PositiveIntegerField()),
            ],
        ),
    ]