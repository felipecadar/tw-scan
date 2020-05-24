import urllib, requests
import time, os, sys

def getAll():
    village_url = "https://br101.tribalwars.com.br/map/village.txt"
    village_data = urllib.parse.unquote_plus(requests.get(village_url).text)
    
    player_url = "https://br101.tribalwars.com.br/map/player.txt"
    player_data = urllib.parse.unquote_plus(requests.get(player_url).text)

    odd_url = "https://br101.tribalwars.com.br/map/kill_def.txt"
    odd_data = urllib.parse.unquote_plus(requests.get(odd_url).text)

    oda_url = "https://br101.tribalwars.com.br/map/kill_att.txt"
    oda_data = urllib.parse.unquote_plus(requests.get(oda_url).text)

    t = str(time.time())
    with open("tw/villages/" + t + ".txt", "w") as f:
        f.write(village_data)

    with open("tw/players/" + t + ".txt", "w") as f:
        f.write(player_data)

    with open("tw/odd/" + t + ".txt", "w") as f:
        f.write(odd_data)

    with open("tw/oda/" + t + ".txt", "w") as f:
        f.write(oda_data)


def job():
    print("I'm working...")

if __name__ == "__main__":

    if not os.path.exists("tw/villages/"):
        os.makedirs("tw/villages/")

    if not os.path.exists("tw/players/"):
        os.makedirs("tw/players/")

    if not os.path.exists("tw/odd/"):
        os.makedirs("tw/odd/")

    if not os.path.exists("tw/oda/"):
        os.makedirs("tw/oda/")
    
    getAll()
    
    if "1" in sys.argv:
        exit()

    import schedule
    schedule.every(2).hours.do(getAll)
    while True:
        schedule.run_pending()
        time.sleep(1)

    print("Stop!")