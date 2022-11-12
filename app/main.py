from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/shutdown", methods=["POST"])
def shutdown():
  os.system("sudo shutdown -h now")
  return "Shutting down…"

@app.route("/")
def index():
  return render_template('index.html')

# if __name__ == "__main__":
  # Only for debugging while developing
  # app.run(host='0.0.0.0', debug=True, port=80)
