import dependencies

import asyncio
import json
import pickle
import tweepy

from config import Tokens
from twitchio.ext import commands

token = Tokens()
auth = tweepy.OAuthHandler(token.auths['API_KEY'],token.auths['API_KEY_SECRET'])
auth.set_access_token(token.auths['ACCESS_TOKEN'],token.auths['ACCESS_TOKEN_SECRET'])
twitter = tweepy.API(auth)
twitter_account = token.auths['TWITTER_HANDLE']
class LengthError(Exception):
    pass

class TweetDeleted(Exception):
    pass

class Bot(commands.Bot):
    def __init__(self, twitchChannels):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=token.auths['TWITCH_OAUTH'], prefix='?', initial_channels=twitchChannels)
        
    async def event_ready(self):
        print(f'Logged in as: {self.nick}')
        print(f'User id is: {self.user_id}')
        print(f'Connected to: {self.connected_channels}')
    
    async def event_message(self, message):
        try:
            data = message.tags
            channelinfo = await self.fetch_channel(data['room-id'])
            streamerName = channelinfo.user.name
            rewardID = data['custom-reward-id']
            display_name = data['display-name']
            rewards = {"Test":"12345"}
            with open("rewards.txt", "wb") as file: pickle.dump(rewards, file)
            rewards = pickle.loads(open('rewards.txt', 'rb').read())
            if streamerName in rewards: 
                pass
            else:
                print("\nREWARDID SET!")
                rewards[streamerName] = rewardID
                with open("rewards.txt", "wb") as file: pickle.dump(rewards, file)
            if rewardID == rewards[streamerName]:
                post = message.content
                if len(post) > 174:
                    raise LengthError
                else:
                    post += f"\n\n This message was tweeted by {display_name} @ https://www.twitch.tv/{streamerName}"
                    twitter.update_status(post) 
                    print(f"{display_name} Just tweeted @{streamerName}")
        except LengthError:
            chan = self.get_channel(streamerName)
            loop = asyncio.get_event_loop()
            loop.create_task(chan.send("Tweet is too long, it will not be sent!"))
            print("Length Error invoked!")
        except:
            print(end="")
        await self.handle_commands(message)