# Generated by Django 4.2.2 on 2023-06-27 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('keywords', models.TextField()),
                ('awards', models.TextField()),
                ('education', models.TextField()),
                ('graduation_date', models.CharField(max_length=255)),
                ('job_title', models.TextField()),
                ('previous_organization', models.TextField()),
                ('certifications', models.TextField()),
            ],
        ),
    ]
