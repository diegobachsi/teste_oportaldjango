# Generated by Django 3.2.6 on 2022-01-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_answerforum'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='qtd_answer',
            field=models.IntegerField(default=0, verbose_name='Qtd Respostas'),
            preserve_default=False,
        ),
    ]