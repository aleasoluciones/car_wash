# -*- coding: utf-8 -*-

import collections

Car = collections.namedtuple('Car', ['plate'])
Customer = collections.namedtuple('Customer', ['name', 'mobile_phone'])
CarWashJob = collections.namedtuple('CarWashJob', ['car', 'customer'])
