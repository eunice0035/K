from gtts import gTTS
import os 
import argparse
import random

language = 'en'
captcha_symbols="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
save_dir = "audio_valid"

for i in range(1000):
	captcha_text = ''.join([random.choice(captcha_symbols) for j in range(8)])
	myobj = gTTS(text=captcha_text, lang=language, slow=False)
	myobj.save(os.path.join(save_dir, captcha_text +'.wav'))

