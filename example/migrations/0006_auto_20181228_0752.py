# Generated by Django 2.1.4 on 2018-12-28 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0005_auto_20180922_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorBioMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('body', models.TextField()),
                ('bio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='metadata', to='example.AuthorBio')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='example.Author'),
        ),
    ]
