from flask import Flask, request, send_from_directory
import json, uuid, requests

app = Flask(__name__)

all_message_dict = {}

### insert one demo message
#demo_msg = {
#    'header' : {
#        'source' : {
#            'sender_id'    : '123456789',
#            'sender_name'  : 'Klaus Typ',
#            'gps_location' : '54N, 23W',
#        },
#        'destination' : {
#            'receiver_id' : '987654321',
#            'gps_center'  : '53N, 23W',
#            'gps_radius'  : 1024,
#        },
#        'msg_uuid' : str(uuid.uuid4()),
#        'msg_type' : 'p2p'
#    },
#    'payload' : 'Help my cows!'
#}
#
#all_message_dict[demo_msg['header']['msg_uuid']] = demo_msg

@app.route('/human/getall')
def human_readable_get_all():
    retval = ''

    for msg in all_message_dict.values():
        retval += json.dumps(msg, sort_keys=True,
                                  indent=4,
                                  separators=(',<br>', ':<br> ') )

    return retval

@app.route('/getall')
def json_get_all():
    retval = { 'messages': all_message_dict.values() }
    return json.dumps(retval, separators=(',',':'))

@app.route('/push', methods=['POST'])
def json_push():
    if request.json is not None and 'messages' in request.json:
        x = request.json
        for msg in x['messages']:
            all_message_dict[msg['header']['msg_uuid']] = msg

    return str(len(all_message_dict))

@app.route('/sync')
def initiate_sync():
    ip = request.args.get('ip')

    r = requests.get('http://{}:5000/getall'.format(ip))

    items = r.json()

    if 'messages' in items:
        for msg in items['messages']:
            all_message_dict[msg['header']['msg_uuid']] = msg

    return str(len(all_message_dict))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
