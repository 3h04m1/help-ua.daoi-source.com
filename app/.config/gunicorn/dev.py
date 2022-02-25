command = "/home/site/help-ua.daoi-source.com/venv/bin/gunicorn"
pythonpath = "/home/site/help-ua.daoi-source.com/app/"
bind = "127.0.0.1:8002"
workers = 5
user = "site"
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = "DJANGO_SETTINGS_MODULE=core.settings"
# daemon = True