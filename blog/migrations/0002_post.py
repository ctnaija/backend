# Generated by Django 3.0.6 on 2020-05-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('body', models.TextField()),
                ('publish', models.BooleanField()),
                ('publish_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
    ]
