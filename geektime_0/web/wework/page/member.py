from dataclasses import dataclass


@dataclass
class Member:
    name: str = None
    account: str = None
    mail: str = None
    phone: int = None
