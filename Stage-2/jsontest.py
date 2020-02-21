import json

data = [ 
    {   
        'user_id': 1000,
        'name': 'Shiyan',
        'pass': 10, 
        'study_time': 50, 
    },  
    {   
        'user_id': 2000,
        'name': 'Lou',
        'pass': 15, 
        'study_time': 171,
    }   
]

json_str = json.dumps(data)
with open('/tmp/jsontest.json', 'w') as json_f:
    json_f.write(json_str)

'''
with open('/tmp/jsontest.json', 'w') as json_f:
    json.dump(data, json_f)
'''
