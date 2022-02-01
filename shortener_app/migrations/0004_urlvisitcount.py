# Generated by Django 4.0.2 on 2022-02-01 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shortener_app', '0003_alter_shortener_short_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='URLVisitCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shortener_app.shortener')),
            ],
        ),
    ]