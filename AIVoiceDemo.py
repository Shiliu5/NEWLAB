import keras
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# 定义模型
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(mfcc.shape[0], mfcc.shape[1], 1))) 
model.add(MaxPooling2D(pool_size=(2, 2))) model.add(Conv2D(64, (3, 3), activation='relu')) 
model.add(MaxPooling2D(pool_size=(2, 2))) 
model.add(Flatten()) model.add(Dense(128, activation='relu')) 
model.add(Dense(1))

#编译模型
model.compile(optimizer='adam', loss='mse')

#训练模型
model.fit(X_train, y_train, batch_size=32, epochs=100)

#进行声音克隆
output = model.predict(input_mfcc)

#播放声音输出
import pyaudio import numpy as np
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)
stream.write(np.float32(output))
stream.stop_stream() stream.close()
p.terminate()
