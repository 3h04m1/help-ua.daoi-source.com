# Generated by Django 4.0.2 on 2022-03-01 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_needhelp_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='help',
            name='category',
            field=models.CharField(choices=[('cazare', 'Cazare | Проживання'), ('transport', 'Transport | Транспорт'), ('consiliere', 'Consiliere | Консультування'), ('voluntariat', 'Волонтерство, переклад'), ('donatii', 'Haine, alimente | Одяг, їжа'), ('lucru', 'Lucru | Работа '), ('medical', 'Servicii medicale | Медицинские услуги')], default='None', max_length=20, null=True),
        ),
    ]
