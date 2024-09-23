from flask import Flask, request, jsonify
import logging
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/send_message": {"origins": "https://your-allowed-origin.com"}})
# Настройка логирования
logging.basicConfig(level=logging.INFO)

@app.route('/send_message', methods=['POST'])
def log_data():
    data = request.json
    chosen_place = data.get('chosenPlace')
    selected_date = data.get('selectedDate')

    # Логирование полученных данных
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    app.logger.info(f'Received data: chosenPlace={chosen_place}, selectedDate={selected_date} --- Time: {current_time}')

    return jsonify({'message': 'Data received'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)