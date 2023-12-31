# Generated by Django 4.2.5 on 2023-11-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parts_of_computer_app', '0004_alter_casefanfeature_product_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coolerfeature',
            name='cooling_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='casefanfeature',
            name='cooling_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='casefanfeature',
            name='fan_Count',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='casefanfeature',
            name='led_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='casefanfeature',
            name='power_Connector',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='casefanfeature',
            name='rpm',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='computercasefeature',
            name='PSU',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='computercasefeature',
            name='PSU_Location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='computercasefeature',
            name='case_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='computercasefeature',
            name='transparent_Case',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='computercasefeature',
            name='type_C',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coolerfeature',
            name='compatible_Sockets',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coolerfeature',
            name='fan_Count',
            field=models.IntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='coolerfeature',
            name='led',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coolerfeature',
            name='radiator_Size',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='graphicscardfeature',
            name='gpu_Manufacturer',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='graphicscardfeature',
            name='gpu_Memory_Capacity',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='graphicscardfeature',
            name='gpu_Model',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='graphicscardfeature',
            name='memory_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='keyboardfeature',
            name='connection_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='keyboardfeature',
            name='keyboard_Layout',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='keyboardfeature',
            name='mechanical',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='keyboardfeature',
            name='numpad',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='keyboardfeature',
            name='wrist_Support',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='monitorfeature',
            name='panel_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='monitorfeature',
            name='refresh_Rate',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='monitorfeature',
            name='resolution',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='monitorfeature',
            name='response_Time',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='monitorfeature',
            name='screen_Size',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='motherboardfeature',
            name='compatible_Processors',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='motherboardfeature',
            name='motherboard_Size',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='motherboardfeature',
            name='processor_Socket_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='motherboardfeature',
            name='ram_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mousefeature',
            name='button_Count',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mousefeature',
            name='connection_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mousefeature',
            name='max_DPI',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mousefeature',
            name='tracking_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='mousefeature',
            name='usage_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='processorfeature',
            name='core_Count',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='processorfeature',
            name='processor_Manufacturer',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='processorfeature',
            name='processor_Model',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='processorfeature',
            name='processor_Series',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='processorfeature',
            name='processor_Socket_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ramfeature',
            name='channel_Type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ramfeature',
            name='ram_Capacity',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ramfeature',
            name='ram_Compatibility',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ramfeature',
            name='ram_Frequency',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ramfeature',
            name='ram_Type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
