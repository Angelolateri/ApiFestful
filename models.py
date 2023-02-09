from importlib.metadata import MetadataPathFinder
from msilib.sequence import tables
from multiprocessing import connection
from sqlite3 import Connection
from tkinter.tix import COLUMN
from config import db 
from datetime import datetime
import enum
from sqlalchemy import Enum



### creation de la table Order*
class Order(db.Model):
    createDate = db.Column(db.DateTime, primary_key = True, nullable = False, default = datetime.utcnow)
    
    def __repr__(self):
        return f"Todo {self.name}"

###creation de la table OrderStatus
class OrderStatus(enum.Enum):
    CREATE = 0
    SHIPPING = 1
    DELIVERED = 2
    PAID = 3

    t= tables('deta', MetadataPathFinder(), 
    COLUMN('value', Enum(OrderStatus))
    )

connection.execute(t.insert(), {"value": OrderStatus.PAID})
assert Connection.scalar(t.select()) is OrderStatus.PAID


###création de la table Customer
class Customer(db.Model):
    #id = db.Column(db.Integer, primary_key = True, nullable = False)
    name = db.Column(db.String(120), primary_key = True, nullable = False)
    deliveryAddress = db.Column(db.Integer, nullable = False)
    contact = db.Column(db.Integer, nullable = False)
    active = db.Column(db.Boolean, nullable = False)
    
###creation de la table OrderDetail
class OrderDetail(db.Model):
    qty = db.Column(db.Interger , primary_key = True, nullable = False)
    taxStatus = db.Column(db.String(120),nullable = False)

    ##### connetion OneTManny 
        ###pour calculateSubTotal
    calculateSubTotalId = db.Column(db.Integer, db.ForeignKey('OrderStatus.PAID'), nullable = True)
    calculateSubTotal = db.relationship('OrderStatus', foreign_keys = [calculateSubTotalId])

        ###pour calculateWeight
    calculateWeightId = db.Column(db.Integer, db.ForeignKey('OrderStatus.DELIVERED'), nullable = True)
    calculateWeight = db.relationship('OrderStatus', foreign_keys = [calculateWeightId])

####creation de la table Item
class Item(db.Model):
    weigth = db.Column(db.float , primary_key = True, nullable = False)
    description = db.Column(db.String(120),nullable = False)

    getPriceForQuantityQty = db.Column(db.Integer, db.ForeignKey('OrderDetail.qty'), nullable = True)
    getPriceForQuantity = db.relationship('Customer', foreign_keys = [getPriceForQuantityQty])

    getWeightA = db.Column(db.Integer, db.ForeignKey('OrderDetail.qty'), nullable = True)
    getWeight = db.relationship('Customer', foreign_keys = [getWeightA])

####creation de la table Payement 
##class Payement(db.Models):
##    amount = db.Column(db.Float , primary_key = True, nullable = False)