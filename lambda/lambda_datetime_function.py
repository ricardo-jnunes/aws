import sys
from datetime import datetime
        
# Retorna a hora atual
def get_current_time():
    return datetime.now().strftime("%H:%M:%S")
        
        
        
def handler(event, context):
    return {
        'statusCode': 200,
        'body': get_current_time()
    }
