<h1 align="center">Mario AI</h1>
This genetic algorithm learns through trial and error to complete levels from Super Mario Bros. During testing, completion of level 1-1 was achieved in around 30 minutes when starting from scratch.

## How does it work?
The algorithm was built with python. Super Mario Bros was emulated with the [OpenAI Gym](https://github.com/openai/gym) enviroment [gym-super-mario-bros](https://github.com/Kautenja/gym-super-mario-bros).

I decided not to use any existing machine learning frameworks for this project, and instead opted to create my own genetic algorithm from scratch. As Super Mario Bros levels are predictable and contain no randomness, image recognition was not necessary for a successful algorithm.

## How does it learn?

The AI learns by playing the level over and over until the flagpole is reached. Attempts are divided into generations, with each generation containing 30 attempts.
For this algorithm, each move has a

## Generation 0
Does random moves, lays the foundation for the AI to learn and improve from

## Generations 1-5
Gets stuck at pipe

## Generations 5-10
Gets stuck at other pipe

## Generations 15-20
Gets over most difficult pipes, learns to beat level

## Why?
