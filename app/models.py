from datetime import datetime

from enum import Enum
from pydantic import BaseModel


class Gender(str, Enum):
    male = "male"
    female = "female"


class UserStatus(str, Enum):
    active = "active"
    deleted = "deleted"
    blocked = "blocked"


class OrderStatus(str, Enum):
    order = "order"
    buy = "buy"


class Token(BaseModel):
    authorization: str


class UserToken(BaseModel):
    id: int
    username: str
    email: str | None
    password: str
    gender: Gender

    class Config:
        orm_mode = True


class ItemBase(BaseModel):
    name: str
    format: str
    price: float = 0


class SimpleItem(BaseModel):
    id: int
    name: str
    created_at: datetime
    price: float
    upload: str

    class Config:
        orm_mode = True


class ItemHistory(BaseModel):
    histories: list[SimpleItem]

    class Config:
        orm_mode = True


class Item(ItemBase):
    id: int
    author: int
    upload: str

    class Config:
        orm_mode = True


class ExhibitionItem(BaseModel):
    id: int
    name: str
    author: str
    upload: str

    class Config:
        orm_mode = True


class ItemURL(BaseModel):
    url: str

    class Config:
        orm_mode = True


class UserRegister(BaseModel):
    email: str | None
    username: str
    password: str
    nickname: str
    gender: Gender


class UserLogin(BaseModel):
    username: str
    password: str


class UserBase(BaseModel):
    status: UserStatus
    email: str | None
    username: str
    password: str
    gender: Gender


class Inventory(BaseModel):
    id: int
    upload: str

    class Config:
        orm_mode = True


class InventoriesBase(BaseModel):
    inventories: list[Inventory]

    class Config:
        orm_mode = True


class Profile(BaseModel):
    id: int
    user: int
    nickname: str
    money: float

    class Config:
        orm_mode = True


class TradeRegister(BaseModel):
    item: int
    orderPrice: float
    immediatePrice: float


class ExhibitionInventory(BaseModel):
    item: SimpleItem
    expire: datetime

    class Config:
        orm_mode = True


class ExhibitionInventories(BaseModel):
    exhibitionInventories: list[ExhibitionInventory]

    class Config:
        orm_mode = True


class Trade(BaseModel):
    id: int
    owner: int
    item: int
    expire: datetime
    immediate_price: float
    is_sell: bool

    class Config:
        orm_mode = True


class ExhibitionTrade(BaseModel):
    id: int
    owner: str
    item: int
    expire: datetime
    immediate_price: float
    is_sell: bool

    class Config:
        orm_mode = True


class OrderRegister(BaseModel):
    item: int
    trade: int
    status: OrderStatus = "buy"


class Order(BaseModel):
    buyer: int
    item: int
    price: float
    trade: int
    status: OrderStatus

    class Config:
        orm_mode = True


class Attendance(BaseModel):
    profile: int
    attendanceDate: datetime
    status: bool = True

    class Config:
        orm_mode = True


class Exhibition(BaseModel):
    item: ExhibitionItem
    trade: ExhibitionTrade | None
    hall: int
    num: int
    max_width: int
    max_height: int

    class Config:
        orm_mode = True


class ExhibitionRegister(BaseModel):
    item: int
    hall: int
    num: int
    order_price: float | None
    immediate_price: float


class ExhibitionImage(BaseModel):
    hall: int
    num: int
