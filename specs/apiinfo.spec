{
    "model": {
        "rest_name": "apiinfo",
        "resource_name": "apiinfos",
        "entity_name": "APIInfo",
        "description": "Represents information about the entire specifications.",
        "extends": ["@parsable"],
        "package": "specifications"
    },

    "attributes": {
        "version": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "availability": null,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "description": "The version of the api",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": true,
            "read_only": false,
            "required": true,
            "transient": false,
            "type": "string",
            "unique": true
        },
        "prefix": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "availability": null,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": false,
            "description": "The prefix of the entire api.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": true,
            "transient": false,
            "type": "string",
            "unique": true
        },
        "root": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "availability": null,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": false,
            "description": "The object in the specification to consider as the root object.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": true,
            "transient": false,
            "type": "string",
            "unique": true
        }
    }
}