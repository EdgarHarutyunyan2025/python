#nkar qasel url hasceov

#import requests
#img_url='nkari url hascen'
#response=requests.get(img_url)
#with open('image.png','wb') as f:
#    f.write(response.content)



#$request moduli mijocov gtnel nkar terminali mej nshelov nkari anun@ ev qanak@

#import requests
#import json

#def download(q:str,p:str):
#    header={"Authorization":"N09Vg1rSY7Oz2yaEWCVj9DmPHSM9s729vlSr3AZt1IDIz7xVfM8CAPA3"}
#    i=1
#    while i<=int(p):
#        i+=1
#        url=f"https://api.pexels.com/v1/search?query={q}&per_page={i}"
#        r=requests.get(url,headers=header)
#        if r.status_code==200:
#            _r=r.json()
#            print(_r)
#            for itemes in _r.get("photos"):
#                print(itemes.get("url"))  
#    else:
#        print(r.text)


#def main():
#    q=input('query ')
#    p=input('count page  ')
#    download(q,p)

#main()