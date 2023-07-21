
########### Python 3.2 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64

headers = {
    # Request headers
    'Authorization': '',
    'X-Callback-Url': '',
    'X-Reference-Id': '',
    'X-Target-Environment': '',
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '68fb094453fe45e883ac8afa721e7fbd',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('sandbox.momodeveloper.mtn.co.rw')
    conn.request("POST", "/collection/v1_0/requesttopay?%s" % params, "500, EUR, help101, 250788314048, askingtopay", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################