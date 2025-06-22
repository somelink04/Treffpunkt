'''class User(Base):
    __tablename__ = "USER"
    USER_ID: Mapped[int] = mapped_column(primary_key=True)
    USER_FIRSTNAME: Mapped[str] = mapped_column(VARCHAR(50))
    USER_SURNAME: Mapped[str] = mapped_column(VARCHAR(50))
    USER_BIRTHDATE: Mapped[Optional[date]]
    USER_USERNAME: Mapped[str] = mapped_column(VARCHAR(50), unique=True)
    USER_EMAIL: Mapped[str] = mapped_column(VARCHAR(50), unique=True)
    USER_PASSWORD: Mapped[str] = mapped_column(TINYTEXT)
    USER_GENDER: Mapped[int] = mapped_column(ForeignKey("GENDER.GENDER_ID"))
    USER_REGION: Mapped[int] = mapped_column(ForeignKey("REGION.REGION_ID"))
#   USER_EVENT: brauchen wir noch.
#   USER_TIME:
#   USER_WEEKDAY: 

# Ich check noch nicht wie ich das richtigerweise in unserem Projekt einbinde. 
# Ich habs mit Region mal getestet und das klappt. 
# Das gleiche was ich für wochentag mach kann ich ja dann so weiter machen. Wir brauchen für jeden User aber zusätzlich noch die Events.1
'''

# Dummy-Userklasse
class User:
    def __init__(self, user_id, region, weekday):
        self.USER_ID = user_id
        self.USER_REGION = region
        self.USER_WEEKDAY = weekday


def matching(users: list[User]):
    matches = {}      
    unmatched = {}    # Nutzer ohne passenden Partner + Grund

    region_buckets = {}
    for user in users:
        region = user.USER_REGION
        if region not in region_buckets:
            region_buckets[region] = []
        region_buckets[region].append(user)

    for user in users:
        # REGION
        region = user.USER_REGION
        region_bucket = region_buckets[region]

        has_partner = False
        for other in region_bucket:
            if other.USER_ID != user.USER_ID:
                has_partner = True
                break

        if not has_partner:
            unmatched[user.USER_ID] = "Kein Match / PLZ"
            continue

        # WOCHENTAG
        weekday_bucket = []
        for other in region_bucket:
            if other.USER_WEEKDAY == user.USER_WEEKDAY:
                weekday_bucket.append(other)

        has_partner = False
        for other in weekday_bucket:
            if other.USER_ID != user.USER_ID:
                has_partner = True
                break

        if not has_partner:
            unmatched[user.USER_ID] = "Kein Match / Wochentag"
            continue

        matches[user.USER_ID] = [other.USER_ID for other in weekday_bucket if other.USER_ID != user.USER_ID]

    return matches, unmatched

'''
Einfach mal kopiert und nur die Werte ausgetauscht. So könnte es klappen.

        # EVENT
        event_bucket = []
        for other in weekday_bucket:
            if other.USER_EVENT == user.USER_EVENT:
                event_bucket.append(other)

        has_partner = False
        for other in event_bucket:
            if other.USER_ID != user.USER_ID:
                has_partner = True
                break

        if not has_partner:
            unmatched[user.USER_ID] = "Kein Match / Event"
            continue

        # UHRZEIT
        time_bucket = []
        for other in event_bucket:
            if other.USER_TIME == user.USER_TIME:
                time_bucket.append(other)

        has_partner = False
        for other in time_bucket:
            if other.USER_ID != user.USER_ID:
                has_partner = True
                break

        if not has_partner:
            unmatched[user.USER_ID] = "Kein Match / Uhrzeit"
            continue
'''






#Testing
def test_matching():
    users = [
        User(1, region=1, weekday="Montag"),
        User(2, region=1, weekday="Dienstag"),
        User(3, region=1, weekday="Montag"),
        User(4, region=2, weekday="Montag"),
    ]

    matches, unmatched = matching(users)

    print("Matches:", matches)
    print("Unmatched:", unmatched)

test_matching()