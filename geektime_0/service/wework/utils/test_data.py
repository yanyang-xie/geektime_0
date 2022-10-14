from dataclasses import dataclass, field

from geektime_0.service.wework.utils.data import Data


@dataclass()
class A:
    a: int = None
    b: dict = None

@dataclass
class B:
    c: list[int]=field(default_factory=list)

def test_export_yaml():
    a={'a': 1, 'b': {'c': [3, 4]}}
    Data.export_yaml(a, '/tmp/1.yaml')
    b=Data.load_yaml('/tmp/1.yaml')
    assert a == b

    a=A()
    a.a=2
    a.b=B()
    a.b.c=[5, 6]
    Data.export_yaml(a, '/tmp/2.yaml')
    b2 = Data.load_yaml('/tmp/2.yaml')
    assert a == b2

    with open('/tmp/3.yaml', 'w') as f:
        f.write("""
!!python/object:geektime_0.service.wework.tests.test_data.A
a: 2
b: !!python/object:geektime_0.service.wework.tests.test_data.B
  c:
  - 5
  - 6
  """)

    b3 = Data.load_yaml('/tmp/3.yaml')
    assert a == b3



