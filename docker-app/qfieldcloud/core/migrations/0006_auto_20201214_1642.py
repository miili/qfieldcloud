# Generated by Django 2.2.17 on 2020-12-14 16:42

import json
import django.contrib.postgres.fields.jsonb
from django.db import migrations


def jsonify_output_field(apps, schema_editor):
    # Old values in output field of delta table where string instead of json
    Delta = apps.get_model('core', 'Delta')
    for delta in Delta.objects.all():
        delta.output = json.dumps([{"msg": delta.output}])
        delta.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20201203_1037'),
    ]

    operations = [
        migrations.RunPython(jsonify_output_field),
        migrations.AlterField(
            model_name='delta',
            name='output',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
