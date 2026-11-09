import time

cancion = [
    {"texto": "I Wanna Da-💃", "espera": 0.5},
    {"texto": "i Wanna Dance In the Lights", "espera": 2.6},
    {"texto": "I Wanna Ro-", "espera": 1},
    {"texto": "I Wanna Rock Your Body", "espera": 3.3},
    {"texto": " I Wanna Go-", "espera": 1},
    {"texto": "I Wanna Go For a Ride", "espera": 2.},
    {"texto": "Hop in the Music", "espera":1.3},
    {"texto": "And Rock Your Body", "espera": 3.3},
    {"texto": "RIGHT", "espera":0.0},
    {"texto": "Rock Your Body", "espera":0.9},
    {"texto": "Common", "espera":0.0},
    {"texto": "Common", "espera":0.2},
    {"texto": "ROCK THAT BODY", "espera":0.8},
    {"texto": "ROCK THAT BODY", "espera": 0.8},
    {"texto": "ROCK YO' BODY", "espera": 1},
    {"texto": "Rock Your Body", "espera":0.9},
    {"texto": "Common", "espera":0.0},
    {"texto": "Common", "espera":0.2},
    {"texto": "ROCK THAT BODY", "espera":0.8},
    {"texto": "ROCK THAT BODY", "espera": 0.8},
    {"texto": "ROCK YO' BODY", "espera": 1},


   

   ]

for parte in cancion :
     print (parte ["texto"])
     time.sleep(parte["espera"])