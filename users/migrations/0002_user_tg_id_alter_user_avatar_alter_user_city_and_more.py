# Generated by Django 5.0.6 on 2024-07-05 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="tg_id",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="ID в телегераме"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(
                blank=True, null=True, upload_to="users/", verbose_name="Аватар"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Город"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="Почта"),
        ),
        migrations.AlterField(
            model_name="user",
            name="phone_number",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="Номер телефона"
            ),
        ),
    ]
