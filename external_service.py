import requests

def get_access_token():
    

    
    url = 'https://external-service.com/auth'
    
    headers = {'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzgxNDYyMDEsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6Imh0dHBzOi8vdC5tZS9iYWJrb3cifQ.QWvti9r95p4UCxCBPoPRI3KFRTE48bQCggjYmCE1FoQ'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        access_token = data['access_token']
        return access_token
    else:
        
        raise Exception('Ошибка получения токена доступа')

def send_message(message):
    

    
    url = 'https://external-service.com/messages'
    
    headers = {'Authorization': 'Bearer YOUR_ACCESS_TOKEN'}
    data = {
        'recipient': message.recipient,
        'text': message.text,
        # Другие данные сообщения
    }
    
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        # Обработайте успешный ответ
        pass
    else:
        # Обработайте ошибку, если не удалось отправить сообщение
        raise Exception('Ошибка отправки сообщения')


