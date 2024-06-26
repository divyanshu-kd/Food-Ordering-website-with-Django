# Generated by Django 4.2.7 on 2024-06-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipe', '0003_alter_receipe_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='receipe_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='receipe_image',
            field=models.ImageField(null=True, upload_to='Media'),
        ),
        migrations.AlterField(
            model_name='receipe',
            name='receipe_name',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
