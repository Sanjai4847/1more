# Generated by Django 4.2.14 on 2024-08-05 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_users_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=120)),
            ],
        ),
    ]
