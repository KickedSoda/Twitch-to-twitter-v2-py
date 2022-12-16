class Tokens:
    auths = {}
    def __init__(self):
        r = open('stuff.txt', 'r')
        data = r.read()
        if data == "":
            API_KEY = input("Enter in your Twitter API KEY:").strip()
            while len(API_KEY) != 25:
                print("Input only accepts real tokens!")
                API_KEY = input("Enter in your Twitter API KEY:").strip()
            API_KEY_SECRET  = input("Enter in your Twitter API KEY SECRET:").strip()
            while len(API_KEY_SECRET) != 50:
                print("Input only accepts real tokens!")
                API_KEY_SECRET  = input("Enter in your Twitter API KEY SECRET:").strip()
            ACCESS_TOKEN = input("Enter in your Twitter ACCESS TOKEN:").strip()
            while len(ACCESS_TOKEN) != 50:
                print("Input only accepts real tokens!")
                ACCESS_TOKEN = input("Enter in your Twitter ACCESS TOKEN:").strip()
            ACCESS_TOKEN_SECRET = input("Enter in your Twitter ACCESS TOKEN SECRET:").strip()
            while len(ACCESS_TOKEN_SECRET) != 45:
                print("Input only accepts real tokens!")
                ACCESS_TOKEN_SECRET = input("Enter in your Twitter ACCESS TOKEN SECRET:").strip()
            TWITCH_OAUTH = input("Enter in your TWITCH BOT'S OAUTH TOKEN:").strip()
            TWITCH_NAME = input("Enter in THE your STREAMERS NAME:").strip()
            TWITTER_HANDLE = input("Enter the TWITTER BOTS @:").strip()
            self.auths['API_KEY'] = API_KEY
            self.auths['API_KEY_SECRET'] = API_KEY_SECRET
            self.auths['ACCESS_TOKEN'] = ACCESS_TOKEN
            self.auths['ACCESS_TOKEN_SECRET'] = ACCESS_TOKEN_SECRET
            self.auths['TWITCH_OAUTH'] = TWITCH_OAUTH
            self.auths["TWITCH_NAME"] = TWITCH_NAME
            self.auths['TWITTER_HANDLE'] = TWITTER_HANDLE
            w = open('stuff.txt', 'w')
            w.write(f"{API_KEY} {API_KEY_SECRET} {ACCESS_TOKEN} {ACCESS_TOKEN_SECRET} {TWITCH_OAUTH} {TWITCH_NAME} {TWITTER_HANDLE}")
            self.firsttime = True
        else:
            tokens = data.split(' ')
            self.auths['API_KEY'] = tokens[0]
            self.auths['API_KEY_SECRET'] = tokens[1]
            self.auths['ACCESS_TOKEN'] = tokens[2]
            self.auths['ACCESS_TOKEN_SECRET'] = tokens[3]
            self.auths['TWITCH_OAUTH'] = tokens[4]
            self.auths["TWITCH_NAME"] = tokens[5]
            self.auths['TWITTER_HANDLE'] = tokens[6]
            self.firsttime = False
        
    def clear_keys(self):
        w = open('stuff.txt', 'w')
        print("API KEYS AND TWITCH INFO CLEARED!\n")
        w.close()
        return
        
    def clear_id(self):
        w = open('rewardID.txt', 'w')
        print("REWARD ID CLEARED\n")
        w.close()
        return
        