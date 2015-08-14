from pyramid.view import view_config
from encryption import generate_key, get_cipher_suite, encrypt, decrypt

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'encryption_service'}

@view_config(route_name='generatekey', renderer='json')
def generatekey_view(request):
    key = generate_key()
    print key
    return {'key': str(key)}

@view_config(route_name='encrypt', renderer='json')
def encrypt_view(request):
    print str(request) + '\n\n\n'
    key = request.json()['key']
    plain_text = request.json_body['plain_text']
    cipher_suite = get_cipher_suite(key)
    cipher_text = cipher_suite.encrypt(plain_text)
    return {'cipher_text', cipher_text}

@view_config(route_name='decrypt', renderer='json')
def decrypt_view(request):
    key = request.json()['key']
    cipher_text = request.json_body['cipher_text']
    cipher_suite = get_cipher_suite(key)
    plain_text = cipher_suite.decrypt(cipher_text)
    return {'plain_text', plain_text}
