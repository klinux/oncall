# Generated by Django 4.2.7 on 2023-11-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0039_remove_alertreceivechannel_unique_integration_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='alertreceivechannel',
            name='alert_group_labels_custom',
            field=models.JSONField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='alertreceivechannel',
            name='alert_group_labels_template',
            field=models.TextField(default=None, null=True),
        ),
    ]