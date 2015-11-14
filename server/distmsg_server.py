from flask import Flask, request
import json, uuid

app = Flask(__name__)

all_message_list = []

#demo_msg = {
#    'sender'      : '123456789',
#    'source_gps'  : '32N 54W',
#    'destination' : '987654321',
#    'msg_uuid'    : uuid.uuid4(),
#    'msgtype'     : 'p2p',
#    'gps_center'  : '31N 54W',
#    'gps_radius'  : 1024
#}

#msg
#    header
#        source
#            sender_id - str
#            sender_name - str
#            gps_location - str
#        destination
#            receiver_id - str
#            gps_center - str
#            gps_radius - int
#        msg_uuid - str
#        msg_type - str
#    payload - str

demo_msg = {
    'header' : {
        'source' : {
            'sender_id'    : '123456789',
            'sender_name'  : 'Klaus Typ',
            'gps_location' : '54N, 23W',
        },
        'destination' : {
            'receiver_id' : '987654321',
            'gps_center'  : '53N, 23W',
            'gps_radius'  : 1024,
        },
        'msg_uuid' : str(uuid.uuid4()),
        'msg_type' : 'p2p'
    },
    'payload' : 'Help my cows!'
}

all_message_list.append(demo_msg)

@app.route('/human/getall')
def human_readable_get_all():
    retval = ''

    for msg in all_message_list:
        retval += json.dumps(msg, sort_keys=True,
                                  indent=4,
                                  separators=(',<br>', ':<br> ') )

    return retval

@app.route('/getall')
def json_get_all():
    return json.dumps(all_message_list, separators=(',',':'))

@app.route('/push', methods=['POST'])
def json_push():
    if request.json is not None:
        x = json.loads(request.json)

        if type(x) is list:
            all_message_list.extend(x)
        else:
            all_message_list.append(x)

    return str(len(all_message_list))



def tablemaker(header_row, other_rows):
    retval = '<table border="1">'

    # First, print the header
    retval += '<tr>'
    for item in header_row:
        retval += "<th>{}</th>".format(item)
    retval += '</tr>'

    # Now print each row
    for row in other_rows:
        retval += "<tr>"
        for item in row:
            retval += "<td>{}</td>".format(item)
        retval += "</tr>"

    retval += "</table>"

    return retval

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
