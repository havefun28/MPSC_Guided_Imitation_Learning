import gym
from mpc import MPC
import numpy as np
env = gym.make('CartPole-v0')
#env.env.theta_threshold_radians = np.pi * 2
#env.env.x_threshold = 5 

start_theta = 0#-np.pi + 0.4# + 0.1#2 * np.pi #np.pi+0.4

mpc = MPC(0.5,0,start_theta,0) 
for i_episode in range(1):
    observation = env.reset()
    #env.env.state[2] = start_theta - np.pi
    action = 0
    for t in range(500):
        env.render()
        #action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        print(observation, reward, done, info)
        a = mpc.update(observation[0] , observation[1], observation[2]+np.pi, observation[3])
        #env.env.force_mag = abs(a) #min(100, abs(a))
        if a < 0:
        	action = 0
        else:
        	action = 1
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
