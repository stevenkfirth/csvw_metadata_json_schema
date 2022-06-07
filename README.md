# csvw_metadata_json_schema

**JSON schema for the Metadata Vocabulary for Tabular Data (CSVW)**

This repository contains JSON Schema files for the W3C Recommendation *Metadata Vocabulary for Tabular Data*.

The Metadata Vocabulary for Tabular Data recommendation defines the structure of the JSON files that are used by *CSV on the Web* (CSVW) to hold the metadata for CSV files.

Although the recommendation states that CSVW metadata files must be JSON, it doesn't define a JSON Schema for the metafiles. 

This work aims to fill this gap by creating a series of JSON Schema files which can be used for creating and validating CSVW metadata file. 

> Note: Not all the rules contained in the W3C Recommendation can be expressed in JSON Schema. Therefore validating csvw metafiles using the JSON Schema files here can only be considered as a partial validation and dows not mean that the csvw metafiles are fully commpliant with the W3C Recommendation.

## Folder Descriptions

- *schema_files* - contains the JSON schema files for the CSVW standard.
- *tests* - contains Python code to test the validity of the schema files. 

## References:

- Metadata Vocabulary for Tabular Data: https://www.w3.org/TR/tabular-metadata/
- CSVW: https://www.w3.org/TR/tabular-data-primer/
- JSON Schema vocabulary: https://json-schema.org/
- jsonschema Python package: https://python-jsonschema.readthedocs.io/en/stable/







