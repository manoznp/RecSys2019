# Generated by Django 2.1.4 on 2019-01-30 10:58

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190130_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinaton_type', multiselectfield.db.fields.MultiSelectField(choices=[('Adventure', 'Adventure'), ('Pilgrims', 'Pilgrims'), ('Waterbody', 'Waterbody'), ('Himalayas', 'Himalayas'), ('Nature Seeing', 'Nature Seeing'), ('Others', 'Others')], max_length=59)),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Destination')),
            ],
        ),
        migrations.AlterField(
            model_name='trekkingtype',
            name='trekking_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cycling', 'Cycling'), ('Walking', 'Walking'), ('Biking', 'Biking'), ('Peak Climbing', 'Peak Climbing'), ('Others', 'Others')], max_length=43),
        ),
    ]
