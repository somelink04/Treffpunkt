from calendar import weekday

from .db_entities import *

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

def get_user (user_id):
    """
    :param user_id: ID of the searched User
    :return: The user_name of the searched user (User object) without password.
    """

    with Session() as session:
        user = session.query(User).filter(User.USER_ID == user_id).first()

        if user is None:
            result = None
        else:
            gender = None
            if user.USER_GENDER:
                gender = session.query(Gender).filter(Gender.GENDER_ID == user.USER_GENDER).first()

            region = None
            if user.USER_REGION:
                region = session.query(Region).filter(Region.REGION_ID == user.USER_REGION).first()
        result = {
            'USER_ID': user.USER_ID,
            'USER_FIRSTNAME': user.USER_FIRSTNAME,
            'USER_SURNAME': user.USER_SURNAME,
            'USER_BIRTHDATE': user.USER_BIRTHDATE,
            'USER_USERNAME': user.USER_USERNAME,
            'USER_EMAIL': user.USER_EMAIL,
            'USER_GENDER': user.USER_GENDER,
            'USER_REGION': user.USER_REGION,
            'GENDER_ID': gender.GENDER_ID if gender else None,
            'GENDER_NAME': gender.GENDER_NAME if gender else None,
            'REGION_ID': region.REGION_ID if region else None,
            'REGION_NAME': region.REGION_NAME if region else None,
            'REGION_ZIP': region.REGION_ZIP if region else None
        }
        return result


def get_all_users ():
    """
    :return: list of all users without password.
    """
    with Session() as session:
        # Fetch all users
        users = session.query(User).all()

        results = []
        for user in users:
            # Fetch related gender (if exists)
            gender = session.query(Gender).filter(
                Gender.GENDER_ID == user.USER_GENDER).first() if user.USER_GENDER else None

            # Fetch related region (if exists)
            region = session.query(Region).filter(
                Region.REGION_ID == user.USER_REGION).first() if user.USER_REGION else None

            # Assemble the result for each user
            user_data = {
                'USER_ID': user.USER_ID,
                'USER_FIRSTNAME': user.USER_FIRSTNAME,
                'USER_SURNAME': user.USER_SURNAME,
                'USER_BIRTHDATE': user.USER_BIRTHDATE,
                'USER_USERNAME': user.USER_USERNAME,
                'USER_EMAIL': user.USER_EMAIL,
                'USER_GENDER': user.USER_GENDER,
                'USER_REGION': user.USER_REGION,
                'GENDER_ID': gender.GENDER_ID if gender else None,
                'GENDER_NAME': gender.GENDER_NAME if gender else None,
                'REGION_ID': region.REGION_ID if region else None,
                'REGION_NAME': region.REGION_NAME if region else None,
                'REGION_ZIP': region.REGION_ZIP if region else None
            }
            results.append(user_data)

        return results


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

def get_region_id_from_zip(zip_code):
    """
    returns Region ID from zip code
    :param zip_code: Zip Code
    :return: Region ID
    """
    with Session() as session:
        region_id = session.query(Region).filter_by(REGION_ZIP=zip_code).first()
    return region_id.REGION_ID

def add_user_region (user_id, zip):
    """
    Updates Region of the user
    :param user_id:  ID of the User
    :param region_id: ID of the new Region
    """
    with Session() as session:
        user_region = session.query(User).filter_by(USER_ID=user_id).first()
        user_region.USER_REGION = get_region_id_from_zip(zip)
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

def add_event (time, region_id, category_id):
    """
    adds an event to the database.
    :param time: time of the event (datetime format)
    :param region: region of the event
    :param category: category of the event
    """
    with Session() as session:
        new_event = Event()
        new_event.EVENT_TIME = time
        new_event.EVENT_REGION = region_id
        new_event.EVENT_CATEGORY = category_id
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
        events = []

        # Step 1: Get all UserEvent records for the given user
        user_events = session.query(UserEvent).filter(UserEvent.USER_USER_EVENT_ID == user_id).all()

        # Step 2: Filter out those without USER_EVENT_ZUSAGE
        user_events = [ue for ue in user_events if ue.USER_EVENT_ZUSAGE]

        if user_events:
            enriched_events = []

            for user_event in user_events:
                event = session.query(Event).filter(Event.EVENT_ID == user_event.EVENT_USER_EVENT_ID).first()
                if not event:
                    continue

                # Fetch category
                category = session.query(Category).filter(
                    Category.CATEGORY_ID == event.EVENT_CATEGORY).first() if event.EVENT_CATEGORY else None

                # Fetch region
                region = session.query(Region).filter(
                    Region.REGION_ID == event.EVENT_REGION).first() if event.EVENT_REGION else None

                # Compose full enriched event
                enriched_event = {
                    'USER_USER_EVENT_ID': user_event.USER_USER_EVENT_ID,
                    'EVENT_USER_EVENT_ID': user_event.EVENT_USER_EVENT_ID,
                    'USER_EVENT_ZUSAGE': user_event.USER_EVENT_ZUSAGE,

                    'EVENT_ID': event.EVENT_ID,
                    'EVENT_TIME': event.EVENT_TIME,
                    'EVENT_REGION': event.EVENT_REGION,
                    'EVENT_CATEGORY': event.EVENT_CATEGORY,

                    'CATEGORY_ID': category.CATEGORY_ID if category else None,
                    'CATEGORY_NAME': category.CATEGORY_NAME if category else None,
                    'CATEGORY_DESCRIPTION': category.CATEGORY_DESCRIPTION if category else None,
                    'CATEGORY_MIN': category.CATEGORY_MIN if category else None,
                    'CATEGORY_ACCEPTION_RATIO': category.CATEGORY_ACCEPTION_RATIO if category else None,

                    'REGION_ID': region.REGION_ID if region else None,
                    'REGION_NAME': region.REGION_NAME if region else None,
                    'REGION_ZIP': region.REGION_ZIP if region else None
                }

                enriched_events.append(enriched_event)

            # You can return directly or pass to subquery_event
            events = subquery_event(events, session, enriched_events)
            return events
        else:
            return []


def get_unconfirmed_user_event(user_id):
    with Session() as session:
        events = []

        # Step 1: Get all UserEvent records for the given user
        user_events = session.query(UserEvent).filter(UserEvent.USER_USER_EVENT_ID == user_id).all()

        # Step 2: Filter out those without USER_EVENT_ZUSAGE
        user_events = [ue for ue in user_events if not ue.USER_EVENT_ZUSAGE]

        if user_events:
            enriched_events = []

            for user_event in user_events:
                event = session.query(Event).filter(Event.EVENT_ID == user_event.EVENT_USER_EVENT_ID).first()
                if not event:
                    continue

                # Fetch category
                category = session.query(Category).filter(
                    Category.CATEGORY_ID == event.EVENT_CATEGORY).first() if event.EVENT_CATEGORY else None

                # Fetch region
                region = session.query(Region).filter(
                    Region.REGION_ID == event.EVENT_REGION).first() if event.EVENT_REGION else None

                # Compose full enriched event
                enriched_event = {
                    'USER_USER_EVENT_ID': user_event.USER_USER_EVENT_ID,
                    'EVENT_USER_EVENT_ID': user_event.EVENT_USER_EVENT_ID,
                    'USER_EVENT_ZUSAGE': user_event.USER_EVENT_ZUSAGE,

                    'EVENT_ID': event.EVENT_ID,
                    'EVENT_TIME': event.EVENT_TIME,
                    'EVENT_REGION': event.EVENT_REGION,
                    'EVENT_CATEGORY': event.EVENT_CATEGORY,

                    'CATEGORY_ID': category.CATEGORY_ID if category else None,
                    'CATEGORY_NAME': category.CATEGORY_NAME if category else None,
                    'CATEGORY_DESCRIPTION': category.CATEGORY_DESCRIPTION if category else None,
                    'CATEGORY_MIN': category.CATEGORY_MIN if category else None,
                    'CATEGORY_ACCEPTION_RATIO': category.CATEGORY_ACCEPTION_RATIO if category else None,

                    'REGION_ID': region.REGION_ID if region else None,
                    'REGION_NAME': region.REGION_NAME if region else None,
                    'REGION_ZIP': region.REGION_ZIP if region else None
                }

                enriched_events.append(enriched_event)

            # You can return directly or pass to subquery_event
            events = subquery_event(events, session, enriched_events)
            return events
        else:
            return []


def get_all_user_events(user_id):
    """
    Get all from UserEvent table
    :param user_id: the ID of the User
    :return: All Events concerning this user
    """
    with Session() as session:
        events = []

        # Step 1: Fetch all UserEvent records for the given user_id
        user_events = session.query(UserEvent).filter(UserEvent.USER_USER_EVENT_ID == user_id).all()

        if user_events:
            enriched_events = []

            for user_event in user_events:
                # Step 2: Get associated Event for each UserEvent
                event = session.query(Event).filter(Event.EVENT_ID == user_event.EVENT_USER_EVENT_ID).first()
                if not event:
                    continue

                # Step 3: Merge relevant fields manually
                enriched_event = {
                    'USER_USER_EVENT_ID': user_event.USER_USER_EVENT_ID,
                    'EVENT_USER_EVENT_ID': user_event.EVENT_USER_EVENT_ID,
                    'USER_EVENT_ZUSAGE': user_event.USER_EVENT_ZUSAGE,

                    'EVENT_ID': event.EVENT_ID,
                    'EVENT_TIME': event.EVENT_TIME,
                    'EVENT_REGION': event.EVENT_REGION,
                    'EVENT_CATEGORY': event.EVENT_CATEGORY,
                }

                enriched_events.append(enriched_event)

            # Step 4: Call your processing function
            events = subquery_event(events, session, enriched_events)
            return events
        else:
            return []


def subquery_event(events, session, user_events):
    for user_event in user_events:
        event_id = user_event['EVENT_ID']
        event = session.query(Event).filter(Event.EVENT_ID == event_id).first()
        if not event:
            continue
        category = None
        if event.EVENT_CATEGORY:
            category = session.query(Category).filter(Category.CATEGORY_ID == event.EVENT_CATEGORY).first()
        region = None
        if event.EVENT_REGION:
            region = session.query(Region).filter(Region.REGION_ID == event.EVENT_REGION).first()
        event = {
            'EVENT_ID': event.EVENT_ID,
            'EVENT_TIME': event.EVENT_TIME,
            'EVENT_REGION': event.EVENT_REGION,
            'EVENT_CATEGORY': event.EVENT_CATEGORY,

            'CATEGORY_ID': category.CATEGORY_ID if category else None,
            'CATEGORY_NAME': category.CATEGORY_NAME if category else None,
            'CATEGORY_DESCRIPTION': category.CATEGORY_DESCRIPTION if category else None,
            'CATEGORY_MIN': category.CATEGORY_MIN if category else None,
            'CATEGORY_ACCEPTION_RATIO': category.CATEGORY_ACCEPTION_RATIO if category else None,

            'REGION_ID': region.REGION_ID if region else None,
            'REGION_NAME': region.REGION_NAME if region else None,
            'REGION_ZIP': region.REGION_ZIP if region else None
        }

        events.append(event)
    return events

def get_all_categories():
    with Session() as session:
        categories = session.query(Category).all()
        return [
            {
                "id": category.CATEGORY_ID,
                "name":category.CATEGORY_NAME,
                "description": category.CATEGORY_DESCRIPTION
            }
            for category in categories
        ]

def get_all_regions():
    with Session() as session:
        regions = session.query(Region).all()
        return [
            {
                "id": region.REGION_ID,
                "zip": region.REGION_ZIP,
                "name": region.REGION_NAME
            }
            for region in regions
        ]

def get_all_times():
    with Session() as session:
        hours = session.query(Hour).all()
        weekdays = session.query(Weekday).all()
        data = {
            "weekdays": [
                {"id": weekday.WEEKDAY_ID, "name": weekday.WEEKDAY_NAME}
                for weekday in weekdays
            ],
            "hours": [
                {"id": hour.HOUR_ID, "hour": hour.HOUR_NAME}
                for hour in hours
            ]
        }
        return data


#Get User Settings
def get_user_settings(user_id):
    """
    Get all settings for the matching
    :param user_id: ID of the User
    :return: Region of the User, Categories of the User, Times of the User (Weekday-Hour pair)
    """
    with Session() as session:
        # 1. Get the user and their region (no join)
        user = session.query(User).filter(User.USER_ID == user_id).first()
        region = None
        if user and user.USER_REGION:
            region = session.query(Region).filter(Region.REGION_ID == user.USER_REGION).first()

        user_region = {
            'USER_ID': user.USER_ID,
            'USER_REGION': user.USER_REGION,
            'REGION_ID': region.REGION_ID if region else None,
            'REGION_NAME': region.REGION_NAME if region else None,
            'REGION_ZIP': region.REGION_ZIP if region else None
        } if user else {}

        # 2. Get all UserCategory records, then fetch matching categories (no join)
        user_categories = session.query(UserCategory).filter(UserCategory.USER_USER_CATEGORY_ID == user_id).all()
        user_category = []
        for uc in user_categories:
            category = session.query(Category).filter(Category.CATEGORY_ID == uc.CATEGORY_USER_CATEGORY_ID).first()
            if category:
                user_category.append({
                    'USER_USER_CATEGORY_ID': uc.USER_USER_CATEGORY_ID,
                    'CATEGORY_USER_CATEGORY_ID': uc.CATEGORY_USER_CATEGORY_ID,
                    'CATEGORY_ID': category.CATEGORY_ID,
                    'CATEGORY_NAME': category.CATEGORY_NAME,
                    'CATEGORY_DESCRIPTION': category.CATEGORY_DESCRIPTION,
                    'CATEGORY_MIN': category.CATEGORY_MIN,
                    'CATEGORY_ACCEPTION_RATIO': category.CATEGORY_ACCEPTION_RATIO
                })

        # 3. Get all UserTime records and their Hour and Weekday separately (no join)
        user_times = session.query(UserTime).filter(UserTime.USER_USER_TIME_ID == user_id).all()
        user_time = []
        for ut in user_times:
            hour = session.query(Hour).filter(
                Hour.HOUR_ID == ut.HOUR_USER_TIME_ID).first() if ut.HOUR_USER_TIME_ID else None
            weekday = session.query(Weekday).filter(
                Weekday.WEEKDAY_ID == ut.WEEKDAY_USER_TIME_ID).first() if ut.WEEKDAY_USER_TIME_ID else None

            user_time.append({
                'USER_TIME_ID': ut.USER_TIME_ID,
                'HOUR_USER_TIME_ID': ut.HOUR_USER_TIME_ID,
                'WEEKDAY_USER_TIME_ID': ut.WEEKDAY_USER_TIME_ID,
                'USER_USER_TIME_ID': ut.USER_USER_TIME_ID,
                'HOUR_ID': hour.HOUR_ID if hour else None,
                'HOUR_NAME': hour.HOUR_NAME if hour else None,
                'WEEKDAY_ID': weekday.WEEKDAY_ID if weekday else None,
                'WEEKDAY_NAME': weekday.WEEKDAY_NAME if weekday else None
            })

        return user_region, user_category, user_time


#Getting Dict -> jsonify sollte damit besser klappen
def user_to_dict (user_object):
    """
    Transform a user object into a dictionary.
    :param user_object: User object to be transformed
    :return: transformed dictionary
    """
    return {
        "firstname": user_object.USER_FIRSTNAME,
        "surname": user_object.USER_SURNAME,
        "birthdate": user_object.USER_BIRTHDATE,
        "username": user_object.USER_USERNAME,
        "email": user_object.USER_EMAIL,
        "gender": user_object.GENDER_NAME,
        "zip:" : user_object.REGION_ZIP,
        "region": user_object.REGION_NAME,
        }

def region_to_dict(region_object):
    return {
        "id" : region_object.REGION_ID,
        "zip": region_object.REGION_ZIP,
        "name": region_object.REGION_NAME,
    }

def category_to_dict(category_object):
    return {
        "id": category_object.CATEGORY_ID,
        "name": category_object.CATEGORY_NAME,
        "description": category_object.CATEGORY_DESCRIPTION,
    }

def event_to_dict(event_object):
    return {
        "name": event_object.CATEGORY_NAME,
        "description": event_object.CATEGORY_DESCRIPTION,
        "time": event_object.EVENT_TIME,
        "eventzip": event_object.REGION_ZIP,
        "eventregion": event_object.REGION_NAME,
    }

def time_to_dict(time_object):
    return {
        "hour_id": time_object.HOUR_ID,
        "hour": time_object.HOUR,
        "weekday_ID": time_object.WEEKDAY_ID,
        "weekday": time_object.WEEKDAY,
    }
