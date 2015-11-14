from flask import Flask
import json, uuid

app = Flask(__name__)

all_message_list = []

demo_msg = {
    'sender'      : '123456789',
    'source_gps'  : '32N 54W',
    'destination' : '987654321',
    'msg_uuid'    : uuid.uuid4(),
    'msgtype'     : 'p2p',
    'gps_center'  : '31N 54W',
    'gps_radius'  : 1024
}

all_message_list.append(demo_msg)

@app.route('/human/getall')
def human_readable_get_all():
    header = demo_msg.keys()
    msgs   = [msg.values() for msg in all_message_list]

    return tablemaker(header, msgs)





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
    app.run(host='0.0.0.0')
