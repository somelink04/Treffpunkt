from datetime import date, datetime
from typing import List, Optional
from sqlalchemy import Integer, VARCHAR, CHAR, Float, ForeignKey, DATETIME
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
    USER_GENDER: Mapped[int] = mapped_column(ForeignKey("Gender.GENDER_ID"))
    USER_REGION: Mapped[int] = mapped_column(ForeignKey("Region.REGION_ID"))

class UserTime(Base):
    USER_TIME_ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    HOUR_USER_TIME_ID: Mapped[int] = mapped_column(ForeignKey("Hour.HOUR_ID"))
    WEEKDAY_USER_TIME_ID: Mapped[int] = mapped_column(ForeignKey("Weekday.WEEKDAY_ID"))
    USER_USER_TIME_ID: Mapped[int] = mapped_column(ForeignKey("User.USER_ID"))

class UserCategory(Base):
    USER_USER_CATEGORY_ID: Mapped[int] = mapped_column(ForeignKey("User.USER_ID"), primary_key=True)
    CATEGORY_USER_CATEGORY_ID: Mapped[int] = mapped_column(ForeignKey("Category.CATEGORY_ID"), primary_key=True)

class Event(Base):
    EVENT_ID: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    EVENT_TIME: Mapped[datetime] = mapped_column(DATETIME)
    EVENT_REGION: Mapped[int] = mapped_column(ForeignKey("Region.REGION_ID"))
    EVENT_CATEGORY: Mapped[int] = mapped_column(ForeignKey("Category.CATEGORY_ID"))

class UserEvent(Base):
    USER_USER_EVENT_ID: Mapped[int] = mapped_column(ForeignKey("User.USER_ID"), primary_key=True)
    EVENT_USER_EVENT_ID: Mapped[int] = mapped_column(ForeignKey("Event.EVENT_ID"), primary_key=True)
