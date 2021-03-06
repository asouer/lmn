# Generated by Django 2.0.3 on 2018-04-10 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lmn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(default='pictures/None/no-image.jpg', upload_to='pictures/')),
            ],
        ),
        migrations.AddField(
            model_name='note',
            name='picture',
            field=models.ImageField(default='pictures/None/no-image.jpg', upload_to='pictures/'),
        ),
    ]
