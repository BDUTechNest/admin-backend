from django.db.models import Q

system_query = Q(content_type_id__in=[1, 2, 3, 4, 5, 6])
admin_query = Q(codename__endswith="admin")
authority_query = Q(codename__endswith="authority")
national_admin_query = Q(codename__endswith="nationaladmin")
divisional_admin_query = Q(codename__endswith="divisionaladmin")
national_authority_query = Q(codename__endswith="nationalauthority")
divisional_authority_query = Q(codename__endswith="divisionalauthority")


## national authority => exclude(system_query & national_authority_query)
## national admin => only include(divisional_admin_query)
# divisional admin => only include(district)
# divisional authority => exclude(system_query & national_authority_query & divisional_authority_query)
