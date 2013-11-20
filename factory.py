# -*- coding: utf-8 -*-

from car_wash import *


def in_memory_job_repository():
    return InMemoryJobRepository()

def file_job_repository():
    return FileJobRepository()

def console_log_notifier():
    return ConsoleJobNotifier()

def null_log_notifier():
    return NullJobNotifier()


def car_wash_service():
    return CarWashService(console_log_notifier(), file_job_repository())

