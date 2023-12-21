# Generated by Django 4.2.7 on 2023-12-15 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('email', models.EmailField(max_length=128, verbose_name='Email')),
                ('subject', models.CharField(max_length=256, verbose_name='Subject')),
                ('body', models.CharField(max_length=2048, verbose_name='Body')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.AlterField(
            model_name='rate',
            name='buy',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Buy'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='currency_type',
            field=models.SmallIntegerField(choices=[(1, 'Dollar'), (2, 'Euro')], default=1, verbose_name='Currency type'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='sell',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Sell'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='source',
            field=models.CharField(max_length=254, verbose_name='Source'),
        ),
    ]