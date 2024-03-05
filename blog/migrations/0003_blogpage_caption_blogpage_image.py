# Generated by Django 4.2.10 on 2024-03-04 06:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        ('blog', '0002_blogpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='caption',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image'),
        ),
    ]
