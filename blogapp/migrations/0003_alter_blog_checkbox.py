# Generated by Django 3.2.6 on 2021-09-02 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blog_checkbox'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='checkbox',
            field=models.BooleanField(choices=[(False, 'Draft'), (True, 'Publish')], default=True),
        ),
    ]
