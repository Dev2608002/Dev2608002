# Generated by Django 4.0.3 on 2022-04-21 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='message',
            field=models.CharField(default=2, max_length=100, verbose_name='message'),
            preserve_default=False,
        ),
    ]
