# Generated by Django 4.2.5 on 2023-12-16 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khata', '0003_applyloan_depositetype_openaccount'),
    ]

    operations = [
        migrations.CreateModel(
            name='heroImages',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('image', models.ImageField(default='default_image.jpg', upload_to='media/images/')),
            ],
        ),
        migrations.RemoveField(
            model_name='openaccount',
            name='mothersname',
        ),
        migrations.AddField(
            model_name='applyloan',
            name='selected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='depositetype',
            name='selected',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='openaccount',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
