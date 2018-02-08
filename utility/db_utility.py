import logging, datetime
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
        self.member_info_properties = MemberInfo._properties
        self.member_eq_properties = MemberEquipment._properties
        self.member_license_properties = MemberLicense._properties
        self.member_lincense_types = ['owd', 'aa', 'ean', 'dd', 'nl', 'nv', 'sidemount', 'rrsr', 'bd', 'rec', 'fd', 'dry', 'pb', 'dc', 'itc', 'nightspi']

    ## Functions for MemberInfo
    def get_member_info(self, **kwargs):
        return MemberInfo.query(*(getattr(MemberInfo, k)==v for (k,v) in kwargs.items())).get()

    def upsert_member_info(self, member_info):
        target_entity = self.get_member_info(id_number = member_info['id_number'])

        if not target_entity:
            target_entity = MemberInfo()
        
        for each_property in self.member_info_properties:
            if (member_info[each_property]):
                setattr(target_entity, each_property, member_info[each_property])
        target_entity.put()

    ## Functions for MemberEquipment
    def get_member_eq(self, id_number):
        return MemberEquipment.query(MemberEquipment.id_number == id_number).get()

    def upsert_member_eq(self, member_eq):
        target_entity = self.get_member_eq(id_number = member_eq['id_number'])

        if not target_entity:
            target_entity = MemberEquipment()
        
        for each_property in self.member_eq_properties:
            if (member_eq[each_property]):
                setattr(target_entity, each_property, member_eq[each_property])
        target_entity.put()

    ## Functions for MemberLicense
    def get_member_license(self, id_number, license_type='all'):
        member_license_results = []

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

    def upsert_member_license(self, member_license):
        target_entity = self.get_member_license(id_number = member_license['id_number'], license_type = member_license['license_type'])

        if not target_entity:
            target_entity = MemberLicense()
        else:
            target_entity = target_entity[0]
        self.logger.info(member_license)
        for each_property in self.member_license_properties:
            if (each_property in member_license and member_license[each_property]):
                setattr(target_entity, each_property, member_license[each_property])
        target_entity.put()

