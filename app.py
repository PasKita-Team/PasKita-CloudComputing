from flask import Flask, jsonify
from google.cloud import firestore
from google.oauth2 import service_account

app = Flask(__name__)

# Konfigurasi Firestore
firebase_credentials = "apikey.json"
firebase_client = firestore.Client.from_service_account_json(firebase_credentials)
firestore_collection_name = "hasil_generated"

# Fungsi untuk mendapatkan data dari Firestore
def get_firestore_data():
    try:
        # Mendapatkan data dari Firestore
        data = []
        docs = firebase_client.collection(firestore_collection_name).stream()
        for doc in docs:
            data.append(doc.to_dict())
        return data
    except Exception as e:
        return str(e)
@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Mendapatkan data dari Firestore
        firestore_data = get_firestore_data()

        # Mengembalikan data sebagai respons API
        return jsonify({'data': firestore_data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("port", 8080)))
