# Generated by Django 4.2.4 on 2023-08-23 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000, verbose_name='content')),
                ('firstPerson', models.CharField(max_length=50, verbose_name='First Person')),
                ('secondPerson', models.CharField(max_length=50, verbose_name='Second Person')),
            ],
        ),
    ]