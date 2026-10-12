from flask import Flask, render_template, request, redirect, session
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.secretkey = os.getenv("APP_SECRET_KEY")