#!/usr/bin/env python3
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# print(np, tf)
tf.keras.backend.set_floatx('float64')

npoints = 100000
x_sqr = 2 * np.random.random((npoints, 3)) - 1

x_circ = x_sqr[(x_sqr**2).sum(axis=1) <= 1].copy()
x_sqr = x_sqr[(x_sqr**2).sum(axis=1) > 1].copy()

my_activation = tf.keras.activations.sigmoid
inputs = tf.keras.Input(3)
Dense = tf.keras.layers.Dense(3, activation=my_activation)(inputs)
for _ in range(3):
    Dense = tf.keras.layers.Dense(3, activation=my_activation)(Dense)
#
outputs = tf.keras.layers.Dense(3, activation=tf.keras.activations.linear)(Dense)
model = tf.keras.Model(inputs=inputs, outputs=outputs)
model.compile()

weights  = model.get_weights()

new_w = []
for w in weights:
    #w = w.clip(0.3, 2.0)
    w = np.random.normal(loc=0, scale=3, size=w.shape) #np.ones(w.shape)
    new_w.append(w)
#
print(new_w)
model.set_weights(new_w)

#plt.plot(x_sqr[:, 0], x_sqr[:, 1], '.', ms=0.3)
#plt.plot(x_circ[:, 0], x_circ[:, 1], '.', ms=0.3)
#plt.show()
y_sqr = model.predict(x_sqr)
y_circ = model.predict(x_circ)
#plt.plot(y_sqr[:, 0], y_sqr[:, 1], '.', ms=0.3)
#plt.plot(y_circ[:, 0], y_circ[:, 1], '.', ms=0.3)
#plt.show()

np.savetxt('in1.dat', x_sqr)
np.savetxt('in2.dat', x_circ)
np.savetxt('out1.dat', y_sqr)
np.savetxt('out2.dat', y_circ)

x0, x1 = x_circ.copy(), x_sqr.copy()

il = 0
np.savetxt('c' + str(il) + '.dat', x0)
np.savetxt('s' + str(il) + '.dat', x1)

for il, layer in enumerate(model.layers, start=1):
    x0 = layer(x0)
    x1 = layer(x1)
    np.savetxt('c' + str(il) + '.dat', x0)
    np.savetxt('s' + str(il) + '.dat', x1)
#