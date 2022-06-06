# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 11:30:24 2022

@author: cvskf
"""

import json
import jsonschema
import os

from jsonschema import RefResolver, Draft7Validator


schema_fp=os.path.join(os.pardir,'schema_files')

schema_store={}
for file in os.listdir(schema_fp):
    print(file)
    if file.endswith('schema.json'):
        with open(os.path.join(schema_fp,file)) as f:
            schema=json.load(f)
            
        Draft7Validator.check_schema(schema)
            
        schema_store[schema['$id']]=schema

#print(list(schema_store))


schema=schema_store['https://github.com/stevenkfirth/csvw_metadata_json_schema/blob/main/schema_files/dialect_description.schema.json']
resolver = RefResolver.from_schema(
    schema=schema,
    store=schema_store
    )
validator = Draft7Validator(schema, resolver=resolver, format_checker=None)


data={'@context':'http://www.w3.org/ns/csvw',
      'headerRowCount':0}
validator.validate(data)


