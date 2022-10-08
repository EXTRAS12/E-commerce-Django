# Generated by Django 4.1.1 on 2022-10-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_options_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Черновик', 'Черновик'), ('Ожидает подтверждения', 'Ожидает подтверждения'), ('Активный', 'Активный'), ('Удалён', 'Удалён')], default='Активный', max_length=50, verbose_name='Статус'),
        ),
    ]
