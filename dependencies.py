import sys
import subprocess
try:     
    import tweepy 
    from twitchio.ext import commands
except:
    print("Dependencies not found, installing now!")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'twitchio'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'tweepy'])