import base64
import time
import hmac
import hashlib


def main():
    #### Secret
    # what secr ares this
    blank_secret = "whatsecraresthis"
    # blank_secret = "what secr ares this"
    secret = base64.b32decode(blank_secret.upper())

    print blank_secret
    # print "Google entered key->", blank_secret
    # print "secret->", secret

    # print "Now printing Google Auth codes every 30s, match these with app..."
    msg = int(time.time()/30)
    old_msg = int(time.time()/30)
    print totp_algo(secret) 

    while(1):
        msg = int(time.time()/30)
        if(msg != old_msg):
            print totp_algo(secret) 
            old_msg = msg


def totp_algo(key):
    # Get time msg every 30 second interval
    msg = int(time.time() / 30)
    hex_string = '{:016x}'.format(msg)
    buckets = []
    for i in range(len(hex_string)-1, 0, -2):
        hex_byte = hex_string[i-1] + hex_string[i]
        dec_byte = int(hex_byte, 16)
        buckets.insert(0, dec_byte)

    # Convert to byte array
    buckets = bytearray(buckets)

    sha_hmac = hmac.new(key = key, msg = buckets, digestmod = hashlib.sha1).hexdigest()
    return offset(sha_hmac)

def offset(sha_hmac):
    offset = int(sha_hmac[-1],16)
    # double for bytes 
    offset = offset * 2

    # Example HOTP computation algo - dynamic truncation - from https://tools.ietf.org/html/rfc4226
    offset_bits = int(sha_hmac[offset:(offset+8)], 16) & 0x7fffffff 
    offset_bits %= pow(10,6)

    return str(offset_bits).zfill(6)

if __name__ == "__main__":
    main()
