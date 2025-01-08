from flask import render_template,request,redirect,url_for,flash
from flask_login import login_user,logout_user,login_required
from app import app,db,bcrypt
from app.models import User
from app.forms