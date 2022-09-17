# Generated by Django 4.0.2 on 2022-07-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the publisher', max_length=50)),
                ('website', models.URLField(help_text='Publisher website')),
                ('email', models.EmailField(help_text='The publisher email', max_length=254)),
            ],
        ),
    ]
