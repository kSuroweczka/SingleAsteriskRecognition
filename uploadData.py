import json

def upload_data(file_path):
    """
    Uploads data from a json file and returns a list of tuples containing the key and the resources of each policy.
    """
    with open(file_path) as f:
        data = json.load(f)

    resources_list = []

    for key, value in data.items():
            if len(value['PolicyDocument']) == 0:
                resources_list.append((key, [None]))
            if "Statement" in value['PolicyDocument']:
                res = []
                for statement in value['PolicyDocument']['Statement']:
                    if 'Resource' in statement:
                        resource = statement['Resource']
                        res.append(resource)
                    else:
                        res.append(None)
                resources_list.append((key, res))
            else:
                resources_list.append((key, [None]))
    return resources_list