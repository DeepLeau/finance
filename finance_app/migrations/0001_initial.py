# Generated by Django 3.2.12 on 2024-10-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField()),
                ('open_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('close_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('high_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('low_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.BigIntegerField()),
            ],
        ),
        migrations.AddIndex(
            model_name='stockdata',
            index=models.Index(fields=['symbol', 'timestamp'], name='finance_app_symbol_a4e601_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='stockdata',
            unique_together={('symbol', 'timestamp')},
        ),
    ]
