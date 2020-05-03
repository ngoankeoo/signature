import errno
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
message = b'This is my message to Ngoankeooo'

try:
    with open('private.pem', 'r') as read_file:
        key = RSA.importKey(read_file.read())
except IOError as err:
    if err.errno != errno.ENOENT:
        raise
    # No private key, generate new one. This is take a few seconds.from
    key = RSA.generate(4096)
    with open('private.pem', 'wb') as write_file:
        write_file.write(key.exportKey('PEM'))
    with open('public.pem', 'wb') as write_file:
        write_file.write(key.publickey().exportKey('PEM'))

hasher = SHA256.new(message)
signer = PKCS1_v1_5.new(key)
signature = signer.sign(hasher)
print("Signature: {0}".format(signature))
