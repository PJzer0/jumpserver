# Generated by Django 4.1.13 on 2024-05-09 03:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('acls', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='loginassetacl',
            name='reviewers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Reviewers'),
        ),
        migrations.AddField(
            model_name='loginacl',
            name='reviewers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Reviewers'),
        ),
        migrations.AddField(
            model_name='connectmethodacl',
            name='reviewers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Reviewers'),
        ),
        migrations.AlterUniqueTogether(
            name='commandgroup',
            unique_together={('org_id', 'name')},
        ),
        migrations.AddField(
            model_name='commandfilteracl',
            name='command_groups',
            field=models.ManyToManyField(related_name='command_filters', to='acls.commandgroup', verbose_name='Command group'),
        ),
        migrations.AddField(
            model_name='commandfilteracl',
            name='reviewers',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='Reviewers'),
        ),
        migrations.AlterUniqueTogether(
            name='loginassetacl',
            unique_together={('name', 'org_id')},
        ),
        migrations.AlterUniqueTogether(
            name='commandfilteracl',
            unique_together={('name', 'org_id')},
        ),
    ]
