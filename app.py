from flask import Flask, request, jsonify, render_template
import socket

app = Flask(__name__)

def ip_to_domain(ip_address):
    try:
        domain = socket.gethostbyaddr(ip_address)
        return domain[0]
    except socket.herror:
        return None

def domain_to_ip(domain_name):
    try:
        ip = socket.gethostbyname(domain_name)
        return ip
    except socket.gaierror:
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    if data['type'] == 'ip_to_domain':
        domain = ip_to_domain(data['input'])
        if domain:
            return jsonify({'result': domain})
        else:
            return jsonify({'error': 'Domain not found'}), 404
    elif data['type'] == 'domain_to_ip':
        ip = domain_to_ip(data['input'])
        if ip:
            return jsonify({'result': ip})
        else:
            return jsonify({'error': 'IP not found'}), 404
    else:
        return jsonify({'error': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(debug=True)
