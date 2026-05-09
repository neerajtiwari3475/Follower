I=Exception
E=input
A=print
import os as C
try:import requests as D
except:C.system('pip install requests')
try:from user_agent import generate_user_agent as J
except:C.system('pip install user_agent')
try:import time as G
except:C.system('pip install time')
try:from colorama import Fore as B,Style as F
except:C.system('pip install colorama')
try:import cfonts as K;from cfonts import render
except:C.system('pip install python-cfonts')
import random as L,webbrowser as M,sys,urllib.request
def N():return L.choice(['cyan','blue','green','yellow','magenta'])
def O(C,D=.05):
	for B in C:A(B,end='',flush=True);G.sleep(D)
	A()
def P():B=K.render('SNYH4X',font='block',colors=[N()],align='left',space=False);A(B)
def Q():
	C=f"\n{B.MAGENTA}Telegram: {B.WHITE}@sunyhx\n{B.MAGENTA}   Join {B.WHITE}@old3x{F.RESET_ALL}\n"
	for D in C.split('\n'):A(' '*40+D)
def Z():A=f"{B.RED}FILE HAS EXPIRED.{F.RESET_ALL}\n{B.YELLOW}DM {B.MAGENTA}@sunyhx {B.YELLOW}to Buy or RENEW.{F.RESET_ALL}";R(A,D=.05)
def R(N,D=.01):
	for A in N.split('\n'):O(A,D)
P()
Q()
S=E('[+] Enter Your Telegram User ID: ')
try:
	H=D.get(f"https://jesusx.pythonanywhere.com/?id={S}");H.raise_for_status();T=H.json().get('status')
	if T=='authorized':A('[=] Access Granted...')
	else:A('[!] Access Denied... Please join @Ergusia to use this file.');M.open('https://t.me/+9Hg5yOKG6o5hZmE1');sys.exit()
except I:A('[!] No Internet Connection. Please restart the file.');sys.exit()
def U(Username,Password):
	E={'mid':'aA_YVwABAAHMFelpsm6Zs8wkuuw-','datr':'V9gPaPnL8wt2M_S2mqnwU2FX','ig_did':'0EC39966-48EA-4407-9995-D8AEF68E7D82','rur':'"FRC\\0541783073644\\0541777405133:01f7594c5ec87054dcb4c84e7140bf3c99d664d9e72b4ace44af3f0ceaf2859588532ede"','csrftoken':'zaThv5kcLZ2uAAcyN5aIA4l076ik2KDq','dpr':'3.69307279586792','wd':'796x1554','ig_nrcb':'1'};F={'authority':'www.instagram.com','accept':'*/*','accept-language':'en-US,en;q=0.9','content-type':'application/x-www-form-urlencoded','origin':'https://www.instagram.com','referer':'https://www.instagram.com/?flo=true','sec-ch-prefers-color-scheme':'dark','sec-ch-ua':'"Chromium";v="137", "Not/A)Brand";v="24"','sec-ch-ua-full-version-list':'"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"','sec-ch-ua-mobile':'?0','sec-ch-ua-model':'""','sec-ch-ua-platform':'"Linux"','sec-ch-ua-platform-version':'""','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':J(),'x-asbd-id':'359341','x-csrftoken':'zaThv5kcLZ2uAAcyN5aIA4l076ik2KDq','x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR3XlqS8iJaWE9DlwYzKhsNYFcycVkD_S8lvX8FSjiSZQIEK','x-instagram-ajax':'1022292862','x-requested-with':'XMLHttpRequest','x-web-session-id':'9ream9:9xzg36:oc6tmb'};H=str(G.time()).split('.')[0];I={'enc_password':f"#PWD_INSTAGRAM_BROWSER:0:{H}:{Password}",'optIntoOneTap':'false','queryParams':'{}','trustedDeviceRecords':'{}','username':Username};B=D.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/',cookies=E,headers=F,data=I)
	if B.json().get('authenticated'):C=B.cookies.get_dict().get('sessionid');A(f"[=] Logged in successfully!\n[=] Your sessionid: {C}");return C
	else:A('Failed to login.')
def V(sessionid):C={'mid':'aA_YVwABAAHMFelpsm6Zs8wkuuw-','datr':'V9gPaPnL8wt2M_S2mqnwU2FX','ig_did':'0EC39966-48EA-4407-9995-D8AEF68E7D82','csrftoken':'zaThv5kcLZ2uAAcyN5aIA4l076ik2KDq','ig_nrcb':'1','ds_user_id':'1783073644','dpr':'3.359027862548828','sessionid':sessionid,'ps_l':'1','ps_n':'1','wd':'321x628','rur':'"FRC\\0541783073644\\0541777417790:01f702e383ccca1dfe103a979f35d82b3dc8ea807a0129fb192da391c7e2e16e3cbbd800"'};E={'authority':'www.instagram.com','accept':'*/*','accept-language':'en-US,en;q=0.9','referer':'https://www.instagram.com/accounts/edit/','sec-ch-prefers-color-scheme':'dark','sec-ch-ua':'"Chromium";v="137", "Not/A)Brand";v="24"','sec-ch-ua-full-version-list':'"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"','sec-ch-ua-mobile':'?1','sec-ch-ua-model':'"vivo 2006"','sec-ch-ua-platform':'"Android"','sec-ch-ua-platform-version':'"12.0.0"','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36','x-asbd-id':'359341','x-csrftoken':'zaThv5kcLZ2uAAcyN5aIA4l076ik2KDq','x-ig-app-id':'1217981644879628','x-ig-www-claim':'hmac.AR3XlqS8iJaWE9DlwYzKhsNYFcycVkD_S8lvX8FSjiSZQNk-','x-requested-with':'XMLHttpRequest','x-web-session-id':'v7mjjo:9bff1n:ijoiob'};F=D.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/',cookies=C,headers=E);G=F.json();B=G['form_data']['username'];A(f"[=] Successfully Logged In As {B}");return B
W=['https://i.pinimg.com/550x/35/3f/c5/353fc517a4f4fac8d9ecfc734818e048.jpg','https://i.pinimg.com/236x/c1/43/43/c1434392c4c11ac42b782e9397eb2b58.jpg','https://i.pinimg.com/originals/0f/42/27/0f42279ce48796e63c920ba9aa0295a2.jpg','https://i.pinimg.com/236x/bf/8d/0d/bf8d0d9df86c121ad4e9ed65b4bb92cb.jpg']
def X(sessionid,url):
	B=D.Session();F={'mid':'aA_YVwABAAHMFelpsm6Zs8wkuuw-','datr':'V9gPaPnL8wt2M_S2mqnwU2FX','ig_did':'0EC39966-48EA-4407-9995-D8AEF68E7D82','csrftoken':'zaThv5kcLZ2uAAcyN5aIA4l076ik2KDq','dpr':'3.69307279586792','ig_nrcb':'1','wd':'796x1554','sessionid':sessionid,'ds_user_id':'1783073644','rur':'"FRC\\0541783073644\\0541777406062:01f77511d80f593ece8abe7f3cd927354a0afa425d1c6b83e6a7b9034168fa65ef3b1762"'};G={'authority':'www.instagram.com','accept':'*/*','accept-language':'en-US,en;q=0.9','origin':'https://www.instagram.com','referer':'https://www.instagram.com/accounts/edit/','sec-ch-prefers-color-scheme':'dark','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36','x-asbd-id':'359341','x-csrftoken':F['csrftoken'],'x-ig-app-id':'936619743392459','x-ig-www-claim':'hmac.AR1kELPSR2wNyOFRoc-koDmpUfyqdVmJxZQgg9VPV8d92vTs','x-instagram-ajax':'1022292862','x-requested-with':'XMLHttpRequest','x-web-session-id':'i0bflx:9xzg36:gxnv5m'};B.cookies.update(F);B.headers.update(G)
	try:
		C=D.get(url)
		if C.status_code==200:
			H=C.content;J={'profile_pic':('profile.jpg',H,'image/jpeg')};E=B.post('https://www.instagram.com/api/v1/web/accounts/web_change_profile_picture/',files=J)
			if E.ok:A('[+] Profile picture changed successfully!')
			else:A(f"[-] Failed to change profile picture: {E.status_code}");A(E.text)
		else:A(f"[-] Failed to download image: {C.status_code}")
	except I as K:A(f"[!] Error: {K}")
def Y():
	A('[=] Choose login method:');A('[1] Login via sessionid');A('[2] Login via username and password');C=E('[+] Choose Your Login Method: ').strip()
	if C=='1':B=E('[+] Enter your Instagram sessionid: ').strip();D=V(B)
	elif C=='2':D=E('[+] Enter your Instagram username: ').strip();G=E('[+] Enter your Instagram password: ').strip();B=U(D,G)
	else:A('[!] Invalid input. Please enter 1 or 2.');return
	F=0
	while F<200:
		F+=1
		for H in W:X(B,H)
if __name__=='__main__':Y()


#Developer @sunyhx If You Edit Or Sell This Tool Your Mom Is A Prostitute 😂