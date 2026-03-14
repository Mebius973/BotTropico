from tropicoEnv import TropicoSimEnv
env = TropicoSimEnv(world_model)
state = initial_state

for episode in range(num_episodes):
    done = False
    while not done:
        action = policy(state)
        next_state, reward = env.step(state, action)
        policy.update(state, action, reward, next_state)
        state = next_state