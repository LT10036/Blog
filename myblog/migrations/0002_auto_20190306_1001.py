# Generated by Django 2.1.7 on 2019-03-06 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'verbose_name_plural': '博主资料'},
        ),
        migrations.AlterModelOptions(
            name='viewpoint',
            options={'verbose_name_plural': '帖子'},
        ),
        migrations.AlterModelOptions(
            name='visitor',
            options={'verbose_name_plural': '访客资料'},
        ),
        migrations.AlterModelOptions(
            name='visitorhistory',
            options={'verbose_name_plural': '访客资料'},
        ),
        migrations.AlterModelTable(
            name='visitorhistory',
            table='vth',
        ),
    ]
