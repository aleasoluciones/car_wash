# -*- coding: utf-8 -*-

from mamba import *
from hamcrest import *
from doublex import *

from car_wash import service, car, customer

def create_car_wash_service(sms_sender):
    return service.CarWashService(sms_sender)


with describe('Car wash service') as _:

    with context('customer notification'):

        with describe('when service completed'):

            def it_notifies_the_customer():
                sms_sender = Spy()
                a_car = car.Car(plate='1234-XXX')
                a_customer = customer.Customer(name='Irrelevant name', mobile_phone='555555555')
                car_wash_service = create_car_wash_service(sms_sender)

                service_id = car_wash_service.require_car_wash(a_car, a_customer)
                car_wash_service.wash_completed(service_id)

                assert_that(sms_sender.send,
                    called().with_args(mobile_phone='555555555',
                        text=contains_string('1234-XXX')))

    with context('reporting'):

        with describe('when client report requested'):

            @pending
            def it_shows_all_wash_services_for_that_client():
                pass

        with describe('when a dailey report requested'):

            @pending
            def it_shows_today_wash_services():
                pass
