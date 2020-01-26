import boto3
import os

if __name__ == '__main__':
    table_name = os.environ["DEV_AUTH_TABLE"]

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    # Corresponding key: "WknzO6H-rU5s_puTeorirwyf9gh6fTK1BAlfDNiyAEiz9kQAkfeU1M3my3H4bSjHa6sEJDRvvYRLUCTxYjW1yA"
    table.put_item(Item={
        'ID': "WknzO6H-rU5s_puTeorirwyf9gh6fTK1",
        'hash': "$argon2id$v=19$m=75000,t=5,p=8$AeCc05ozBqDU+p+T0rpXKg$P6g8Mqn2iaFN6BBeVt7Mwg",
        'created_on': '1579729631.106215',
        'event_log': {},
        'key_type': 'USER',
        'entity_id': '123123'})
