# Generated by Django 2.2.12 on 2022-02-07 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice_chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=30)),
                ('password', models.TextField(max_length=30)),
                ('data', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_done', models.CharField(blank=True, max_length=150, null=True)),
                ('how_done', models.CharField(blank=True, max_length=150, null=True)),
                ('learn', models.CharField(blank=True, max_length=150, null=True)),
                ('work_next', models.CharField(blank=True, max_length=150, null=True)),
                ('how_next', models.CharField(blank=True, max_length=150, null=True)),
                ('code', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='sites',
            name='site_yaml',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sites',
            name='tree_script',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
