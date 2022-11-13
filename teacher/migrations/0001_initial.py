# Generated by Django 3.2.16 on 2022-11-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='学生姓名')),
                ('age', models.SmallIntegerField()),
                ('sex', models.SmallIntegerField(default=1)),
                ('qq', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20, verbose_name='电话')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]