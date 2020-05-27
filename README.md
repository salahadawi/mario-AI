<h1 align="center">Mario AI</h1>
<p align="center">
    <img src="https://github.com/salahadawi/mario-AI/blob/master/images/mario_flag_get.gif">
</p>
This genetic algorithm learns through trial and error to complete levels from Super Mario Bros. During testing, completion of level 1-1 was achieved in around 30 minutes of training when starting from scratch.

## How does it work?
The algorithm was built with python. Super Mario Bros was emulated with the [OpenAI Gym](https://github.com/openai/gym) enviroment [gym-super-mario-bros](https://github.com/Kautenja/gym-super-mario-bros).

I decided not to use any existing machine learning frameworks for this project, and instead opted to create my own genetic algorithm from scratch. As Super Mario Bros levels are predictable and contain no randomness, image recognition was not necessary for a successful algorithm.

## How does it learn?

The AI learns by playing the level over and over until the flagpole is reached. Attempts are divided into generations, with each generation containing 30 attempts. Each attempt is called an [agent](https://en.wikipedia.org/wiki/Software_agent). Each agent is given a fitness score, corresponding to how far right the agent was able to move in the level.

Once each agent from a generation has completed its run, the agent with the highest fitness score is chosen, and the next generation of agents will base their movements of the chosen agents moves.

As level 1-1 does not contain any dead-ends

For this algorithm, each move has a


Each frame, the AI randomly chooses an action.
The available actions are:

* Do nothing

* Move right

* Move right and press A

* Move right and press B

* Move right and press A and B

A button jumps, B button makes Mario run instead of walk.

## Generation 0
The AI starts its learning process from generation 0. Having no previous input to work with, the AI attempts to complete the level by doing random actions each frame. Once 30 attempts have been made and the generation is over, the sequence of inputs that ac
Does random moves, lays the foundation for the AI to learn and improve from

## Generations 1-5
Gets stuck at pipe

## Generations 5-10
Gets stuck at other pipe

## Generations 15-20
Gets over most difficult pipes, learns to beat level

## Why?
