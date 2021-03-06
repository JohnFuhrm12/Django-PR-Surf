# Generated by Django 4.0.3 on 2022-04-20 22:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('surf_report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('url_field', models.URLField(blank=True, default=None)),
                ('favorites', models.ManyToManyField(blank=True, default=None, related_name='favorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
