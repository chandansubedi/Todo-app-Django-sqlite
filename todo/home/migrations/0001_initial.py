# Generated by Django 4.1.3 on 2022-12-29 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todoName', models.CharField(max_length=100)),
                ('isCompleted', models.BooleanField(default=False)),
                ('createAt', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
