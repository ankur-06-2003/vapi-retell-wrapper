# Generated by Django 4.2.6 on 2025-04-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_description_agent_firstmessage'),
    ]

    operations = [
       
        migrations.AddField(
            model_name='agent',
            name='speed',
            field=models.FloatField(default=1, verbose_name=range(0, 5)),
        ),
    ]
