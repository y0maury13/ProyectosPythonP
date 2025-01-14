from flask import*
import json,time

app =Flask(__name__)

@app.router('/',methods=['GET'])
def home_page():
    data_set={'Page':'Home','Message': 'Successfully loaded page','Timestamp':time.time()}
    json_dump=json.dumps(data_set)
    return json_dump

@app.route('/user/',methods=['GET'])
def request_page():
    user_query =str(request.args.get('user'))
    data_set={'Page':'Request','Message': 'Successfully got the request for{user_query}','Timestamp':time.time()}
    json_dump=json.dumps(data_set)
    return json_dump