# Generated by Django 2.1.4 on 2019-01-30 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190129_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrekkingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trekking_type', models.CharField(choices=[('Cycling', 'Cycling'), ('Walking', 'Walking'), ('Biking', 'Biking'), ('Peak Climbing', 'Peak Climbing'), ('Others', 'Others')], max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='destination',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='trekkingtype',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Destination'),
        ),
    ]
