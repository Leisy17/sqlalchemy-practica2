import datetime
import json


def get_body(event):
    data = event.get("httpMethod")
    if data == "GET" or data == "DELETE":
        body = event['queryStringParameters']
    else:
        body = event.get('body')
        if type(body) != dict:
            body = json.loads(event['body'])
            if body.get('Message'):
                body = json.loads(body['Message'])
    return body


def validate_date(date: str) -> None:
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def response(msg, statusCode=200):

    msg = {
        'statusCode': statusCode,
        'body': json.dumps(msg)
    }
    return msg


def handler(func):
    def Any_Error(*args):
        statusCode = 400
        event = args[0]
        context = args[1]
        try:
            if event.get('Records'):
                for val in event['Records']:
                    msg = func(val, context)
            elif event.get('httpMethod'):
                msg = func(event, context)
            statusCode = 200
        except KeyError:
            msg = {"msg": "Todos los campos son necesarios."}
        except TypeError:
            msg = {"msg": "Inserte caracteres válidos."}
        except ValueError as error:
            print(str(error))
            msg = {"msg": str(error)}
        except Exception as error:
            print(str(error))
            msg = {"msg": str(error)}

        return response(msg, statusCode)
    return Any_Error
