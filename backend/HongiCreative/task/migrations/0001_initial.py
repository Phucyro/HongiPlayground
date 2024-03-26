# Generated by Django 5.0.3 on 2024-03-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('todo', 'Todo'), ('done', 'Done')], default='todo', max_length=10)),
            ],
        ),
    ]
