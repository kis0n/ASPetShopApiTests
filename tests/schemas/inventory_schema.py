from unicodedata import category

INVENTORY_SCHEMA = {
    "type": "object",
    "properties": {
        "approved": {
            "type": "integer"
        },
        "placed": {
            "type": "integer"
        },
        "delivered": {
            "type": "integer"
        },
    },
    "additionalProperties": False
}