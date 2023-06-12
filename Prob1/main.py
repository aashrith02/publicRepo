from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/numbers', methods=['GET'])
def get_numbers():
    urls = request.args.getlist('url')
    all_numbers = []

    for url in urls:
        try:
            response = requests.get(url)
            data = response.json()
            numbers = data.get('numbers')
            if numbers:
                all_numbers.extend(numbers)
        except Exception as e:
            print(f"Failed to retrieve numbers from {url}: {str(e)}")
    print(all_numbers)
    res = []
    set1 = set()
    for ele in all_numbers:
        if ele not in set1:
            res.append(ele)
            set1.add(ele)
    res.sort()

    return jsonify({'numbers':res})

if __name__ == '__main__':
    app.run(host = 'localhost',port=8008)
