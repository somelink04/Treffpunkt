from datetime import date
from typing import List, Optional
from sqlalchemy import Integer, String, VARCHAR, CHAR, Float, DATE
from sqlalchemy.dialects.mysql import TINYTEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Gender(Base):
    __tablename__ = 'GENDER'
    GENDER_ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    GENDER_NAME: Mapped[str] = mapped_column(VARCHAR(8))

class Hour(Base):
    __tablename__ = 'HOUR'
    HOUR_ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    HOUR_NAME: Mapped[str] = mapped_column(VARCHAR(10))

class Weekday(Base):
    __tablename__ = 'WEEKDAY'
    WEEKDAY_ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    WEEKDAY_NAME: Mapped[str] = mapped_column(VARCHAR(10))

class Region(Base):
    __tablename__ = 'REGION'
    REGION_ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    REGION_NAME: Mapped[str] = mapped_column(VARCHAR(50))
    REGION_ZIP: Mapped[str] = mapped_column(CHAR(5))

class Category(Base):
    __tablename__ = 'CATEGORY'
    CATEGORY_ID: Mapped[int] = mapped_column(Integer, primary_key=True)
    CATEGORY_NAME: Mapped[str] = mapped_column(VARCHAR(50))
    CATEGORY_DESCRIPTION: Mapped[str] = mapped_column(TINYTEXT)
    CATEGORY_ACCEPTION_RATIO: Mapped[float] = mapped_column(Float)
    CATEGORY_MIN: Mapped[Optional[int]]

class User(Base):
    __tablename__ = "USER"
    USER_ID: Mapped[int] = mapped_column(primary_key=True)
    USER_FIRSTNAME: Mapped[str] = mapped_column(VARCHAR(50))
    USER_SURNAME: Mapped[str] = mapped_column(VARCHAR(50))
    USER_BIRTHDATE: Mapped[Optional[date]]
    USER_USERNAME: Mapped[str] = mapped_column(VARCHAR(50), unique=True)
    USER_EMAIL: Mapped[str] = mapped_column(VARCHAR(50), unique=True)
    USER_PASSWORD: Mapped[str] = mapped_column(TINYTEXT)
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(back_populates="user")
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))
    user: Mapped[User] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"