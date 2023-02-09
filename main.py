from app import app 
from flask import Flask, request, jsonify
from models import OrderDetail, OrderStatus, Customer, Item, Payement
from config import db 

    #### Les methodes d'ajout, liste, 
###--------------Pour la class custumer---------------------------------
@app.route('/Customer/add', methods=['POST'])
def add_Customer():
    try:
        json = request.json
        name = json['name']
        deliveryAddress = json['deliveryAdress']
        resultat = jsonify('Add customer')
        return resultat
    except Exception as e:
        print(e)
        resultat = {"code_status": 404, "message": 'Erreur'}
        return jsonify(resultat)
    finally:
        db.session.rollback()
        db.session.close()
