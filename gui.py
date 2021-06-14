from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from main import main_neuro
import pickle

def check_paths(path):
	with open('path_data.pickle', 'rb') as f:
		data = pickle.load(f)
	return(data.get(path))

def choose_file():
	file = askopenfilename()
	return file

def choose_directory():
	return askdirectory()

def choose_lyrics_path():
	global lyricsPath
	lyricsPath = choose_file()
	with open('path_data.pickle', 'wb') as f:
		pickle.dump({"lyricsPath": lyricsPath, "savePath": savePath, "trainPath": trainPath, "preTrain": preTrain.get()}, f)
	chosen_lyrics_path_label['text'] = lyricsPath
	if (lyricsPath):
		main_neuro()

def choose_save_path():
	global savePath
	savePath = choose_directory()
	with open('path_data.pickle', 'wb') as f:
		pickle.dump({"lyricsPath": lyricsPath, "savePath": savePath, "trainPath": trainPath, "preTrain": preTrain.get()}, f)
	chosen_save_path_label['text'] = savePath

def choose_train_path():
	global trainPath
	trainPath = choose_directory()
	with open('path_data.pickle', 'wb') as f:
		pickle.dump({"lyricsPath": lyricsPath, "savePath": savePath, "trainPath": trainPath, "preTrain": preTrain.get()}, f)
	chosen_train_path_label['text'] = trainPath

def choose_is_train():
	global preTrain
	with open('path_data.pickle', 'wb') as f:
		pickle.dump({"lyricsPath": lyricsPath, "savePath": savePath, "trainPath": trainPath, "preTrain": preTrain.get()}, f)

lyricsPath = check_paths("lyricsPath")
savePath = check_paths("savePath")
trainPath = check_paths("trainPath")

root = Tk()
root.geometry('500x360+{}+{}'.format(root.winfo_screenwidth()//2 - 410, root.winfo_screenheight()//2 - 250))

Tk().withdraw()

preTrain = IntVar()
preTrain.set(check_paths("preTrain"))

chosen_lyrics_path_label = Label()
chosen_save_path_label = Label(text=check_paths("savePath"))
chosen_train_path_label = Label(text=check_paths("trainPath"))

Label().pack()
Label(text="Choose file to add lyrics").pack()
Checkbutton(text="Train before generation", variable=preTrain, command=choose_is_train).pack()
Button(text="Choose file", width=20, command=choose_lyrics_path).pack()
Label().pack()
Label(text="You chose file:").pack()
chosen_lyrics_path_label.pack()
Label().pack()
Label(text="Save path:").pack()
chosen_save_path_label.pack()
Button(text="Change save path", width=20, command=choose_save_path).pack()
Label().pack()
Label(text="Path to train network:").pack()
chosen_train_path_label.pack()
Button(text="Change train path", width=20, command=choose_train_path).pack()

def on_closing():
	root.quit()
	root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()