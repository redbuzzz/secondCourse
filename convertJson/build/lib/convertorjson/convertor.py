import json


def dumping(dictionary):
    with open('to.json', 'w') as f:
        return f.write(json.dumps(dictionary))

def dumping_file(dictionary):
    with open('tofile.json', 'w') as f:
        return f.write(json.dump(dictionary))
