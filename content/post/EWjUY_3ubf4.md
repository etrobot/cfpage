
---
title: "Training an AI to Bowl in Unity"
date: 2023-07-30T09:05:19
draft: true
tags: ['Reinforcement Learning', 'PPO algorithm', 'Unity']
author: Frank
category: Efficiency
---

In this experiment, a reinforcement learning algorithm called PPO was used to train an AI agent to bowl in the Unity game engine. 

## The Goal
The goal was to create an AI that could knock down bowling pins efficiently by throwing the ball straight down the lane.

## The Agent
The agent was a ragdoll with 12 joints and 13 bones. It was given control over the angles of its joints to move its body.

## The Interface
The interface consisted of passing the agent information about the position, velocity and angles of its joints. The agent could then control the angles it tried to point its joints towards.

## The Reward System
A reward function was designed to incentivize the agent to:
- Keep the ball in the lane
- Throw the ball fast and straight
- Knock over pins

## The Training Process
Over several training sessions, the agent explored different strategies like flinging its body to launch the ball. But it often got stuck optimizing for only one aspect of the reward function. 

After tweaking the rewards to better align with the overall goal, the agent learned an efficient bowling motion and was able to knock down all the pins.

## Adding Spin Control
Open brain surgery was performed on the trained network to give it control over ball spin. With minor retraining, it learned to aim and control spin for even better bowling.

Overall, this experiment demonstrated the potential for using reinforcement learning to train AI agents to perform complex physical tasks like bowling in a simulated environment. The PPO algorithm proved effective at optimizing behaviors purely through trial-and-error experience.


### Reference:
AI Invents New Bowling Techniques:
{{< youtube EWjUY_3ubf4 allow_fullscreen>}}
        