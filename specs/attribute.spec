{
    "model": {
        "rest_name": "attribute",
        "resource_name": "attributes",
        "entity_name": "Attribute",
        "package": "specifications",
        "extends": ["@parsable"],
        "description": "Represents an attribute of an object."
    },

    "attributes": {
        "name": {
            "description": "the name of the attribute",
            "type": "string",
            "unique": true
        },
        "allowedChars": {
            "description": "regexp representing what can be set. Only available for type string",
            "type": "string"
        },
        "allowedChoices": {
            "description": "Possible value that can be set. Only available for type enum",
            "type": "list"
        },
        "autogenerated": {
            "description": "Defines is the value will be autogenerated by the server if sent as null.",
            "type": "boolean"
        },
        "availability": {
            "description": "Defines what kind of roles can access the attribute.",
            "type": "list"
        },
        "channel": {
            "description": "Defines on what channel this attribute is sent.",
            "type": "string"
        },
        "creationOnly": {
            "description": "Defines is the attribute can only be set during the object creation.",
            "type": "boolean"
        },
        "defaultOrder": {
            "description": "Defines if the attribute is used when getting a list of objects as the default ordering key.",
            "type": "boolean"
        },
        "defaultValue": {
            "description": "Defines what will be the default value if sent as null.",
            "type": "string"
        },
        "deprecated": {
            "description": "Defines is the attribute is deprecated.",
            "type": "boolean"
        },
        "description": {
            "description": "description of the attribute. Will be used when generating documentation.",
            "type": "string"
        },
        "exposed": {
            "description": "Defines if this attribute is exposed or not through the api.",
            "type": "boolean"
        },
        "filterable": {
            "description": "Defines if this attribute can be used to do filtering.",
            "type": "boolean"
        },
        "format": {
            "allowed_choices": ["email", "phone", "ipv4", "ipv6", "date", "id", "free", "cidr"],
            "description": "Define what is the format of the attribute. Only available for type string",
            "type": "enum"
        },
        "maxLength": {
            "description": "Defines what is the max lenght for the attribute. Only available for type string",
            "type": "integer"
        },
        "maxValue": {
            "description": "Defines what is the max value for the attribute. Only available for type integer or float",
            "type": "integer"
        },
        "minLength": {
            "description": "Defines what is the min lenght for the attribute. Only available for type string",
            "type": "integer"
        },
        "minValue": {
            "description": "Defines what is the min value for the attribute. Only available for type int or float",
            "type": "integer"
        },
        "orderable": {
            "description": "Defines if the attribute can be used to do ordering.",
            "type": "boolean"
        },
        "readOnly": {
            "description": "Defines if the attribute is read only.",
            "type": "boolean"
        },
        "required": {
            "description": "Defines if the attribute is required.",
            "type": "boolean"
        },
        "subtype": {
            "description": "The sub type of the attribute. Not used by monolithe.",
            "type": "string"
        },
        "transient": {
            "description": "Defines if the attribute is transient.",
            "type": "boolean"
        },
        "type": {
            "allowed_choices": ["string", "boolean", "integer", "float", "list", "enum", "object", "time"],
            "default_value": "string",
            "description": "The type of the attribute.",
            "type": "enum"
        },
        "unique": {
            "default_value": "no",
            "description": "Defines if the attribute must be unique.",
            "type": "boolean"
        },
        "uniqueScope": {
            "allowed_choices": ["global", "local", "no"],
            "default_value": "no",
            "description": "Defines if how attribute must be unique.",
            "type": "enum"
        }
    }
}