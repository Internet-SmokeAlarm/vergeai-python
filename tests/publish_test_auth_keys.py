import boto3
import os


if __name__ == '__main__':
    table_name = os.environ["DEV_AUTH_TABLE"]

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    table.put_item(Item={
        'ID': "Pr9FDAEvCYY68XDZX5hH-V4DlDXx0oXx",
        'hash': "$argon2id$v=19$m=75000,t=5,p=8$Nebcu1cqJWTMWeu9NybkHA$Hf/306TF0Yd7H90rtSxQgg",
        'created_on': '1579729631.106215',
        'event_log': {},
        'key_type': 'USER',
        'entity_id': '123123'})
