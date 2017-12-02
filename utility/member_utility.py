import logging
from db_utility import DBUtility
#import google.cloud.logging
#from google.cloud.logging.handlers import CloudLoggingHandler

class MemberUtility:
    def __init__(self):
        self.license_types = ['owd', 'aa', 'ean', 'dd', 'nl', 'nv', 'sidemount', 'rrsr', 'bd', 'rec', 'fd', 'dry', 'pb', 'dc', 'itc', 'nightspi']
        self.license_entities = ['deposit', 'payment', 'material', 'apply', 'get_license', 'status']

        ## Initialize logger
        #client = google.cloud.logging.Client()
        #handler = CloudLoggingHandler(client, name="member")
        handler = logging.StreamHandler()
        self.logger = logging.getLogger('cloudLogger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)
    
    def create_member(self, request):
        db_utility = DBUtility()
        # member_data, member_eq_data, license_data = self.request2Dict(request)
        self.logger.info('Create member %s' % request.id_number)

        if (request.id_number == None):
            return 'error'

        ## create member info into database
        db_utility.create_member_info(
            id_number = request.id_number, ch_name = request.ch_name, en_name = request.en_name, birthday = request.birthday,
            nationality = request.nationality, tel_code = request.tel_code,  mobile_phone = request.mobile_phone, email = request.email,
            postal_code = request.postal_code, address = request.address, company = request.company, job_title = request.job_title,
            company_tel_code = request.company_tel_code, emergency_contact_name = request.emergency_contact_name, 
            emergency_contact_phone = request.emergency_contact_phone, source = request.source, remarks = request.remarks,
            blood_type = request.blood_type, left_eye = request.left_eye, right_eye = request.right_eye, height = request.height,
            weight = request.weight)

        ## create member equipment info into database
        db_utility.create_member_eq(
           id_number = request.id_number, mirror = request.mirror, breathing_tube = request.breathing_tube, jackets = request.jackets,
           gloves = request.gloves, overshoes = request.overshoes, fins = request.fins, bc = request.bc, regulator = request.regulator, 
           dive_computer = request.dive_computer, counterweight = request.counterweight)
        
        ## create member license data into data, only OWD has  tank card
        for license_type in self.license_types:
            if license_type == 'owd':
                db_utility.create_member_license(
                    id_number = request.id_number, license_type = license_type, deposit = request.get_assigned_value('%s_deposit' % (license_type)),
                    payment = request.get_assigned_value('%s_payment' % (license_type)), material = request.get_assigned_value('%s_material' % (license_type)),
                    apply = request.get_assigned_value('%s_apply' % (license_type)), get_license = request.get_assigned_value('%s_license' % (license_type)),
                    status = request.get_assigned_value('%s_status' % (license_type)), tank_card = request.get_assigned_value('%s_tank_card' % (license_type)))
            else:
                db_utility.create_member_license(
                    id_number = request.id_number, license_type = license_type, deposit = request.get_assigned_value('%s_deposit' % (license_type)),
                    payment = request.get_assigned_value('%s_payment' % (license_type)), material = request.get_assigned_value('%s_material' % (license_type)),
                    apply = request.get_assigned_value('%s_apply' % (license_type)), get_license = request.get_assigned_value('%s_license' % (license_type)),
                    status = request.get_assigned_value('%s_status' % (license_type)))

        return 'success'
        