# Generated by Django 2.1.4 on 2019-02-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('actor', models.CharField(max_length=100)),
                ('picture', models.FileField(upload_to='images/pics/')),
            ],
        ),
    ]
