# Generated by Django 4.0.3 on 2022-04-21 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_service_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='name',
        ),
        migrations.AddField(
            model_name='service',
            name='FullName',
            field=models.CharField(default=1, max_length=100, verbose_name='FullName'),
            preserve_default=False,
        ),
    ]
