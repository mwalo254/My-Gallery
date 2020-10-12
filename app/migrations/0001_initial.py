# Generated by Django 3.1.2 on 2020-10-12 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=30)),
                ('image_description', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='welcome/')),
                ('img_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
                ('img_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.location')),
            ],
            options={
                'ordering': ['image_name'],
            },
        ),
    ]
