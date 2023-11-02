# Generated by Django 4.2.7 on 2023-11-02 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='views',
        ),
        migrations.RemoveField(
            model_name='question',
            name='vote_count',
        ),
        migrations.AddField(
            model_name='question',
            name='metrics',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]