# Generated by Django 5.0.2 on 2024-02-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogpage', '0003_alter_blogpostmodel_title1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostcontent',
            name='subtitle',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
