from mongoengine import Document, StringField

class Register(Document):
    username = StringField()
    password = StringField()

class Bike(Document):
    Model = StringField()
    Daily_fee = StringField()
    Image = StringField()
    Year = StringField()
    text_description = StringField()