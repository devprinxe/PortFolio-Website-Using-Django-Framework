# Generated by Django 3.1.7 on 2021-03-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('website', models.URLField(blank=True, null=True)),
                ('city', models.CharField(max_length=200)),
                ('role', models.CharField(max_length=200)),
                ('birhtday', models.DateField()),
                ('age', models.IntegerField()),
                ('aboutme', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(max_length=200)),
                ('twitter', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('skype', models.CharField(max_length=200)),
                ('linkedin', models.CharField(max_length=200)),
            ],
        ),
    ]
