# Generated by Django 4.2.20 on 2025-03-11 15:00

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
            name='MealPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.DateField()),
                ('monday_food', models.TextField()),
                ('tuesday_food', models.TextField()),
                ('wednesday_food', models.TextField()),
                ('thursday_food', models.TextField()),
                ('friday_food', models.TextField()),
                ('saturday_food', models.TextField()),
                ('sunday_food', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_plans', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
