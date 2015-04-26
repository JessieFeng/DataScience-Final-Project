# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models, migrations

def load_data_business(apps, schema_editor):
    import json
    Business = apps.get_model("YelpAPI", "Business")
    for biz in open('yelp_academic_dataset_business.json'):
    	bline = json.loads(biz)
        _, created = Business.objects.get_or_create(
            Type = bline['type'].encode('utf-8'),
            business_id = bline['business_id'].encode('utf-8'),
            name = bline['name'].encode('utf-8'),
	    	city = bline['city'].encode('utf-8'),
	    	state = bline['state'].encode('utf-8'),
	    	stars = float(bline['stars']),
	    	review_count = int(bline['review_count']),
            )

class Migration(migrations.Migration):

    dependencies = [
        ('YelpAPI', '0002_auto_20150425_2203'),
    ]

    operations = [
    	migrations.RunPython(load_data_business),
    ]





