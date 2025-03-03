from flask import Flask, jsonify

app = Flask(__name__)

CONTEXT_PATH = "/customer-service"
SERVICE_PORT = 5000

# http://127.0.0.1:5000/customer-service/customer
@app.route(f'{CONTEXT_PATH}/customers', methods=["GET"])
def get_customer():
    customer_list=[
        {"id":1, "name":"John", "email":"john@gmail.com"},
        {"id":2, "name":"John", "email":"john@gmail.com"}
    ]
    return jsonify(customer_list)

app.run(port=SERVICE_PORT)