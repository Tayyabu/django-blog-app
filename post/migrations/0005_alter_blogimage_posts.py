# Generated by Django 5.1 on 2024-08-29 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_post_intro_post_content_blogimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimage',
            name='posts',
            field=models.ManyToManyField(related_name='images', to='post.post'),
        ),
    ]