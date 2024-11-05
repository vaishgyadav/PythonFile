# app.py

from flask import Flask, render_template
import yaml

app = Flask(__name__)

@app.route("/")
def home():
    # Load configuration from the YAML file
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    
    # Get the message from the YAML configuration
    message = config.get('message', 'Hello, World!')
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
