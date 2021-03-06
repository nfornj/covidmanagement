# Generated by Django 3.2.2 on 2021-05-09 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('covidfeed', '0007_auto_20210509_0609'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bed',
            old_name='bed_request_date',
            new_name='request_date',
        ),
        migrations.RenameField(
            model_name='bed',
            old_name='bed_social_media_content',
            new_name='social_media_content',
        ),
        migrations.RenameField(
            model_name='bed',
            old_name='bed_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='bed',
            old_name='bed_topic_name',
            new_name='topic_name',
        ),
        migrations.RenameField(
            model_name='bed',
            old_name='bed_user_location',
            new_name='user_location',
        ),
        migrations.RenameField(
            model_name='bed',
            old_name='bed_user_name',
            new_name='user_name',
        ),
        migrations.RenameField(
            model_name='oxygen',
            old_name='oxygen_request_date',
            new_name='request_date',
        ),
        migrations.RenameField(
            model_name='oxygen',
            old_name='oxygen_social_media_content',
            new_name='social_media_content',
        ),
        migrations.RenameField(
            model_name='oxygen',
            old_name='oxygen_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='oxygen',
            old_name='oxygen_topic_name',
            new_name='topic_name',
        ),
        migrations.RenameField(
            model_name='oxygen',
            old_name='oxygen_user_location',
            new_name='user_location',
        ),
        migrations.RenameField(
            model_name='oxygen',
            old_name='oxygen_user_name',
            new_name='user_name',
        ),
    ]
