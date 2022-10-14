from dataclasses import dataclass, field


@dataclass
class CalendarModel:
    """
    提供业务的数据定义，因为会在多种地方序列化与反序列化，所以尽量与api拆开。
    如果不想做这么标准，也可以跟api进行合并，或者让api继承model
    """
    summary: str = None
    color: str = None
    shares: list[str] = field(default_factory=list)
    organizer: str = None
    cal_id: str = None
