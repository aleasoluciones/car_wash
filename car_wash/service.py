# -*- coding: utf-8 -*-

import uuid


class CarWashService(object):

    def __init__(self, sms_sender):
        self.persistence = {}
        self.sms_sender = sms_sender

    def require_car_wash(self, car, customer):
        service_id = uuid.uuid4().hex
        self.persistence[service_id] = (car, customer)
        return service_id

    def wash_completed(self, service_id):
        car, customer = self.persistence[service_id]
        self.sms_sender.send(mobile_phone=customer.mobile_phone,
            text='Car %{car.plate} whased'.format(car=car))
