import os
from requests import get
from json import dumps
from time import sleep
from hmac import new
from hashlib import sha1
from aminofix import Client
from bs4 import BeautifulSoup as bs
import random
from os import system
A = "\033[1;91m"  #احمر
Z1 = '\033[2;31m' #احمر ثاني
E = "\033[1;92m"  #اخضر
H = "\033[1;93m" #اصفر
L = "\033[1;95m" #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح 
M = "\033[1;94m" #ازرك
t = "_"
print(Y)
import pyfiglet
logo="""\033[31m⣿⣿⣿⣿⣿⣿⡿⣾⡇⣸⣿⡌⠀⢀⣀⣀⣞⣁⣾⣉⣉⣻⣄⣤⠄⠤⠤⠶⡶⠖⢺⣿⣸⡏⠹⣷⣿⣿⡀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⣸⡟⡇⣿⣟⡏⠉⠍⠉⣏⣿⣍⠙⠛⠋⣩⠇⠀⠀⠀⠀⢠⠁⠀⢸⣿⣿⠁⠀⣿⡆⠀⢸⣿⡆⠀⠀⠀⠀⣿⣷⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⡿⠀⢀⣿⠁⣷⣿⣿⠁⠀⠀⠀⡟⠷⠼⠟⠒⠛⠁⠀⠀⠀⠀⠀⡜⠀⠀⢸⣿⣇⣀⣬⣿⡇⠀⢸⣿⣇⠀⠀⠀⠀⣿⣿⡆⠀⠀⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⡇⠀⣾⣿⣰⣿⣿⢸⠀⠀⢸⡀⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣤⣤⣶⣾⣿⣿⡿⠟⢿⣧⠆⣿⣿⣿⠀⠀⠀⠀⣿⣿⣷⠀⠀⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡇⠀⠀⠀⢀⣾⠃⢠⣿⣿⣿⣿⣿⣿⣶⣶⣶⣿⣷⣶⣶⣶⣿⣿⣿⣿⣿⣿⡿⢯⣿⣿⣻⣿⣧⠶⢶⢶⣿⣿⢸⣿⣿⣿⠀⠀⠀⢨⣿⡿⣿⠀⡀⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠁⠀⠀⠀⣾⢾⠀⣾⣿⣏⠉⢻⡏⢉⣛⡿⣯⣉⡉⠉⠉⠻⡉⠉⠛⣁⣀⣠⣶⣿⣋⡶⣯⣿⢥⡀⠉⠉⣻⣿⣿⣿⣿⣿⡇⠀⠀⣼⣿⡇⢿⡆⣷⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⠀⢰⣿⢹⢠⣿⣿⣿⠐⣾⣷⠖⠛⢉⣛⣿⣿⣗⢖⠜⠃⠸⠄⠉⢛⠽⣾⣷⠟⠀⣧⣿⣿⡇⠀⢰⢿⣿⣿⣿⣿⣿⣇⠀⢠⣿⣿⡇⢸⣧⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⠀⣿⣿⢸⣾⣿⣿⣿⡄⠘⣧⠀⢰⣿⣿⣾⡏⠹⡿⠅⣦⠴⠖⠒⣾⡄⠛⢏⣀⣀⣈⣉⣉⣠⣴⠟⣾⣿⢿⣿⣿⣿⣿⢀⣾⣿⣿⠇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⢰⣿⣿⢸⣿⣿⣿⣿⣇⠀⢈⣧⣄⡙⢓⣛⣁⣤⣵⣴⠌⠃⠀⠀⠼⠳⣦⣌⣉⡛⠛⠓⠒⠂⠀⠀⣿⡟⣸⣿⣿⣿⣿⣼⣿⣿⣿⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⠀⠀⣾⣿⣿⣼⣿⣿⣿⣿⣿⡀⠀⠈⠉⠀⠈⠉⠑⠚⡡⠋⠀⠀⠀⠀⠀⠀⠀⠑⠦⣀⠀⠀⠀⠀⠀⢀⣿⢣⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋
⣿⣿⣿⣿⣿⡀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢀⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠦⡀⠀⠀⢸⢇⠆⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢋⠀⠀⠀
⣿⣿⣿⣿⣿⡇⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⢠⠎⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠌⠎⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠉⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠰⠃⠀⠀⠀⠀⢸⣀⣀⣀⣤⡀⠀⠀⠀⠀⠀⠀⠰⣄⠈⢆⡀⠀⣼⣿⣿⣿⣿⠿⠿⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⢠⠃⠀⠀⠀⠀⠀⠀⠑⠮⣀⠽⠁⠀⠀⢀⣀⠤⡶⣻⣿⡇⠀⠁⢰⣿⣿⡏⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢷⡀⠈⠀⠀⠻⣖⠒⠒⠂⠀⠐⠒⠒⠒⠋⣉⣁⠤⠴⡿⠃⣿⠁⠀⠀⡆⣿⣿⣿⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣧⡀⠀⢰⡏⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠱⡄⠀⠀⠀⠹⣿⡟⢻⠛⠛⠛⠉⠉⠉⠀⠀⠀⣰⢳⣦⠃⠀⠀⡸⢠⣿⣿⣿⡆⢸⡀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀
⣿⣷⣄⡈⠉⠘⡞⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢸⢆⠀⠀⠀⠹⡧⣼⠞⠉⠓⠒⠂⠐⠛⠉⣹⠃⡸⠃⠀⠀⡰⢃⣼⣿⣿⣿⣧⠈⡇⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣇⠀⠀⢻⡹⣿⠏⠸⣿⣿⣿⡏⣿⡇⠀⠀⠀⢸⠈⠳⣀⠀⠀⠱⡈⠢⠤⠀⠀⠀⠤⠔⠚⣁⠞⠁⠀⢀⡔⡱⠋⢸⣿⣿⡿⢻⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴
⣿⣿⣿⣿⣧⣒⡈⣧⢯⠀⠀⢿⣿⣿⡏⢿⡇⠀⠀⠀⠘⠀⠀⠘⢦⣀⠀⠙⠢⣤⠤⠀⠠⣤⠴⠊⠁⠀⠀⣠⣮⠎⠀⠀⣿⣿⣿⠃⢸⠀⣿⢈⣈⡀⠀⣀⣀⣀⣀⣀⠌⢀⣴⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀	AKATUSKI AMINO  """
print(H+'Instagram:-SFAH_101\nTelegram:-AKAT_4\nAmino:-S_F8')
print(logo)
print(B)
import random
password = input("password>>>")
secmail = 'https://www.1secmail.com/api/v1/?action='
count = 0

def email_generator():return 'Team OKSPLORS'+''.join(get(f'{secmail}genRandomMailbox').json())

def device_generator():
 identifier = os.urandom(20)
 return ("19" + identifier.hex() + new(bytes.fromhex("E7309ECC0953C6FA60005B2765F99DBBC965C8E9"), b"\x19" + identifier, sha1).hexdigest()).upper()

def save_account(email,password,device):
 account = dumps({'email':email,'password':password,'device':device})
 file = open('accounts.json','a')
 file.write(f'{account},\n')
 file.close()

def get_code(email):
 info = email.split('@')
 sleep(2.5)
 login = info[0]
 domin = info[1]
 id = get(f'{secmail}getMessages&login={login}&domain={domin}').json()[0]['id']
 html = get(f'{secmail}readMessage&login={login}&domain={domin}&id={id}').json()['body']
 data = bs(html,features="html.parser").get_text()
 return data.split()[28]
 
while True:
 count +=1
 try:
  email = email_generator()
  print(email)
  deviceId = device_generator()
  client = Client(deviceId=deviceId)
  client.request_verify_code(email=email)
  url = get_code(email)
  print(url)
  code = input('code:')
  client.register(email=email,password=password,nickname='Team OKSPLORS',verificationCode=code,deviceId=deviceId)
  save_account(email,password,deviceId)
  print(f'account_saved[{count}]\n')
 except Exception as e:
  print(e)
  pass
