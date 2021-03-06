{
    "attributes": [
        {
            "description": "Defines if this attribute is exposed or not through the api.",
            "name": "exposed",
            "type": "boolean"
        },
        {
            "description": "Defines is the value will be autogenerated by the server if sent as null.",
            "name": "autogenerated",
            "type": "boolean"
        },
        {
            "description": "Defines what is the min value for the attribute. Only available for type int or float",
            "name": "minValue",
            "type": "integer"
        },
        {
            "description": "regexp representing what can be set. Only available for type string",
            "name": "allowedChars",
            "type": "string"
        },
        {
            "description": "Possible value that can be set. Only available for type enum",
            "name": "allowedChoices",
            "type": "list"
        },
        {
            "description": "Defines if the attribute is used when getting a list of objects as the default ordering key.",
            "name": "defaultOrder",
            "type": "boolean"
        },
        {
            "description": "Defines what kind of roles can access the attribute.",
            "name": "availability",
            "type": "list"
        },
        {
            "description": "Defines if this attribute can be used to do filtering.",
            "name": "filterable",
            "type": "boolean"
        },
        {
            "description": "Defines what will be the default value if sent as null.",
            "name": "defaultValue",
            "type": "string"
        },
        {
            "description": "Defines if the attribute can be used to do ordering.",
            "name": "orderable",
            "type": "boolean"
        },
        {
            "allowed_choices": [
                "string",
                "boolean",
                "integer",
                "float",
                "list",
                "enum",
                "object",
                "time"
            ],
            "default_value": "string",
            "description": "The type of the attribute.",
            "name": "type",
            "type": "enum"
        },
        {
            "description": "Defines is the attribute can only be set during the object creation.",
            "name": "creationOnly",
            "type": "boolean"
        },
        {
            "description": "Defines on what channel this attribute is sent.",
            "name": "channel",
            "type": "string"
        },
        {
            "description": "description of the attribute. Will be used when generating documentation.",
            "name": "description",
            "type": "string"
        },
        {
            "allowed_choices": [
                "email",
                "phone",
                "ipv4",
                "ipv6",
                "date",
                "id",
                "free",
                "cidr"
            ],
            "description": "Define what is the format of the attribute. Only available for type string",
            "name": "format",
            "type": "enum"
        },
        {
            "description": "Defines what is the min lenght for the attribute. Only available for type string",
            "name": "minLength",
            "type": "integer"
        },
        {
            "description": "Defines what is the max value for the attribute. Only available for type integer or float",
            "name": "maxValue",
            "type": "integer"
        },
        {
            "description": "Defines if the attribute is read only.",
            "name": "readOnly",
            "type": "boolean"
        },
        {
            "description": "Defines if the attribute is transient.",
            "name": "transient",
            "type": "boolean"
        },
        {
            "description": "Defines what is the max lenght for the attribute. Only available for type string",
            "name": "maxLength",
            "type": "integer"
        },
        {
            "default_value": "no",
            "description": "Defines if the attribute must be unique.",
            "name": "unique",
            "type": "boolean"
        },
        {
            "description": "the name of the attribute",
            "name": "name",
            "type": "string",
            "unique": true
        },
        {
            "description": "Defines is the attribute is deprecated.",
            "name": "deprecated",
            "type": "boolean"
        },
        {
            "description": "Defines if the attribute is required.",
            "name": "required",
            "type": "boolean"
        },
        {
            "allowed_choices": [
                "global",
                "local",
                "no"
            ],
            "default_value": "no",
            "description": "Defines if how attribute must be unique.",
            "name": "uniqueScope",
            "type": "enum"
        },
        {
            "description": "The sub type of the attribute. Not used by monolithe.",
            "name": "subtype",
            "type": "string"
        }
    ],
    "model": {
        "description": "Represents an attribute of an object.",
        "entity_name": "Attribute",
        "extends": [
            "@parsable"
        ],
        "package": "specifications",
        "resource_name": "attributes",
        "rest_name": "attribute"
    }
}
