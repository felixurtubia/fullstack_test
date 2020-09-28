#!/usr/bin/env sh

./fullstack_test/walmart_discount_campaign/manage.py collectstatic --noinput
cd /fullstack_test/walmart_discount_campaign
uwsgi --http "0.0.0.0:${PORT}" --module walmart_discount_campaign.wsgi --master --processes 4 --threads 2