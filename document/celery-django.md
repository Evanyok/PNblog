1. create celery.py
    <p><code>

        from __future__ import absolute_import, unicode_literals
        import os
        from celery import Celery

        # set the default Django settings module for the 'celery' program.
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djserv.settings')

        app = Celery('djserv')

        # Using a string here means the worker doesn't have to serialize
        # the configuration object to child processes.
        # - namespace='CELERY' means all celery-related configuration keys
        #   should have a `CELERY_` prefix.
        app.config_from_object('django.conf:settings', namespace='CELERY')

        # Load task modules from all registered Django app configs.
        app.autodiscover_tasks()


        @app.task(bind=True)
        def debug_task(self):
            print('Request: {0!r}'.format(self.request))

    </code></p>

2. modify __init__.py
    <p><code>

        from __future__ import absolute_import, unicode_literals

        # This will make sure the app is always imported when
        # Django starts so that shared_task will use this app.
        from .celery import app as celery_app

        __all__ = ('celery_app',)

    </code></p>

3. add tasks.py
    <p><code>

        from __future__ import absolute_import, unicode_literals
        from celery import shared_task

        @shared_task
        def add(x, y):
            return x + y

        @shared_task
        def mul(x, y):
            return x * y

        @shared_task
        def xsum(numbers):
            return sum(numbers)

    </code></p>

4. modify settings.py
    <p><code>

        CELERY_ACCEPT_CONTENT = ['json']
        CELERY_TASK_SERIALIZER = 'json'
        CELERY_BROKER_URL = 'amqp://'
        CELERY_RESULT_BACKEND = 'redis://'

        INSTALLED_APPS = [
            ...
            'account',
            'django_celery_results',
        ]

    </code></p>

5. start up
    <p><code>

        $ celery -A myproject worker -l info
        or
        $ celery multi start w1 -A myproject -l info
        stop
        $ celery multi stop w1 -A myproject -l info
        restart
        $ celery multi restart w1 -A myproject -l info
    </code></p>

6. check
    <p><code>

        $ python manage.py shell
        [1] from myapp.tasks import *
        [2] res = add.delay(1,2)
        [3] res.get()

    </code></p>