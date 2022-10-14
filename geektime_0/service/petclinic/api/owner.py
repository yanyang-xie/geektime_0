from dataclasses import dataclass


@dataclass
class Owner:
    address: str = None
    city: str = None
    firstName: str = None
    lastName: str = None
    telephone: str = None
    id: int = None

    # def __init__(self, address city, firstName....):
    # {"firstName":"Betty","lastName":"Davis","address":"638 Cardinal Ave.","city":"Sun Prairie","telephone":"6085551749","id":2 }
    # **dict == __init__(**dict) == __init__(address=.., city=....)
    # asdict(dataclass)  => dict
