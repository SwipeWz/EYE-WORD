from pyrogram import Client
import os
import time,requests as legendx
from pyrogram.raw.functions.account import CheckUsername
import asyncio,string,random
api_id =   # Your API ID
api_hash = ' '  #Your API HASH
os.system("cls")
print("""
                   \\
                    \\
     \\\\\__________\\\\\
      \  _______   o   _\\
   --  \\   o   \_____/ ||  
     __ \\_______//______||  
    /              //      \  
   /__________    //  |   | \  
  /   _|_   _|  //   |   |  \  
 /___________   //    |   |   \  
|__[X]__[X]___/||     |   |____\
               ||     |   |    ||
               ||     |   |    ||
DDW ORGANIZATION
Created by @SwipeWz
""")



bot=input("\033[93m Ingrese el token de Telegram Bot para reenviar todos los nombres de usuario válidos a su cuenta- \033[0m")
userid=int(input("\033[93m Coloca tu USER ID de Telegram:- \033[0m"))

with Client("admin", api_id=api_id, api_hash=api_hash) as app:
    while True:
        DDWORGANIZATION = 'aeiou'
        DDWORG = 'bcdfghjklmnpqrstvwxyz'
        length=5
        length = max(length, 2)
        syllables = [random.choice(legendxdied) + random.choice(DDWORGANIZATION) for _ in range(length // 2)]
        if length % 2 == 1:
            syllables.append(random.choice(legendxdied))
        random_word = ''.join(syllables)
        time.sleep(1)
        print(f"\033[94m Using {random_word}")
        try:
            legendxdied=app.invoke(CheckUsername(username=f"{random_word}"))
        
            if ddworg==True:
                print(f"\033[92m {random_word} bot en cursot")
                text=f"@{random_word} EL Nombre de usuario de telegram es valido."
                api_url = f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={userid}&text={text}"
                legendx.get(api_url)
            else:
                print("\033[91m {random_word} Intente con otro")
        except Exception as e:
            print(f"\033[91m{e}")
