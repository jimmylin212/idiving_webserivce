from google.appengine.ext import ndb

class MemberInfo(ndb.Model):
    id_number = ndb.StringProperty(required=True)
    ch_name = ndb.StringProperty(required=False)
    en_name = ndb.StringProperty()
    birthday = ndb.DateProperty(required=False)
    nationality = ndb.StringProperty()
    tel_code = ndb.StringProperty()
    mobile_phone = ndb.StringProperty(required=False)
    email = ndb.StringProperty(required=False)
    postal_code = ndb.IntegerProperty(required=False)
    city = ndb.StringProperty(required=False)
    region = ndb.StringProperty(required=False)
    address = ndb.StringProperty(required=False)
    company = ndb.StringProperty()
    job_title = ndb.StringProperty()
    company_tel_code = ndb.StringProperty()
    emergency_contact_name = ndb.StringProperty(required=False)
    emergency_contact_phone = ndb.StringProperty(required=False)
    source = ndb.StringProperty()
    remarks = ndb.StringProperty()
    blood_type = ndb.StringProperty()
    left_eye = ndb.StringProperty()
    right_eye = ndb.StringProperty()
    height = ndb.FloatProperty()
    weight = ndb.FloatProperty()

class MemberEquipment(ndb.Model): 
    id_number = ndb.StringProperty(required=True)  
    mirror = ndb.BooleanProperty()
    breathing_tube = ndb.BooleanProperty()
    jackets = ndb.BooleanProperty()
    gloves = ndb.BooleanProperty()
    overshoes = ndb.BooleanProperty()
    fins = ndb.BooleanProperty()
    bc = ndb.BooleanProperty()
    regulator = ndb.BooleanProperty()
    dive_computer = ndb.BooleanProperty()
    counterweight = ndb.FloatProperty()

class MemberLicense(ndb.Model):
    id_number = ndb.StringProperty(required=True)
    license_type = ndb.StringProperty()
    deposit = ndb.DateProperty()
    payment = ndb.DateProperty()
    material = ndb.DateProperty()
    apply = ndb.DateProperty()
    license = ndb.DateProperty()
    status = ndb.StringProperty()
    tank_card = ndb.IntegerProperty()
    