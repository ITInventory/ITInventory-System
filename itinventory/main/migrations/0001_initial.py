# Generated by Django 4.0.2 on 2022-02-14 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_id', models.CharField(max_length=100)),
                ('current_computer_id', models.CharField(max_length=100)),
                ('pic', models.CharField(max_length=100)),
                ('previous_pic', models.CharField(max_length=100)),
                ('pccurrentstatus', models.CharField(default='', editable=False, max_length=100)),
                ('Brand', models.CharField(max_length=100)),
                ('Model', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('asset_no', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('pctype', models.CharField(max_length=100)),
                ('processor_type', models.CharField(max_length=100)),
                ('ram_type', models.CharField(max_length=100)),
                ('ram_slot', models.CharField(max_length=100)),
                ('total_ram', models.CharField(max_length=100)),
                ('storage_type', models.CharField(max_length=100)),
                ('storage_space', models.CharField(max_length=100)),
                ('dop', models.CharField(max_length=100)),
                ('dop_Warranty_end_date', models.CharField(max_length=100)),
                ('po', models.CharField(max_length=100)),
                ('invoice', models.CharField(max_length=100)),
                ('block', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('standard_installation', models.CharField(max_length=100)),
                ('microsoft_office', models.CharField(max_length=100)),
                ('microsoft_office_keys', models.CharField(max_length=100)),
                ('windows', models.CharField(max_length=100)),
                ('type_of_purchase', models.CharField(max_length=100)),
                ('lan_mac_address', models.CharField(max_length=100)),
                ('lan_ip_address', models.CharField(max_length=100)),
                ('wlan_mac_address', models.CharField(max_length=100)),
                ('wlan_ip_address', models.CharField(max_length=100)),
                ('joined_domain', models.CharField(max_length=100)),
                ('connection_type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Computer',
                'db_table': 'Computer',
            },
        ),
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('ip_assisgned', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('remark', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'IP',
                'db_table': 'IP',
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_id', models.CharField(max_length=100)),
                ('pic', models.CharField(max_length=100)),
                ('previous_pic', models.CharField(max_length=100)),
                ('current_computer_id', models.CharField(max_length=100)),
                ('Brand', models.CharField(max_length=100)),
                ('Model', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('asset_no', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('processor_type', models.CharField(max_length=100)),
                ('ram_type', models.CharField(max_length=100)),
                ('ram_slot', models.CharField(max_length=100)),
                ('total_ram', models.CharField(max_length=100)),
                ('storage_type', models.CharField(max_length=100)),
                ('storage_space', models.CharField(max_length=100)),
                ('dop', models.CharField(max_length=100)),
                ('dop_Warranty_end_date', models.CharField(max_length=100)),
                ('po', models.CharField(max_length=100)),
                ('invoice', models.CharField(max_length=100)),
                ('block', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('standard_installation', models.CharField(max_length=100)),
                ('microsoft_office', models.CharField(max_length=100)),
                ('microsoft_office_keys', models.CharField(max_length=100)),
                ('windows', models.CharField(max_length=100)),
                ('type_of_purchase', models.CharField(max_length=100)),
                ('lan_mac_address', models.CharField(max_length=100)),
                ('lan_ip_address', models.CharField(max_length=100)),
                ('wlan_mac_address', models.CharField(max_length=100)),
                ('wlan_ip_address', models.CharField(max_length=100)),
                ('joined_domain', models.CharField(max_length=100)),
                ('connection_type', models.CharField(max_length=100)),
                ('pccurrentstatus', models.CharField(default='', editable=False, max_length=100)),
            ],
            options={
                'verbose_name': 'Laptop',
                'db_table': 'Laptop',
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.CharField(max_length=100)),
                ('employee_number', models.CharField(max_length=100)),
                ('asset_id', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('designation', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('date_start', models.CharField(max_length=100)),
                ('date_end', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Loan',
                'db_table': 'Loan',
            },
        ),
        migrations.CreateModel(
            name='loghistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.CharField(blank=True, max_length=100, null=True)),
                ('Username', models.CharField(blank=True, max_length=100, null=True)),
                ('Activity', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Log History',
                'db_table': 'loghistory',
            },
        ),
        migrations.CreateModel(
            name='NetworkHardware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hardware_id', models.CharField(max_length=100)),
                ('hardware_type', models.CharField(max_length=100)),
                ('Brand', models.CharField(max_length=100)),
                ('Current_Status', models.CharField(max_length=100)),
                ('Model', models.CharField(max_length=100)),
                ('serial_number', models.CharField(max_length=100)),
                ('asset_no', models.CharField(max_length=100)),
                ('dop', models.CharField(max_length=100)),
                ('dop_Warranty_end_date', models.CharField(max_length=100)),
                ('vendor', models.CharField(max_length=100)),
                ('mac_address', models.CharField(max_length=100)),
                ('ip_address', models.CharField(max_length=100)),
                ('block', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('po', models.CharField(max_length=100)),
                ('invoice', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Network Hardware',
                'db_table': 'Network Hardware',
            },
        ),
        migrations.CreateModel(
            name='softwareUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Software_Type', models.CharField(blank=True, max_length=100, null=True)),
                ('User_Type', models.CharField(blank=True, max_length=100, null=True)),
                ('Software_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('User_ID', models.CharField(blank=True, max_length=100, null=True)),
                ('Software_Version', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'software User',
                'db_table': 'software User',
            },
        ),
        migrations.CreateModel(
            name='UserAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('designation', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('block', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('vpn', models.CharField(max_length=100)),
                ('vpnaccount', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'User Asset',
                'db_table': 'UserAsset',
            },
        ),
    ]
