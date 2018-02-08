import logging, json, datetime
from db_utility import DBUtility
#import google.cloud.logging
#from google.cloud.logging.handlers import CloudLoggingHandler

RETURN_SUCCESS = 'success'
RETURN_ERROR = 'error'

class MemberUtility:
    def __init__(self):
        ## Initialize logger
        #client = google.cloud.logging.Client()
        #handler = CloudLoggingHandler(client, name="member")
        handler = logging.StreamHandler()
        self.logger = logging.getLogger('cloudLogger')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(handler)
    
    def pre_process(self, request):
        db_utility = DBUtility()
        member_info = {}
        member_eq = {}
        member_licenses = []

        for each_property in db_utility.member_info_properties:
            if (request.get_assigned_value(each_property) and each_property == 'birthday'):
                member_info[each_property] = datetime.datetime.strptime(request.get_assigned_value(each_property), '%Y/%m/%d')
            elif (request.get_assigned_value(each_property) and (each_property == 'height' or each_property == 'weight')):
                member_info[each_property] = float(request.get_assigned_value(each_property))
            else:
                member_info[each_property] = request.get_assigned_value(each_property)
        
        for each_property in db_utility.member_eq_properties:
            if (each_property == 'id_number'):
                member_eq[each_property] = request.id_number
            elif (request.get_assigned_value(each_property) and each_property == 'counterweight'):
                member_eq[each_property] = float(request.get_assigned_value(each_property))
            else:
                if (request.get_assigned_value(each_property)):
                    member_eq[each_property] = True
                else:
                    member_eq[each_property] = False

        for license_type in db_utility.member_lincense_types:
            member_license = {}
            for each_property in db_utility.member_license_properties:
                if (each_property == 'license_type'):
                    member_license['license_type'] = license_type
                elif (each_property == 'id_number'):
                    member_license['id_number'] = request.id_number
                elif (each_property == 'tank_card'):
                    if (license_type == 'owd'):
                        if (request.get_assigned_value('%s_%s' % (license_type, each_property))):
                            member_license['tank_card'] = int(request.get_assigned_value('%s_%s' % (license_type, each_property)))
                else:
                    if (request.get_assigned_value('%s_%s' % (license_type, each_property))):
                        member_license[each_property] = datetime.datetime.strptime(
                            request.get_assigned_value('%s_%s' % (license_type, each_property)), '%Y/%m/%d')
                    else:
                        member_license[each_property] = None
                
            member_licenses.append(member_license)

        return member_info, member_eq, member_licenses

    def get_member(self, request):
        final_result = {}
        db_utility = DBUtility()
      
        if (request.id_number):
            self.logger.info('Get member %s' % request.id_number)
            member_info_result = db_utility.get_member_info(id_number = request.id_number)
            final_result.update(member_info_result.to_dict())
        elif (request.ch_name):
            self.logger.info('Get member %s' % request.ch_name)
            member_info_result = db_utility.get_member_info(ch_name = request.ch_name)
            final_result.update(member_info_result.to_dict())
        else:
            return RETURN_ERROR
        
        if member_info_result:
            request_id_number = final_result['id_number']

            member_eq_result = db_utility.get_member_eq(id_number = request_id_number)
            final_result.update(member_eq_result.to_dict())

            member_license_results = db_utility.get_member_license(id_number = request_id_number)
            for member_license_result in member_license_results:
                license_type = member_license_result.license_type
                final_result['%s_apply' % license_type] = member_license_result.apply
                final_result['%s_deposit' % license_type] = member_license_result.deposit
                final_result['%s_license' % license_type] = member_license_result.license
                final_result['%s_material' % license_type] = member_license_result.material
                final_result['%s_payment' % license_type] = member_license_result.payment
                final_result['%s_status' % license_type] = member_license_result.status
                if license_type == 'owd':
                    final_result['%s_tank_card' % license_type] = member_license_result.tank_card

        return RETURN_SUCCESS, json.dumps(final_result, ensure_ascii=True)

    def create_member(self, request):
        db_utility = DBUtility()
        # member_data, member_eq_data, license_data = self.request2Dict(request)
        self.logger.info('Create member %s' % request.id_number)

        if (request.id_number == None):
            return RETURN_ERROR

        ## get the key value of each member data
        member_info, member_eq, member_licenses = self.pre_process(request)

        ## create member info into database
        db_utility.upsert_member_info(member_info)

        ## create member equipment info into database
        db_utility.upsert_member_eq(member_eq)

        ## create member license data into data, only OWD has tank card
        for member_license in member_licenses:
            db_utility.upsert_member_license(member_license)

        return RETURN_SUCCESS

    def patch_member(self, request):
        db_utility = DBUtility()
        self.logger.info('Patch member %s' % request.id_number)

        if (request.id_number == None):
            return RETURN_ERROR

        target_member_info = db_utility.get_member_info(id_number = request.id_number)

        if (target_member_info):
            db_utility.upsert_member_info(request)
            db_utility.upsert_member_eq(request)
            db_utility.upsert_member_license(request)

        else:
            return RETURN_ERROR

        return RETURN_SUCCESS
        