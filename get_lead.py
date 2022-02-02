from flask import Flask
from flask import request
import requests as rq
from auth import get_token
import json
import phonenumbers
from urllib import parse

app = Flask(__name__)


@app.route('/lead', methods=['POST'])
def get_leads():
    data = request.form.to_dict()
    print(data)
    motor_id = data['motor_id']
    name = data['name']
    unformat_phone = data['phone']
    comment = parse.quote(data['comment'][14:])
    print(motor_id, name, unformat_phone, comment)

    parse_phone = phonenumbers.parse(unformat_phone, None)
    national_phone = str(phonenumbers.format_number(parse_phone, phonenumbers.PhoneNumberFormat.NATIONAL))
    phone = '+7' + national_phone[1:]
    print(parse_phone, national_phone, phone)

    token = get_token()
    client_data = {
        "name": name,
        "phone[]": phone
    }
    create_client = rq.post('https://api.remonline.ru/clients/', params={"token": token}, data=client_data)
    print(create_client, create_client.text, create_client.json())

    client_id = create_client.json()["data"]["id"]

    post_data = f'client_id={int(client_id)}&leadtype_id=81441&description={comment}'
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    create_lead = rq.post('https://api.remonline.ru/lead/', data=post_data, params={"token": token}, headers=headers)
    print(create_lead, create_lead.text, create_lead.json())

    return 'Form Data Example'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
