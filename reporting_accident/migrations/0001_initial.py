# Generated by Django 3.2.5 on 2021-07-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('accident_id', models.AutoField(db_column='Accident_ID', primary_key=True, serialize=False)),
                ('accident_volume', models.CharField(db_column='Accident_Volume', max_length=45)),
                ('accident_description', models.CharField(db_column='Accident_Description', max_length=45)),
                ('place_long', models.FloatField(db_column='Place_Long')),
                ('place_lat', models.FloatField(db_column='Place_Lat')),
                ('special_case_1', models.IntegerField(blank=True, db_column='Special_Case_1', null=True)),
                ('special_case_2', models.IntegerField(blank=True, db_column='Special_Case_2', null=True)),
                ('special_case_3', models.IntegerField(blank=True, db_column='Special_Case_3', null=True)),
                ('special_case_4', models.IntegerField(blank=True, db_column='Special_Case_4', null=True)),
                ('accident_time', models.DateTimeField(db_column='Accident_Time')),
            ],
            options={
                'db_table': 'ACCIDENT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.AutoField(db_column='Hospital_ID', primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(db_column='Hospital_Name', max_length=45)),
                ('place_long', models.FloatField(db_column='Place_Long')),
                ('place_lat', models.FloatField(db_column='Place_Lat')),
                ('governerate', models.CharField(db_column='Governerate', max_length=45)),
                ('city', models.CharField(db_column='City', max_length=45)),
                ('saturday', models.IntegerField(db_column='Saturday')),
                ('sunday', models.IntegerField(db_column='Sunday')),
                ('monday', models.IntegerField(db_column='Monday')),
                ('tuesday', models.IntegerField(db_column='Tuesday')),
                ('wednesday', models.IntegerField(db_column='Wednesday')),
                ('thursday', models.IntegerField(db_column='Thursday')),
                ('friday', models.IntegerField(db_column='Friday')),
            ],
            options={
                'db_table': 'HOSPITAL',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('reporter_id', models.AutoField(db_column='Reporter_ID', primary_key=True, serialize=False)),
                ('phone_number', models.CharField(db_column='Phone_Number', max_length=11)),
                ('reporter_name', models.CharField(db_column='Reporter_Name', max_length=45)),
                ('national_number', models.CharField(blank=True, db_column='National_Number', max_length=14, null=True)),
            ],
            options={
                'db_table': 'REPORTER',
                'managed': False,
            },
        ),
    ]
