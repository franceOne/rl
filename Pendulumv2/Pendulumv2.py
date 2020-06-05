import numpy as np
import random
from IPython.display import clear_output
from collections import deque
import progressbar
from SimpleQLearning import Agent
import Training
import gym
import tensorflow as tf
from tensorflow.keras import Model, Sequential
from tensorflow.keras.layers import Dense, Embedding, Reshape
from tensorflow.keras.optimizers import Adam


enviroment = gym.make("CartPole-v0").env
enviroment.render()

print('Number of states: {}'.format(enviroment.observation_space))
print('Number of actions: {}'.format(enviroment.action_space))


optimizer = tf.keras.optimizers.SGD(learning_rate=0.0001, momentum=0.9)

loss =  tf.keras.losses.CategoricalCrossentropy()
agent = Agent(enviroment, optimizer, loss)

batch_size = 128
num_of_episodes = 500
agent.q_network.summary()


print("Train")
Training.train(enviroment, agent, batch_size, num_of_episodes)
print("RUN")
Training.runModel(enviroment, agent, 100)