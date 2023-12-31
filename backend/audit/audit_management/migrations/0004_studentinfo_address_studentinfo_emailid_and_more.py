# Generated by Django 4.2.6 on 2023-10-15 22:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("audit_management", "0003_studentinfo_delete_basicinfo"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentinfo",
            name="address",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="studentinfo",
            name="emailId",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="studentinfo",
            name="fathersName",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="studentinfo",
            name="mothersName",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="studentinfo",
            name="phoneNo",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="studentinfo",
            name="rollNo",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="studentinfo",
            name="schoolHouse",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="studentinfo",
            name="section",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="studentinfo",
            name="studentAdmNum",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="studentinfo",
            name="age",
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name="studentinfo",
            name="dob",
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="studentinfo",
            name="name",
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name="studentinfo",
            name="studentClass",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
