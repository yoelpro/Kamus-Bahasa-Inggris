import json
from difflib import get_close_matches
data = json.load(open("data.json",'r'))

def ask(query):
    query=query.lower()
    if query in data:
        return data[query]
    else:
        if not get_close_matches(query,data.keys(),cutoff=0.8):
            return "Kata tidak dapat ditemukan"
        else:
            confirm = input(("Apakah yang anda maksud %s ? (Y/T)" % get_close_matches(query,data.keys(),cutoff=0.8)[0]))
            if (confirm.lower() == "y"):
                return data[get_close_matches(query,data.keys(),cutoff=0.8)[0]]
            elif (confirm.lower() == "n"):
                return "Kata tidak dapat ditemukan"
            else:
                return "Masukan tidak dimengerti"

while (True):
    word=input("Masukkan kata yang ingin anda cari: ")
    if word.lower() == "keluar":
        print("Terima kasih")
        break
    hasil = ask(word)
    if type(hasil) == list:
        for result in hasil:
            print(result)
    else:
        print(hasil)
    print("-----------------------------------------")
