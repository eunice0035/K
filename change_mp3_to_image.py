import librosa
import librosa.display
import os
import numpy as np
import matplotlib.pyplot as plt

path ="audio_train"
save_dir = "audio_train_image"
file_list = os.listdir(path)
file_list_wav = [file for file in file_list if file.endswith(".wav")]

for i in file_list_wav:
	(file_dir, file_id) = os.path.split(i)
	#print("file_dir:", file_dir)
	print("file_id:", file_id)

	y, sr = librosa.load(os.path.join(path, i))

	plt.figure(figsize=(1.28, .64), dpi=100)

	plt.axes([0., 0., 1., 1., ], frameon=False, xticks=[], yticks=[])
	#time = np.linspace(0, len(y)/sr, len(y)) # time axis
	#fig, ax1 = plt.subplots()
	#ax1.plot(time, y, color = 'b', label='speech waveform')
	#ax1.set_ylabel("Amplitude") # y 축
	#ax1.set_xlabel("Time [s]") # x 축
	#plt.title(file_id) # title

	S = librosa.feature.melspectrogram(y, sr)
	librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
	plt.savefig(os.path.join(save_dir, os.path.splitext(file_id)[0] +'.png'), bbox_inches=None, pad_inches=0)
	plt.close()
