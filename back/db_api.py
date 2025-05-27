from db_entities import *
from sqlalchemy import text

from db_entities import UserTime

#Create Session
engine = create_engine("mysql+pymysql://treffpunkt:b55tQKAc0z2K0hluWSo7Zxq2cMs9pTgx@localhost/TREFFPUNKT_DB")
Session = sessionmaker(bind=engine)


def add_user(firstname, surname, birthday, username, email, password, gender, region):
    """
    Add a new user to the database.
    :param firstname: First name of new user
    :param surname: Last name of new user
    :param birthday: Birthday of new user
    :param username: User name of new user
    :param email: email of new user
    :param password: password of new user (hashed)
    :param gender: ID of gender -> mapped table
    :param region: ID of region -> mapped table
    """
    with Session() as session:
        new_user = User()
        new_user.USER_FIRSTNAME = firstname
        new_user.USER_SURNAME = surname
        new_user.USER_BIRTHDATE = birthday
        new_user.USER_USERNAME = username
        new_user.USER_EMAIL = email
        new_user.USER_PASSWORD = password
        new_user.USER_GENDER = gender
        new_user.USER_REGION = region
        session.add(new_user)
        session.commit()

def delete_user_by_id(user_id):
    """
    Delete a user from the database.
    :param user_id: id of user to delete
    """
    with Session() as session:
        user = session.get(User, user_id)
        if user:
            session.delete(user)
            session.commit()
            print(f"Deleted user with ID {user_id}")
        else:
            print(f"No user found with ID {user_id}")


def get_all_user_auth ():
    """
    Gets all users auth data from the database.
    :return: List of all users with username and passwords (User object --> access with User.USER_USERNAME and User.USER_PASSWORD)
    """
    with Session() as session:
        user_auth = session.query(User).with_entities(User.USER_USERNAME, User.USER_PASSWORD).all()

    return user_auth

#Alternativ: Suche nach User über Username
def get_user_auth(user_name):
    """
    Gets one user auth data from the database.
    :return: The Password of the User if existent, None otherwise
    """
    with Session() as session:
        user_auth_one_user = session.query(User).with_entities(User.USER_PASSWORD).filter_by(USER_USERNAME=user_name).first()
        if user_auth_one_user:
            return user_auth_one_user.USER_PASSWORD
        else:
            print ("No User with this Username in DB.")
            return None

#--TODO: Brauchen wir hier noch was, was USER_GENDER, USER_REGION auflöst? Weil so bekommen wir vorraussichtlich 1, 39043 zurück
def get_user (user_id):
    """
    :param user_id: ID of the searched User
    :return: The user_name of the searched user (User object) without password.
    """
    with Session() as session:
        user = session.query(User).with_entities(User.USER_ID, User.USER_FIRSTNAME, User.USER_SURNAME,
                                                 User.USER_BIRTHDATE, User.USER_USERNAME, User.USER_EMAIL,
                                                 User.USER_GENDER, User.USER_REGION).filter_by(USER_ID=user_id).first()
        if user:
            return user
        else:
            print ("No User with this ID in DB.")
            return None

def get_all_users ():
    """
    :return: list of all users without password.
    """
    with Session() as session:
        user = session.query(User).with_entities(User.USER_ID, User.USER_FIRSTNAME, User.USER_SURNAME,
                                                 User.USER_BIRTHDATE, User.USER_USERNAME, User.USER_EMAIL,
                                                 User.USER_GENDER, User.USER_REGION).all()
        return user


#Write User Settings
def add_user_time (user_id, user_hour, user_weekday):
    """
    Sets new UserTime in UserTime Table (One Hour on One Weekday).
    ->Mapping Front (entering hour start-end for each weekday) to DB in Back
    :param user_id: ID of the User
    :param user_hours: ID of the hour
    :param weekday: ID of the weekday
    """
    with Session() as session:
        new_user_time = UserTime()
        new_user_time.USER_USER_TIME_ID = user_id
        new_user_time.HOUR_USER_TIME_ID = user_hour
        new_user_time.WEEKDAY_USER_TIME_ID = user_weekday
        session.add(new_user_time)
        session.commit()

def add_user_category (user_id, category_id):
    """
    Sets new UserCategory in UserCategory Table
    :param user_id: ID of the User
    :param category_id: ID of the Category
    """
    with Session() as session:
        new_user_category = UserCategory()
        new_user_category.USER_USER_CATEGORY_ID = user_id
        new_user_category.CATEGORY_USER_CATEGORY_ID = category_id
        session.add(new_user_category)
        session.commit()

def add_event (time, region, category):
    """
    adds an event to the database.
    :param time: time of the event (datetime format)
    :param region: region of the event
    :param category: category of the event
    """
    with Session() as session:
        new_event = Event()
        new_event.EVENT_TIME = time
        new_event.EVENT_REGION = region
        new_event.EVENT_CATEGORY = category
        session.add(new_event)
        session.commit()

#Depends on the matching algorithm, has to be changed possibly
def add_user_event(user_id, event_id):
    """
    Sets new UserEvent in UserEvent Table
    :param user_id: ID of the User
    :param event_id: ID of the Event
    """
    with Session() as session:
        new_user_event = UserEvent()
        new_user_event.EVENT_USER_EVENT_ID = event_id
        new_user_event.USER_USER_EVENT_ID = user_id
        new_user_event.USER_EVENT_ZUSAGE = False
        session.add(new_user_event)
        session.commit()

def add_confirm(user_event_id):
    """
    Sets UserEvent to confirmed
    :param user_event_id: ID of the Event
    """
    with Session() as session:
        user_event = session.query(UserEvent).filter_by(EVENT_USER_EVENT_ID=user_event_id).first()
        user_event.USER_EVENT_ZUSAGE = True
        session.commit()

def revoke_confirm(user_event_id):
    """
    Sets UserEvent to unconfirmed
    :param user_event_id: ID of the Event
    """
    with Session() as session:
        user_event = session.query(UserEvent).filter_by(EVENT_USER_EVENT_ID=user_event_id).first()
        user_event.USER_EVENT_ZUSAGE = False
        session.commit()

#Get Events
def get_confirmed_user_event(user_id):
    """
    Get only confirmed UserEvent from the database.
    :param user_id: ID of the User
    :return: Events the user confirmed to.
    """
    with Session() as session:
        user_events = session.query(UserEvent).filter_by(USER_USER_EVENT_ID = user_id).all()
        count = 0
        if len(user_events) > 0:
            for i in range (len(user_events)):
                if not user_events[count].USER_EVENT_ZUSAGE:
                    user_events.pop(i)
                else:
                    count += 1
            return user_events
        else:
            return []

def get_unconfirmed_user_event(user_id):

    with Session() as session:
        user_events = session.query(UserEvent).filter_by(USER_USER_EVENT_ID = user_id).all()
        count = 0
        if len(user_events) > 0:
            for i in range (len(user_events)):
                if user_events[count].USER_EVENT_ZUSAGE:
                    user_events.pop(i)
                else:
                    count += 1
            return user_events
        else:
            return []


def get_all_user_events(user_id):
    """
    Get all from UserEvent table
    :param user_id: the ID of the User
    :return: All Events concerning this user
    """
    with Session() as session:
        user_events = session.query(UserEvent).filter_by(USER_USER_EVENT_ID = user_id).all()
        return user_events

#Get User Settings
def get_user_settings(user_id):
    """
    Get all settings for the matching
    :param user_id: ID of the User
    :return: Region of the User, Cathegories of the User, Times of the User (Weekday-Hour pair)
    """
    with Session() as session:
        user_region = session.query(User).with_entities(User.USER_REGION).filter_by(USER_ID=user_id).first()
        user_category = session.query(UserCategory).filter_by(USER_USER_CATEGORY_ID=user_id).all()
        user_time = session.query(UserTime).filter_by(USER_USER_TIME_ID=user_id).all()
        return user_region, user_category, user_time


'''
für Test
def get_user_cat(user_id):
    with Session() as session:
        user_category = session.query(UserCategory).filter_by(USER_USER_CATEGORY_ID=user_id).all()
        return user_category

def get_user_time(user_id):
    with Session() as session:
        user_time = session.query(UserTime).filter_by(USER_USER_TIME_ID=user_id).all()
        return user_time
'''