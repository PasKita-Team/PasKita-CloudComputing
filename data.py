import requests

# Ganti URL dengan URL API Anda
api_url = 'http://127.0.0.1:5000/get_data'

# Kirim permintaan GET ke API
response = requests.get(api_url)

# Periksa apakah permintaan berhasil (kode status 200)
if response.status_code == 200:
    # Parse data JSON dari respons
    data = response.json()

    # Ambil teks yang berisi URL produk
    urls = [item['url_produk'] for item in data['data']]

    # Tampilkan URL produk
    for url in urls:
        print(url)
else:
    # Tampilkan pesan kesalahan jika permintaan tidak berhasil
    print(f'Error: {response.status_code} - {response.text}')
