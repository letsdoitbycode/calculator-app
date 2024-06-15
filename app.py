from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data['operation']
    num1 = data['num1']
    num2 = data['num2']
    
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return jsonify({"error": "Invalid input! Please enter numeric values."}), 400
    
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return jsonify({"error": "Error! Division by zero."}), 400
        result = num1 / num2
    else:
        return jsonify({"error": "Invalid operation!"}), 400
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
