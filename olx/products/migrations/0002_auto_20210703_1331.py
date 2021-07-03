# Generated by Django 3.2.4 on 2021-07-03 13:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='owner',
            name='profilePicture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='owner',
            name='rating',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='owner',
            name='rollNo',
            field=models.CharField(default=200101001, max_length=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AddField(
            model_name='product',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='lastModified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Images', to='products.product'),
        ),
    ]