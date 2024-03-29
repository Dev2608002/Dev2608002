# Generated by Django 4.0.3 on 2022-03-19 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_mainproperty_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100, verbose_name=' First name')),
                ('Lastname', models.CharField(max_length=100, verbose_name=' last name')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('subject', models.CharField(max_length=100, verbose_name='subject')),
                ('message', models.CharField(max_length=100, verbose_name='message')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]
