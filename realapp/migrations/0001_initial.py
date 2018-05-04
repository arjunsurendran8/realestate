# Generated by Django 2.0.5 on 2018-05-04 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('mobile_no', models.IntegerField()),
                ('password', models.CharField(max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=50)),
                ('item_description', models.CharField(max_length=90)),
                ('item_type', models.CharField(choices=[('V', 'Villa'), ('P', 'Plot'), ('F', 'Flat')], max_length=1)),
                ('item_images', models.ImageField(upload_to='realapp/images')),
                ('name', models.CharField(max_length=15)),
                ('contact_phone_no', models.IntegerField()),
                ('city', models.CharField(choices=[('KOCHI', 'kochi'), ('TRIVANDRUM', 'trivandrum'), ('KOTTAYAM', 'kottayam'), ('THRISSUR', 'thrissur'), ('KOZHIKODE', 'kozhikode')], max_length=20)),
            ],
        ),
    ]
