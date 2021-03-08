# Generated by Django 3.1.7 on 2021-03-01 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UseCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_clothes', models.CharField(choices=[('1-5', (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'))), ('6-10', (('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'))), ('11-15', (('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'))), ('16-20', (('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20')))], max_length=6)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateField()),
                ('collection_info', models.DateTimeField()),
                ('status', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.student')),
            ],
        ),
    ]
