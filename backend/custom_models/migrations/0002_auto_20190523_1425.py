# Generated by Django 2.1.7 on 2019-05-23 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('custom_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('order', models.PositiveIntegerField()),
                ('date_created', models.DateTimeField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemText',
            fields=[
                ('item_text_id', models.AutoField(primary_key=True, serialize=False)),
                ('text_detail', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField(blank=True, null=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_models.Item')),
            ],
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('item_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_desc', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
                ('ISO_Code_1', models.CharField(max_length=2)),
                ('ISO_Code_2', models.CharField(max_length=3)),
                ('date_created', models.DateTimeField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField(blank=True, null=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_models.Item')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionType',
            fields=[
                ('question_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_type_desc', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField()),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='question_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_models.QuestionType'),
        ),
        migrations.AddField(
            model_name='itemtext',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_models.Language'),
        ),
        migrations.AddField(
            model_name='item',
            name='item_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custom_models.ItemType'),
        ),
        migrations.AddField(
            model_name='item',
            name='parent_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='custom_models.Item'),
        ),
    ]
