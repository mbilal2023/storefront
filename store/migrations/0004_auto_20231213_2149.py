# Generated by Django 5.0 on 2023-12-13 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection (title)
            VALUES ('collection1')
        """, """
            DELETE FROM store_collection
            WHERE title='collection1'
        """)
    ]
