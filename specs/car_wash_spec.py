# -*- coding: utf-8 -*-

from mamba import *
from hamcrest import *
from doublex import *

from car_wash import service, car, customer

def create_car_wash_service(sms_sender):
    return service.CarWashService(sms_sender)


car1 = car.Car(plate='123-XXX')
car2 = car.Car(plate='666-XXX')
car3 = car.Car(plate='777-XXX')
customer1 = customer.Customer(name='customer1', mobile_phone='123')
customer2 = customer.Customer(name='customer2', mobile_phone='666')
customer3 = customer.Customer(name='customer1', mobile_phone='777')

with describe('Car wash service') as _:

    @before.each
    def set_up():
        _.sms_sender = Spy()
        _.car_wash_service = create_car_wash_service(_.sms_sender)

    with context('customer notification'):

        with describe('when service completed'):

            def it_notifies_the_customer():
                service_id = _.car_wash_service.require_car_wash(car1, customer1)
                _.car_wash_service.wash_completed(service_id)

                assert_that(_.sms_sender.send,
                    called().with_args(mobile_phone='123', text=contains_string('123-XXX')))

    with context('reporting'):

        with describe('when client report requested'):

            @pending
            def it_shows_all_wash_services_for_that_client():
                pass

        with describe('when a dailey report requested'):

            @pending
            def it_shows_today_wash_services():
                pass
