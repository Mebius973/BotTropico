from stable_baselines3 import PPO

from tropicoEnv import TropicoEnv

env = TropicoEnv()

model = PPO(
    "CnnPolicy",
    env,
    verbose=1
)

model.learn(total_timesteps=100000)

model.save("tropico_ai")