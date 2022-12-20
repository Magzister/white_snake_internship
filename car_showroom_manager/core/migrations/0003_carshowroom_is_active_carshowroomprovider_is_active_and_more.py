# Generated by Django 4.1.4 on 2022-12-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_carshowroom_carshowroomvehisle_provider_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="carshowroom",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="carshowroomprovider",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="carshowroomspecialoffer",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="carshowroomvehiclecharacteristics",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="carshowroomvehisle",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="desiredvehiclecharacteristics",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="provider",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="providerdiscount",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="providerpurchasehistory",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="providerspecialoffer",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="providervehicle",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="providervehiclecharacteristics",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="userpurchasehistory",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
