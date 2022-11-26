# coding: utf-8

import requests


def enumirate(N: int = 1000):
  for x in range(N):
    print(f'Now x is {x}')
    x += 1

enumirate(103)