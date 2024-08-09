# Generated by Django 5.0.7 on 2024-08-09 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='post/')),
                ('alt_text', models.CharField(default='...', max_length=100)),
                ('width', models.BigIntegerField()),
                ('styles', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.CharField(blank=True, max_length=500, null=True)),
                ('styles', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.CharField(blank=True, max_length=500, null=True)),
                ('styles', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_styles', models.TextField()),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='list', to='post.listitem')),
            ],
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.image')),
                ('list', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.list')),
                ('paragraph', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.paragraph')),
                ('sub_title', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='post.subtitle')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('elements', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.element')),
            ],
        ),
    ]