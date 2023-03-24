import json
import psycopg2
import os

def lambda_handler(event, context):
    user = event['request']['userAttributes']
    print('userAttributes')
    print(user)

    user_display_name  = user['name']
    user_email         = user['email']
    user_handle        = user['preferred_username']
    user_cognito_id    = user['sub']
    try:
      print('entered-try')
      conn = psycopg2.connect(os.getenv('PROD_CONNECTION_URL'))
      cur = conn.cursor()
      cur.execute("INSERT INTO users (display_name, email, handle, cognito_user_id) VALUES(%s, %s, %s, %s)", (user['name'], user['email'], user['preferred_username'], user['sub']))
      params = [
        user_display_name,
        user_email,
        user_handle,
        user_cognito_id
      ]
      conn.commit() 

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print('Database connection closed.')

    return event