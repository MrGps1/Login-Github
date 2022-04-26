import requests

email = 'USER or EMAIL'

passwd = 'PASSWD'

url = 'https://github.com/session'

headers = {

'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',

'accept-encoding': 'gzip, deflate, br',

'accept-language': 'ar,en-US;q=0.9,en;q=0.8',

'cache-control': 'max-age=0',

'content-length': '539',

'content-type': 'application/x-www-form-urlencoded',

'cookie': '_octo=GH1.1.1602150843.1629997608; _device_id=2cfe8a0e419dfac78cf692e1d4ab314b; has_recent_activity=1; tz=Asia%2FBaghdad; tz=Asia%2FBaghdad; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; logged_in=no; _gh_sess=lRR5kFMx%2FlqgPtVpWJ%2BJAplP9pV6kkZOP6b0vx4s2FIuU%2B%2FBG777M9KbIzH%2F0%2Fc5GxssendhoACPBk8kMuvyBcqN23lOyFlZf821%2FrRY%2BlJLiB7cyZ01m6eF8bonJtjf0PW0Zh%2BVY15xCY0uy1I5ib7Sx9191WRaFNawYcqj39B26%2Fewq%2Fnt7kxliFzYVM%2BcCnqx%2BNi3tPcO9bD3lIeL%2FeHW6XeBWZmS8IZxo1bI1nQ6ohoACe5nyc6vuDKH4ABY4Gm6X9T5PdvA3gFrnET%2BDg%3D%3D--Du38ZoVbadjHBMt%2F--9BaWzXXfAtGz5F9V0T4k6A%3D%3D',

'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'

}

data = {

'commit': 'Sign in',

'authenticity_token': '6BiZ-RX3lpYxVhfauwg6_K_YePJUwZvaOzrr8kfuJJg85VpwcWnieB3GcaL8xs1aNbb-7mKgKwpocXsU_3YFvw',

'login': email,

'password': passwd,

'trusted_device': '',

'webauthn-support': 'supported',

'webauthn-iuvpaa-support': 'unsupported',

'return_to': 'https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home',

'allow_signup': '',

'client_id': '',

'integration': '',

'required_field_1ffb': '',

'timestamp': '1642448287955',

'timestamp_secret':  '6577639cddb7c9207e854bda61a03c8ec8c14d8425b8bfbaccf00cf727553181'

}

r = requests.session()

req=r.post(url,headers=headers,data=data)

if '_octo' in req.cookies:

 print(True)

else:

 print(False)
