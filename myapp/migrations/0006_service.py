# Generated by Django 4.0.3 on 2022-04-19 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_mainproperty_image1_mainproperty_image2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='  name')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('City', models.CharField(max_length=100, verbose_name='City')),
                ('ApartmentSize', models.CharField(max_length=100, verbose_name='ApartmentSize')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]