from stable_baselines3 import PPO

from tropicoEnv import TropicoEnv


model = PPO.load("tropico_ai")

env = TropicoEnv()

obs, _ = env.reset()

while True:

    action, _ = model.predict(obs)

    obs, reward, done, _, _ = env.step(action)