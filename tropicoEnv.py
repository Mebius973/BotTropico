import gymnasium as gym
from gymnasium import spaces
import numpy as np

from actions import perform_action
from readScreen import get_observation
from reward import compute_reward

class TropicoEnv(gym.Env):

    def __init__(self):
        super().__init__()

        self.action_space = spaces.Discrete(4)

        self.observation_space = spaces.Box(
            low=0,
            high=255,
            shape=(90,160,3),
            dtype=np.uint8
        )

    def reset(self, seed=None, options=None):

        observation = get_observation()
        return observation, {}

    def step(self, action):

        perform_action(action)

        observation = get_observation()

        reward = compute_reward()

        done = False

        return observation, reward, done, False, {}