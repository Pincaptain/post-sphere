# Generated by Django 2.2.7 on 2019-12-04 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20191203_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', related_query_name='post', to='forum.Tag'),
        ),
    ]