#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:09:05 2022

@author: Noe Gebert/Onill Pydannah/SHAYAN sHAKUN
"""
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/enregdestination')
def enregdestination():

    result = request.form 
    nom = ['nom']
    continent = ['continent']
    temps_moyen = ['temps_moyen']
    note_des_voyageurs = ['note_des_voyageurs']


    if nom != '' and continent != '' and temps_moyen != '' and note_des_voyageurs != '':
        
        conn = sqlite3.connect('../bdd/BDD_Agence.db') # connection à la BDD
        cur = conn.cursor()

        cur.execute("INSERT INTO destinations (nom,continent,temps_moyenne,note_voyageurs VALUES (?,?,?,?))"(nom,continent,temps_moyen,note_des_voyageurs))

        return render_template("enregdestination.html")


    else :
        #revenir à la page réservation
        return render_template('enregdestination.html', message='formulaire non valide')



    


@app.route('/enregvol')
def enregvol():
    return render_template("enregvol.html")


@app.route('/enregclient')
def enregclient():
    return render_template("enregclient.html")


@app.route('/enreglogement')
def enreglogement():
    return render_template("enreglogement.html")


@app.route('/verifdispovol')
def verifdispovol():
    return render_template("verifdispovol.html")


@app.route('/verifdispologement')
def verifdispologement():
    return render_template("verifdispologement.html")


@app.route('/reservvol')
def reservvol():
    return render_template("reservvol.html")


@app.route('/reservlogement')
def reservlogement():
    return render_template("reservlogement.html")


app.run(debug=True)


print('TORMA PITIN')