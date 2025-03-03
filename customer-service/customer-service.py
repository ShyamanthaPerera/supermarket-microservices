from flask import Flask, jsonify
import py_eureka_client.eureka_client as eureka_client

app = Flask(__name__)

CONTEXT_PATH = "/customer-service"
SERVICE_PORT = 5000
EUREKA_SERVER = "http://localhost:8761/eureka/"

eureka_client.init(
    eureka_server = EUREKA_SERVER,
    app_name = "CUSTOMER-SERVICE",
    instance_port = SERVICE_PORT
)

# http://127.0.0.1:5000/customer-service/customers
@app.route(f'{CONTEXT_PATH}/customers', methods=["GET"])
def get_customer():
    customer_list=[
        {"id":1, "name":"John", "email":"john@gmail.com"},
        {"id":2, "name":"John", "email":"john@gmail.com"}
    ]
    return jsonify(customer_list)

app.run(port=SERVICE_PORT)