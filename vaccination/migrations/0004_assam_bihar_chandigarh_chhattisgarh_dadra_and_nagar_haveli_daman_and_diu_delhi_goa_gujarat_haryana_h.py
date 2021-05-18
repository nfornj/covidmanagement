# Generated by Django 3.2.2 on 2021-05-18 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccination', '0003_arunachal_pradesh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Bihar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Chandigarh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Chhattisgarh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Dadra_and_nagar_haveli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Daman_and_diu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Delhi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Goa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Gujarat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Haryana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Himachal_pradesh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Jammu_and_kashmir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Jharkhand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Karnataka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Kerala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ladakh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Lakshadweep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Madhya_pradesh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Maharashtra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Manipur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Meghalaya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Mizoram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Nagaland',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Odisha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Puducherry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Punjab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rajasthan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Sikkim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tamil_nadu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Telangana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tripura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Uttar_pradesh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Uttarakhand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='West_bengal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(max_length=1024)),
                ('district_id', models.IntegerField()),
                ('name', models.CharField(max_length=1024)),
                ('vaccine_date', models.DateField()),
                ('available_capacity', models.IntegerField()),
                ('vaccine', models.CharField(max_length=50)),
                ('status', models.CharField(default='DEFAULT', max_length=10)),
            ],
        ),
    ]
