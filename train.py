from parse_in import generate_sample, check_for_new_files
import numpy as np
from normalize import encode_sequences
from keras.models import load_model
from sklearn.model_selection import train_test_split
from keras.callbacks import TensorBoard


def pre_train(in_out):
	if check_for_new_files():	
		sample = np.array(generate_sample())
		train, test = train_test_split(sample, test_size=0.1, random_state=12) 
		print("moooo")
		print(in_out.get("in_data"))
		trainX = encode_sequences(in_out.get("in_data"), 3, train[:, 0])
		trainY = encode_sequences(in_out.get("out_data"), 2, train[:, 1])

		testX = encode_sequences(in_out.get("in_data"), 3, test[:, 0])
		testY = encode_sequences(in_out.get("out_data"), 8, test[:, 1])

		model = load_model('model.h5')

		num_epochs = 500
		history = model.fit(trainX, trainY.reshape(trainY.shape[0], trainY.shape[1], 1), epochs=num_epochs, batch_size=256, validation_split=0.1, callbacks=[tensorboard], verbose=1)
		#model.save('model.h5')