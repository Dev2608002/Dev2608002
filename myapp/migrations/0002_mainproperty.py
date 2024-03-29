# Generated by Django 4.0.3 on 2022-03-19 08:42

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='mainproperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=100, verbose_name='Post Title')),
                ('details', models.CharField(max_length=1000, verbose_name='Post Details')),
                ('PostDate', models.DateField(default=datetime.date.today)),
                ('WriterName', models.CharField(max_length=100, verbose_name='Write Name')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
