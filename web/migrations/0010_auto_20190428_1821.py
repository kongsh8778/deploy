# Generated by Django 2.1.4 on 2019-04-28 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20190428_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sqlcredential',
            name='status',
            field=models.IntegerField(choices=[(1, '提交更新'), (2, '负责人审核'), (3, '运维操作'), (4, '否决上线'), (5, '回滚'), (6, '流程结束')], default=1, verbose_name='状态'),
        ),
    ]
