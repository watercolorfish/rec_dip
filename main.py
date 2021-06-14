from parse_in import parce_from
from parse_out import parce_to
from normalize import get_syllable
from train import pre_train
from keras.models import load_model
import pickle

def main_neuro():
	with open('path_data.pickle', 'rb') as f:
		data = pickle.load(f)
	with open('in-out_data.pickle', 'rb') as f:
		in_out = pickle.load(f)
	if (data.get("preTrain")):
		pre_train(in_out)
	parced_data = parce_from(data.get("lyricsPath"))
	model = load_model('model.h5')
	preds = model.predict_classes(in_out.get("in_enc"))
	export = list()
	for i in range(0, len(parced_data)):
		export.append([get_syllable(preds[i][0], in_out.get("out_date")), get_syllable(preds[i][1], in_out.get("out_date"))])
	parce_to(data.get("lyricsPath"), data.get("savePath"), export)