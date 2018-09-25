from flask import Flask, render_template
from gpiozero import Servo
from time import sleep
import config

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', name=0)


@app.route('/spin')
def spin():
  servo = Servo(17)
  servo.max()
  sleep(1)
  servo.detach()
  print("servo spin ran")
  return render_template('index.html', name=0)


app.run(host=config.GENERAL_CONFIG['host'])
