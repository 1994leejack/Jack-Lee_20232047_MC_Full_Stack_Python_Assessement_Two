from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RenewablePowerGeneration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_of_generation', models.CharField(max_length=100)),
                ('contribution_twh', models.FloatField()),
            ],
        ),
    ]
