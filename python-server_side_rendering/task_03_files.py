from flask import Flask, render_template,request
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
       return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    try:
        with open('items.json') as f:
            data = json.load(f)
            items = data.get("items", [])
    except Exception as e:
        print("Error", e)
        items = []
    return render_template('items.html', items = items)

@app.route('/source')
def source():
    filename = request.args.get('filename')
    if not filename:
        return "Missing filename parameter", 400
    
    try:
        with open(filename, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        return "File not found", 404
    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)