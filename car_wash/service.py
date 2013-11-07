# -*- coding: utf-8 -*-

import uuid
from car_wash import CarWashJob

class CarWashService(object):

    def __init__(self, notifier):
        self.persistence = {}
        self.notifier = notifier

    def require_car_wash(self, car, customer):
        service_id = uuid.uuid4().hex
        self.persistence[service_id] = CarWashJob(car, customer)
        return service_id

    def wash_completed(self, service_id):
        car_wash_job = self.persistence[service_id]
        self.notifier.job_completed(car_wash_job)

    def services_by_customer(self, customer):
        return [job for job in self.persistence.values() if job.customer == customer]

