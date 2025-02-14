# Generated by Django 4.1.5 on 2024-03-10 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=200)),
                ('institution', models.CharField(max_length=200)),
                ('avatar', models.ImageField(default='avatar.svg', null=True, upload_to='')),
                ('year_started', models.DateField()),
                ('year_completed', models.DateField()),
            ],
            options={
                'ordering': ['year_completed'],
            },
        ),
    ]
