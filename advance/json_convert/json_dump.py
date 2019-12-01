import json

from datetime import datetime
from decimal import Decimal
from functools import singledispatch

class MyClass:
    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

# 创建三个非内置类型的实例
mc = MyClass('i am class MyClass ')
dm = Decimal('11.11')
dt = datetime.now()
other = ""


@singledispatch
def convert(o):
    raise TypeError('can not convert type')

@convert.register(datetime)
def _(o):
    return o.strftime('%b %d %Y %H:%M:%S') 

@convert.register(Decimal)
def _(o):
    return float(o)

@convert.register(MyClass)
def _(o):
    return o.get_value()

class ExtendJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        try:
            return convert(obj)
        except TypeError:
            return super(ExtendJSONEncoder, self).default(obj)

data = {
    'mc': mc,
    'dm': dm,
    'dt': dt,
    'other': other,
}

b=json.dumps(data, cls=ExtendJSONEncoder)
print(b)
