# Generated by Django 3.2.16 on 2022-11-08 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_auto_20221108_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student', to='teacher.grade'),
        ),
    ]