#! /usr/bin/python3
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

env = gym_super_mario_bros.make('SuperMarioBros-1-1-v0')
env = JoypadSpace(env, SIMPLE_MOVEMENT)
done = True

t = 0
def print_info(info, reward):
	global t 
	t += 1
	if not t % 100:
		print(info, reward)

for step in range(5000):
	if done:
		state = env.reset()
	action = env.action_space.sample()
	state, reward, done, info = env.step(env.action_space.sample())
	print_info(info, reward)
	env.render()
	
env.close()
