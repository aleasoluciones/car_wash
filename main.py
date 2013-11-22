# -*- coding: utf-8 -*-
import factory
import car_wash


def main():
    service = factory.car_wash_service()

    car1 = car_wash.Car('555-XXX')
    car2 = car_wash.Car('666-YYY')
    customer1 = car_wash.Customer('Foo', mobile_phone='666')

    job1 = service.enter_in_the_car_wash(car1, customer1)
    job2 = service.enter_in_the_car_wash(car2, customer1)

    service.wash_completed(job1.service_id)
    service.wash_completed(job2.service_id)


if __name__ == '__main__':
    main()
