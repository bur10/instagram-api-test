import requests

# zh69Xct?f6zu!9 denizxxar
# emc2pass cokmakbulegecti

url = 'https://www.instagram.com/accounts/login/'
url_main = url + 'ajax/'
auth = {
    "enc_password": "#PWD_INSTAGRAM:0:0:zh69Xct?f6zu!9",
    "username": "denizxxar", }
headers = {}

with requests.Session() as s:
    req = s.get(url)
    print(req.status_code, req.headers)
    headers['x-csrftoken'] = req.cookies['csrftoken']
    res = s.post(url_main, data=auth, headers=headers)
    # Now, you can use 's' object to 'get' response from any instagram url
    # as a logged in user.
    print(res.status_code)

    if res.status_code == 200:
        print(res.json(), res.headers)

        # headers['cookie'] = res.cookies['Set-Cookie']

    # r = s.get('https://www.instagram.com/accounts/edit/')

    # If you want to check whether you're getting the correct response,
    # you can use this:
    # print(auth['username'] in r.text)  # which returns 'True'
