# -*- coding: utf-8 -*-

import collections

Car = collections.namedtuple('Car', ['plate'])
Customer = collections.namedtuple('Customer', ['name', 'mobile_phone'])


class CarWashJob(object):

    def __init__(self, car, customer):
        self._car = car
        self._customer = customer

    def has_customer(self, customer):
        return self._customer == customer

    @property
    def service_id(self):
        return '{car.plate}.{customer.mobile_phone}'.format(car=self._car, customer=self._customer)

    def __eq__(self, other):
        return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)

    def __ne__(self, other):
        return not self.__eq__(other)


class InMemoryJobRepository(object):

    def __init__(self):
        self._storage = {}

    def put(self, job):
        self._storage[job.service_id] = job

    def find_by_id(self, job_id):
        return self._storage.get(job_id)

    def find_by_customer(self, customer):
        return [job for job in self._storage.values() if job.has_customer(customer)]


class CarWashService(object):

    def __init__(self, notifier, repository):
        self.repository = repository
        self.notifier = notifier

    def enter_in_the_car_wash(self, car, customer):
        self.repository.put(CarWashJob(car, customer))

    def wash_completed(self, service_id):
        car_wash_job = self.repository.find_by_id(service_id)
        self.notifier.job_completed(car_wash_job)

    def services_by_customer(self, customer):
        return self.repository.find_by_customer(customer)
