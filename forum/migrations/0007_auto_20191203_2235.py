# Generated by Django 2.2.7 on 2019-12-03 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20191203_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='rules',
            field=models.ManyToManyField(blank=True, related_name='threads', related_query_name='thread', to='forum.Rule'),
        ),
    ]
