from __future__ import absolute_import, unicode_literals
from celery import shared_task
import zerorpc


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def findUsers():
    # mysql-rpc:9100
    client = zerorpc.Client()
    client.connect("tcp://127.0.0.1:9100")

    try:
        client.findUsers()
    except Exception as e:
        return '[ERR] %s' % e
