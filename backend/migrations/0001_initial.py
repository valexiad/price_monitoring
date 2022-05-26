# Generated by Django 4.0.4 on 2022-05-22 16:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackItemHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TrackItemComponents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=150)),
                ('site_type', models.CharField(choices=[('SK', 'SKROUTZ'), ('BG', 'BANGGOOD'), ('LR', 'Leroy Merlin'), ('PR', 'Praktiker')], default='SK', max_length=2)),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.trackitemheader')),
            ],
        ),
    ]
