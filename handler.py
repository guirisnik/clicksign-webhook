from json import loads


def main(event, context = None):

    clicksign_data = loads(event['body'])

    if clicksign_data['event']['name'] == "auto_close":
        issuer_full_name = clicksign_data['document']['template']['data']['issuer_full_name']
        print(issuer_full_name)

    return {
        'statusCode': 200,
        'body': 'Success'
    }