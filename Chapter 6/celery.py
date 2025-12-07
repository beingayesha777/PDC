from celery import Celery

app = Celery('helloTask', broker='amqp://guest@localhost//')

@app.task
def hello():
    return "Hello World"

import celery

if __name__ == '__main__':
    result = celery.hello.delay()
