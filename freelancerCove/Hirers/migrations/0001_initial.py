# Generated by Django 4.2.16 on 2024-10-05 11:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hirer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('phone_no', models.IntegerField(null=True)),
                ('joined', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
