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

    ## Functions for MemberInfo
    def get_member_info(self, **kwargs):
        return MemberInfo.query(*(getattr(MemberInfo, k)==v for (k,v) in kwargs.items())).get()

    def upsert_member_info(self, request):
        properties = MemberInfo._properties

        target_entity = self.get_member_info(id_number = request.id_number)

        if target_entity:
            ## Update if find the same id_number in db
            for each_property in properties:
                updated_value = request.get_assigned_value(each_property)
                if updated_value:
                    setattr(target_entity, each_property, updated_value)
            target_entity.put()
        else:
            ## Insert new record if doesn't find in db
            added_entity = MemberInfo()
            for each_property in properties:
                setattr(added_entity, each_property, request.get_assigned_value(each_property))
            added_entity.put()

    ## Functions for MemberEquipment
    def get_member_eq(self, id_number):
        return MemberEquipment.query(MemberEquipment.id_number == id_number).get()

    def upsert_member_eq(self, request):
        properties = MemberEquipment._properties

        target_entity = self.get_member_eq(id_number = request.id_number)

        if target_entity:
            ## Update if find the same id_number in db
            for each_property in properties:
                updated_value = request.get_assigned_value(each_property)
                if updated_value:
                    setattr(target_entity, each_property, updated_value)
            target_entity.put()
        else:
            ## Insert new record if doesn't find in db
            added_entity = MemberEquipment()
            for each_property in properties:
                setattr(added_entity, each_property, request.get_assigned_value(each_property))
            added_entity.put()

    ## Functions for MemberLicense
    def get_member_license(self, id_number, license_type='all'):
        member_license_results = []
        license_types = ['owd', 'aa', 'ean', 'dd', 'nl', 'nv', 'sidemount', 'rrsr', 'bd', 'rec', 'fd', 'dry', 'pb', 'dc', 'itc', 'nightspi']

        if (license_type == 'all'):
            for license_type in license_types:
                query_result = MemberLicense.query(MemberLicense.id_number == id_number, MemberLicense.license_type == license_type).get()
                if query_result:
                    member_license_results.append(query_result)
        else:
            query_result = MemberLicense.query(MemberLicense.id_number == id_number, MemberLicense.license_type == license_type).get()
            if query_result:
                member_license_results.append(query_result)

        return member_license_results

    def upsert_member_license(self, request):
        ## The license_types cloud be replaced once the course data is in database
        license_types = ['owd', 'aa', 'ean', 'dd', 'nl', 'nv', 'sidemount', 'rrsr', 'bd', 'rec', 'fd', 'dry', 'pb', 'dc', 'itc', 'nightspi']
        properties = MemberLicense._properties

        for license_type in license_types:
            target_entity = self.get_member_license(id_number = request.id_number, license_type = license_type)

            if target_entity and target_entity[0]:
                target_entity = target_entity[0]
                ## Update if find the same id_number in db
                for each_property in properties:
                    if each_property != 'id_number' and each_property != 'license_type':
                        if each_property == 'tank_card' and license_type != 'owd':
                            continue

                        updated_value = request.get_assigned_value('%s_%s' % (license_type, each_property))
                        if updated_value:
                            setattr(target_entity, each_property, updated_value)

                target_entity.put()
            else:
                ## Insert new record if doesn't find in db
                added_entity = MemberLicense()
                for each_property in properties:
                    if each_property == 'id_number':
                        setattr(added_entity, each_property, request.id_number)
                    elif each_property == 'license_type':
                        setattr(added_entity, each_property, license_type)
                    elif each_property == 'tank_card':
                        if license_type == 'owd':
                            setattr(added_entity, each_property, request.get_assigned_value('%s_%s' % (license_type, each_property)))    
                    else:
                        setattr(added_entity, each_property, request.get_assigned_value('%s_%s' % (license_type, each_property)))
                added_entity.put()