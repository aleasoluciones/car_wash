# -*- coding: utf-8 -*-

import uuid
import collections

Car = collections.namedtuple('Car', ['plate'])
Customer = collections.namedtuple('Customer', ['name', 'mobile_phone'])
CarWashJob = collections.namedtuple('CarWashJob', ['car', 'customer'])


class InMemoryJobRepository(object):

    def __init__(self):
        self._storage = {}

    def put(self, job):
        job_id = uuid.uuid4().hex
        self._storage[job_id] = job
        return job_id

    def find_all(self):
        return self._storage.values()

    def find_by_id(self, job_id):
        return self._storage.get(job_id)


class CarWashService(object):

    def __init__(self, notifier, repository):
        self.repository = repository
        self.notifier = notifier

    def require_car_wash(self, car, customer):
        return self.repository.put(CarWashJob(car, customer))

    def wash_completed(self, service_id):
        car_wash_job = self.repository.find_by_id(service_id)
        self.notifier.job_completed(car_wash_job)

    def services_by_customer(self, customer):
        return [job for job in self.repository.find_all() if job.customer == customer]

