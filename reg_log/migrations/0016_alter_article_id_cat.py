# Generated by Django 4.1 on 2022-10-11 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reg_log', '0015_alter_article_id_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='reg_log.category'),
        ),
    ]
