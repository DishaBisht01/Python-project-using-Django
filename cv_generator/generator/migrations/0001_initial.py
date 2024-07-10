# Generated by Django 4.2.6 on 2024-07-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('summary', models.TextField()),
                ('degree', models.CharField(max_length=100)),
                ('school', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('previous_work', models.TextField()),
                ('skills', models.TextField()),
            ],
        ),
    ]
