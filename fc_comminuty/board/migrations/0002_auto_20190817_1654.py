# Generated by Django 2.2.3 on 2019-08-17 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={'verbose_name': '패스트캠퍼스 게시글', 'verbose_name_plural': '패스트 캠퍼스 게시글'},
        ),
        migrations.AlterModelTable(
            name='board',
            table='fastcampus_board',
        ),
    ]