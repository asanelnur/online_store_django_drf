# Generated by Django 3.2.16 on 2023-07-18 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_alter_basket_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('ProcessInProgress', 'Processinprogress'), ('Cancel', 'Cancel'), ('Paid', 'Paid')], default='New', max_length=20),
        ),
    ]