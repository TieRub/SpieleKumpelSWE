from flask import request, flash, redirect, url_for, render_template
from src.database import *
def kumpel_verwaltung(sender_id, receiver_id):
    print(f"Sender ID: {sender_id}, Receiver ID: {receiver_id}")
