# -*- coding: utf-8 -*-

from mamba import *
from hamcrest import *
from doublex import *

from car_wash import service
from car_wash import CarWashJob, Car, Customer

def create_car_wash_service(notifier, repository):
    return service.CarWashService(notifier, repository)


car1 = Car(plate='123-XXX')
car2 = Car(plate='666-XXX')
car3 = Car(plate='777-XXX')
customer1 = Customer(name='customer1', mobile_phone='123')
customer2 = Customer(name='customer2', mobile_phone='666')
customer3 = Customer(name='customer1', mobile_phone='777')

with describe('Car wash service') as _:

    @before.each
    def set_up():
        _.notifier = Spy()
        _.car_wash_service = create_car_wash_service(_.notifier, service.InMemoryJobRepository())

    with context('customer notification'):

        with describe('when service completed'):

            def it_notifies_the_customer():
                service_id = _.car_wash_service.require_car_wash(car1, customer1)
                _.car_wash_service.wash_completed(service_id)

                assert_that(_.notifier.job_completed,
                    called().with_args(CarWashJob(car1, customer1)))

    with context('reporting'):

        with describe('when client report requested'):

            def it_shows_all_wash_services_for_that_customer():
                _.car_wash_service.require_car_wash(car1, customer2)
                _.car_wash_service.require_car_wash(car1, customer1)
                _.car_wash_service.require_car_wash(car2, customer1)
                _.car_wash_service.require_car_wash(car3, customer1)
                _.car_wash_service.require_car_wash(car1, customer2)

                services = _.car_wash_service.services_by_customer(customer1)

                assert_that(services, has_items(CarWashJob(car1, customer1),
                                                CarWashJob(car2, customer1),
                                                CarWashJob(car3, customer1),))
                assert_that(services, not(has_item(CarWashJob(car1, customer2))))

