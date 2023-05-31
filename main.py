from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="og:image" content="https://cdn.discordapp.com/avatars/295917036335398922/b91342410e6cc08011fe7ca10223a18d.png?size=2048">
    <meta name="og:title" content="Eviltwin">
    <meta name="og:description" content="'Pls cumshot on me' - Eviltwin 2010-2023">
    <title>Document</title>
</head>
<body>
    
</body>
</html>"""
