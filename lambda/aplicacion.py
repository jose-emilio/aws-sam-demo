from __future__ import print_function
import json

def manejador(event, context):
    for record in event['Records']:
        print('IDEvento: ' + record['eventID'])
        print('NombreEvento: ' + record['eventName'])
        print("Registro de DynamoDB:\n " + json.dumps(record['dynamodb'], indent=2))
    print('Se han procesado %s registros.' % str(len(event['Records'])))
    return {"Registros procesados":str(len(event['Records']))}
