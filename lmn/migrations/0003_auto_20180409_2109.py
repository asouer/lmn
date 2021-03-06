# Generated by Django 2.0.3 on 2018-04-10 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0002_auto_20180409_1917'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.AddField(
            model_name='artist',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
        migrations.AddField(
            model_name='show',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
        migrations.AddField(
            model_name='venue',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
        migrations.AlterField(
            model_name='note',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
    ]
