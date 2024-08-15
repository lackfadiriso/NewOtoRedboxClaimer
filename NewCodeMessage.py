import string, asyncio, time, random, pyautogui, webbrowser,pyperclip, socket, ctypes, os
import tkinter as tk
from tkinter import messagebox
from bilgilerim import binance_username, binance_password
from telethon import TelegramClient, events



#İnternet kontrolü
def check_wifi():
    try:
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False
   
def aç():
    openImage = pyautogui.locateOnScreen('open.png')
    if openImage is not None:
        open_merkez = pyautogui.center(openImage)
        pyautogui.sleep(1)
        pyautogui.moveTo(open_merkez.x, open_merkez.y)
        pyautogui.click()
    else:
        raise pyautogui.ImageNotFoundException("Resim bulunamadı.")

#Telegram
api_id = 'Api id'
api_hash = 'Telegram Api Hash'
target_chats = ['XCOINBOXES', 'panda_task' ,'KingBX', 'bqbox', 'abemav', 'rsbox', 'Crypto_Box_Code_Binance', 'UnlimitedBinanceBoxes', 'Chat_CryptoBoxSuper',
                'Luckyboxs', 'SHN_Crypto', 'BARISYILDIZ_live', 'BIGBOCSESSS', 'crypto_box_free_binance', 'hotchatcrypto', 'freec24', 'hitcryptoworld', 'Token_Boxes',
                'SOHBETLiMM', 'Binance_global_red_box', 'sheikhbdbox_chat', 'Crypto_box_07', 'hitcryptoworld', 'binanceboxi', 'redboxbinance1', 'Th3GR34T']

client = TelegramClient('session_name', api_id, api_hash)

#siteyi açmak
def opensite():
    url = "https://www.binance.com/en/my/wallet/account/payment/cryptobox"
    webbrowser.open(url)

root = tk.Tk()
root.withdraw()

messagebox.showwarning("UYARI!", "UYGULAMA BAŞLATILDI LÜTFEN BİNANCE AÇILINCA ELEMEYİNİZ. \n THE APPLICATION HAS STARTED. PLEASE DO NOT CLOSE WHEN BINANCE OPENS.")

opensite()
@client.on(events.NewMessage(chats=target_chats))
async def handle_new_message(event):
    message = event.message
    messages = client.get_messages(target_chats, limit = None)
    if len(message.text) == 8:
        if message.text == message.text.upper():
            if message.text.isalnum():
                kopyala = pyperclip.copy(message.text)
                #bugları düzeltmek için zorunlu
                pyautogui.click(1166, 177)
                pyautogui.click(1163, 267)
                #-------------------------------#
                time.sleep(1)
                pyautogui.moveTo(1127, 525)
                pyautogui.click()
                pyautogui.click(1251, 512)
                pyautogui.sleep(1)
                pyautogui.click(1159, 639)
                pyautogui.sleep(2)
                aç()
                time.sleep(random.randrange(2,3))

                
                

            else:
                print("özel karakter içeriyor")
        else:
            print("küçük harf içeriyor")
    else:
        print("8 Harf Ve Rakamdan Küçük veya Uzun ")

async def main():
    await client.start()
    me = await client.get_me()
    print(f"Oturum açıldı: {me.first_name}")

    # İstemciyi çalışır durumda tutma
    await client.run_until_disconnected()

# Ana işlevi çağırma
if check_wifi() == True:
    # Uyku modunu engelle
    ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bye Bye...👋")
else:
    print ("İnternet Bağlantısı Yok, Lütfen Daha Sonra Tekrar Deneyiniz 😔😯")
