# Generated by Django 3.1.2 on 2020-10-13 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpredict', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taskclassification',
            old_name='todo_date',
            new_name='todo_text',
        ),
        migrations.AddField(
            model_name='taskclassification',
            name='todo_pred',
            field=models.CharField(default='PHP', max_length=50),
            preserve_default=False,
        ),
    ]
