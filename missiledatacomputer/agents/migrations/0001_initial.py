# Generated by Django 4.1 on 2024-06-05 20:14

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('model_type', models.CharField(default='unidentified', max_length=50, verbose_name='model')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('owner', models.CharField(blank=True, max_length=50)),
                ('hostility', models.CharField(choices=[('H', 'Hostile'), ('F', 'Friendly'), ('N', 'Neutral')], default='N', max_length=10)),
                ('stationary', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LocationRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)])),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)])),
                ('agent', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='agents.agent')),
            ],
        ),
    ]