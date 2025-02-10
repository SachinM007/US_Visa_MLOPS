import sys

from us_visa.logger import logging
from us_visa.exception import USvisaException

try:
    2/0
except Exception as e:
    raise USvisaException(e, sys)  #sys package helps it identify wehre the error occured
