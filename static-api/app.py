import os
from flask import Flask, jsonify
  
app = Flask(__name__)
  
person1 = {'id': 1, 'name': 'John', 'lastname': 'Doe', 'age': 33, 'gender': 'Male',
'lucky_numbers': [7, 13, 22]}
person2 = {'id': 2, 'name': 'Jane', 'lastname': 'Doe', 'age': 35, 'gender': 'Female',
'lucky_numbers': [10, 14, 3]}
person3 = {'id': 3, 'name': 'Jimmy', 'lastname': 'Doe', 'age': 5, 'gender': 'Male',
'lucky_numbers': [1]}
family = {'lastname': 'Doe', 'members': [person1, person2, person3]}

@app.route('/members')
def hello():
    luckySum = sum(person1['lucky_numbers']) + sum(person2['lucky_numbers']) + sum(person3['lucky_numbers'])
    return jsonify({
        'status_code': 200, 
        'data': {
            'members': [person1, person2, person3],
            'family-name': family['lastname'], 
            'lucky_numbers': person1['lucky_numbers'] + person2['lucky_numbers'] + person3['lucky_numbers'],
            'sum_of_lucky': luckySum
        }
    })
    
@app.route('/members/<int:member_id>')
def hello2(member_id):
    a = {
        'status_code': 200,
        'data': ""
    }
    b = {
        'status_code': 200,
        'message': 'member not found'
    }
    for x in family['members']:
        if(x['id'] == member_id):
            a['data'] = x
            return jsonify(a)
    return jsonify(b)
  
  
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))