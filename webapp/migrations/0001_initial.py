# Generated by Django 3.0.8 on 2020-07-23 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=30)),
                ('contact_email', models.CharField(max_length=30)),
                ('contact_msg', models.CharField(max_length=300)),
            ],
        ),
    ]
