# Generated by Django 4.1 on 2022-09-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg_log', '0002_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='last_change',
            field=models.DateField(auto_now=True),
        ),
    ]
