#!/usr/bin/env python

from celery import task

@task
def foo_task():
    print "Hello"

try:
    foo_task.delay()
except Exception, e:
    print "Expected to get that exception: %s" % e

print "Now I'm going to lock up..."

foo_task.delay()
