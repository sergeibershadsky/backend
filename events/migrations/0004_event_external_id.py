# Generated by Django 2.2 on 2019-04-25 19:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('events', '0003_remove_activity_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='external_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]