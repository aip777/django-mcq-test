# Generated by Django 3.0.9 on 2020-10-20 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0008_remove_makequestion_ans_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinformation',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]
