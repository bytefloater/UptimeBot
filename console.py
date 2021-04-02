def log(message, type='info'):
    if type == 'info':
        print('[i]', message)
    else:
        print('   ', message)
