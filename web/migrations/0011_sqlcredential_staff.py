# Generated by Django 2.1.4 on 2019-04-29 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20190428_1821'),
    ]

    operations = [
        migrations.AddField(
            model_name='sqlcredential',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.UserInfo'),
        ),
    ]
