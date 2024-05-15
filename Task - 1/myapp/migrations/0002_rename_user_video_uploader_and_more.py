# Generated by Django 5.0.6 on 2024-05-15 13:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='user',
            new_name='uploader',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='url',
            new_name='video_url',
        ),
        migrations.AlterField(
            model_name='video',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]