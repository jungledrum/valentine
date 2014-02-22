from mongoengine import (Document,
                         StringField,
                         DateTimeField)


class Products(Document):
    banner = StringField()
    name = StringField()
    price = StringField()
    images = StringField()
    category = StringField()
    sub_category = StringField()
    buy_url = StringField()
    desc = StringField()
    created_at = DateTimeField()
    updated_at = DateTimeField()
