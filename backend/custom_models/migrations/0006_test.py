# Generated by Django 2.1.7 on 2019-06-03 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_models', '0005_upload_emib_sample'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('is_public', models.BooleanField(blank=True, default=False)),
                ('default_time', models.IntegerField(blank=True, null=True)),
                ('test_type', models.CharField(max_length=100)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_models.Item')),
            ],
        ),
    ]