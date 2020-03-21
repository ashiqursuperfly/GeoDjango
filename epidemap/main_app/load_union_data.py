import os
from django.contrib.gis.utils import LayerMapping
from .models import BdUnions

'''
bd_union_data/* is gitignored since, its too big. But can be downloaded from: https://geodash.gov.bd/layers/
'''

# Inspect a shapeFile: python manage.py ogrinspect main_app/bd_districts_data/Bangladesh_District.shp BdDistricts --srid=4326 --mapping --multi

bdunions_mapping = {
    'div_id': 'Div_ID',
    'dist_id': 'Dist_ID',
    'upz_id': 'Upz_ID',
    'un_id': 'Un_ID',
    'un_uid': 'Un_UID',
    'divi_name': 'Divi_name',
    'dist_name': 'Dist_name',
    'upaz_name': 'Upaz_name',
    'uni_name': 'Uni_name',
    'area_sqkm': 'Area_SqKm',
    'geom': 'MULTIPOLYGON',
}

shp_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'bd_union_data/union_map.shp'))

def load(verbose=True):
    lm = LayerMapping(BdUnions, shp_file, bdunions_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True,verbose=verbose)