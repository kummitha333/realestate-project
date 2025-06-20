

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='area_sqft',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='mobilenumber',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
