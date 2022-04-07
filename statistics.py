import os
import json
import zipfile
from unittest import mock

@mock.patch.dict(os.environ, {"DIDS": " [ \"8f67E08be5dD941a701c2491E814535522c33bC2\" ]"})
@mock.patch.dict(os.environ, {"ROOT_FOLDER": os.path.dirname(os.path.realpath(__file__))})
def get_job_details():
    root = os.getenv('ROOT_FOLDER', '')
    """Reads in metadata information about assets used by the algo"""
    job = dict()
    job['dids'] = json.loads(os.getenv('DIDS'))
    job['metadata'] = dict()
    job['files'] = dict()
    job['algo'] = dict()
    job['secret'] = os.getenv('secret', None)
    if job['dids'] is not None:
        for did in job['dids']:
            # get the ddo from disk
            filename = root + '/data/ddos/' + did
            print(f'Reading json from {filename}')
            with open(filename) as json_file:
                ddo = json.load(json_file)
                # search for metadata service
                for service in ddo['service']:
                    if service['type'] == 'metadata':
                        job['files'][did] = list()
                        index = 0
                        for file in service['attributes']['main']['files']:
                            job['files'][did].append(
                                root + '/data/inputs/' + did + '/' + str(index))
                            index = index + 1
    return job


def descriptive_statistics(job_details):
    root = os.getenv('ROOT_FOLDER', '')
    print('Starting compute job with the following input information:')
    print(json.dumps(job_details, sort_keys=True, indent=4))
    """ Computes descriptive statistics for the first file in first did """
    first_did = job_details['dids'][0]
    for f in os.listdir('data/inputs/'+first_did+'/'):
        if os.path.splitext(f)[1] == '.zip':
            filename = f
    print(filename)
    with zipfile.ZipFile('data/inputs/'+ first_did + '/' +filename, 'r') as zip_ref:
        zip_ref.extractall('data/inputs/'+first_did)
    for f in os.listdir('data/inputs/'+first_did+'/'):
        if os.path.splitext(f)[1] !='.zip':
            folder = f
    images = list()
    for f in os.listdir('data/inputs/'+first_did+'/'+folder+'/'):
        images.append(f)
    print(images)



if __name__ == '__main__':
    descriptive_statistics(get_job_details())
