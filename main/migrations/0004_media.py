# Generated by Django 4.0.4 on 2022-05-24 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_task_options_alter_task_order_with_respect_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('image', models.ImageField(upload_to='media_image')),
                ('url', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Media',
            },
        ),
    ]