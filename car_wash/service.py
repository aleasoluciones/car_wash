# -*- coding: utf-8 -*-

import uuid
from car_wash import CarWashJob

class CarWashService(object):

    def __init__(self, sms_sender):
        self.persistence = {}
        self.sms_sender = sms_sender

    def require_car_wash(self, car, customer):
        service_id = uuid.uuid4().hex
        self.persistence[service_id] = CarWashJob(car, customer)
        return service_id

    def wash_completed(self, service_id):
        car_wash_job = self.persistence[service_id]
        self.sms_sender.send(mobile_phone=car_wash_job.customer.mobile_phone,
            text='Car %{car.plate} whased'.format(car=car_wash_job.car))

    def services_by_customer(self, customer):
        pass
