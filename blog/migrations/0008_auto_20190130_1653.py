# Generated by Django 2.1.4 on 2019-01-30 11:08

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190130_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccomodationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accomodation_type', multiselectfield.db.fields.MultiSelectField(choices=[('Hotel', 'Hotel'), ('Teahouse', 'Teahouse'), ('Motel', 'Motel'), ('Himalayas', 'Himalayas'), ('Tent', 'Tent'), ('Homestay', 'Homestay')], max_length=44)),
            ],
        ),
        migrations.AddField(
            model_name='destination',
            name='altitude',
            field=models.FloatField(default='1'),
        ),
        migrations.AddField(
            model_name='destination',
            name='difficulty',
            field=models.FloatField(default='1'),
        ),
        migrations.AddField(
            model_name='destination',
            name='security',
            field=models.FloatField(default='1'),
        ),
        migrations.AddField(
            model_name='destination',
            name='temperature',
            field=models.FloatField(default='1'),
        ),
        migrations.AddField(
            model_name='accomodationtype',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Destination'),
        ),
    ]
