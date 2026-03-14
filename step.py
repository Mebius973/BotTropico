from actions import perform_action
from readScreen import get_observation
from reward import compute_reward

def step(action):

    perform_action(action)

    observation = get_observation()

    reward = compute_reward()

    done = False

    return observation, reward, done