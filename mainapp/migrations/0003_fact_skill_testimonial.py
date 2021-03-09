# Generated by Django 3.1.7 on 2021-03-07 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210307_0032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clients', models.IntegerField()),
                ('projects', models.IntegerField()),
                ('supporthour', models.IntegerField()),
                ('worker', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html', models.IntegerField()),
                ('css', models.IntegerField()),
                ('javascript', models.IntegerField()),
                ('php', models.IntegerField()),
                ('wordpress', models.IntegerField()),
                ('android', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('review', models.TextField()),
                ('profile', models.ImageField(max_length=255, upload_to='')),
            ],
        ),
    ]