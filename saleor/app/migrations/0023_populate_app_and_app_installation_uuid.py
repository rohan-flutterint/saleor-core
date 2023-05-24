# Generated by Django 3.2.18 on 2023-04-07 09:44

from django.apps import apps as registry
from django.db import migrations
from django.db.models.signals import post_migrate

from .tasks.saleor3_13 import (
    update_app_installation_uuid_field_task,
    update_app_uuid_field_task,
)


def update_apps_uuid_field_migration(apps, _schema_editor):
    def on_migrations_complete(sender=None, **kwargs):
        update_app_uuid_field_task.delay()
        update_app_installation_uuid_field_task.delay()

    sender = registry.get_app_config("app")
    post_migrate.connect(on_migrations_complete, weak=False, sender=sender)


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0022_auto_20230410_0859"),
    ]

    operations = [
        migrations.RunPython(
            update_apps_uuid_field_migration, reverse_code=migrations.RunPython.noop
        )
    ]