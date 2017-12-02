import logging
from models.database import MemberInfo, MemberEquipment, MemberLicense
#import google.cloud.logging
#from google.cloud.logging.handlers import CloudLoggingHandler

class DBUtility:
    def __init__(self):
        ## Initialize logger
        #client = google.cloud.logging.Client()
        #handler = CloudLoggingHandler(client, name="member")
        handler = logging.StreamHandler()
        self.logger = logging.getLogger('cloudLogger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler) 

    def create_member_info(
        self, id_number, ch_name, en_name, birthday, nationality, tel_code, mobile_phone, email, postal_code, address,
        company, job_title, company_tel_code, emergency_contact_name, emergency_contact_phone, source, remarks, blood_type,
        left_eye, right_eye, height, weight):

        # print member_data
        added_entity = MemberInfo(
            id_number = id_number, ch_name = id_number, en_name = en_name, birthday = birthday, nationality = nationality, tel_code = tel_code, 
            mobile_phone = mobile_phone, email = email, postal_code = postal_code, address = address, company = company, job_title = job_title, 
            company_tel_code = company_tel_code, emergency_contact_name = emergency_contact_name, emergency_contact_phone = emergency_contact_phone, 
            source = source, remarks = remarks, blood_type = blood_type, left_eye = left_eye, right_eye = right_eye, height = height, weight = weight)

        added_entity.put()

    def create_member_eq(self, id_number, mirror, breathing_tube, jackets, gloves, overshoes, fins, bc, regulator, dive_computer, counterweight):

        added_entity = MemberEquipment(
            id_number = id_number, mirror = mirror, breathing_tube = breathing_tube, jackets = jackets, gloves = gloves, 
            overshoes = overshoes, fins = fins, bc = bc, regulator = regulator, dive_computer = dive_computer, counterweight = counterweight)
        
        added_entity.put()

    def create_member_license(self, id_number, license_type, deposit, payment, material, apply, get_license, status, tank_card=0):
        added_entity = MemberLicense(
            id_number = id_number, license_type = license_type, deposit = deposit, payment = payment, material = material, 
            apply = apply, get_license = get_license, status = status, tank_card = tank_card)

        added_entity.put()