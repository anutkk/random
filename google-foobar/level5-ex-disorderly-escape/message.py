import base64

MESSAGE = '''
CEYeAAYPSx8cSURURVUUEwgUEUsCTEgNCwIJFxIGGBBCTBRMSAsXGgAXHgQJUklMCQkJCAscEQFU QVdVQgVADx0LAAcHHhZGQVVCDU0EBgsSCwgXHRVKVV9MCRkBAgsNDhcXRkFVQh5PDg0HEB1CUklB SgYECktLQ05DCAodVEFXVUIbRwJOSRk=
'''

KEY = 'samuel.londner'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)