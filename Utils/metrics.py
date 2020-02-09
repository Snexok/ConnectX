from kaggle_environments import evaluate
def mean_reward(rewards):
    return sum(r[0] for r in rewards) / sum(r[0] + r[1] for r in rewards)
def mean_reward_with_enemy(agent, enemy, num_episodes=10):
    print("My Agent vs Random Agent:", mean_reward(evaluate("connectx", [agent, enemy], num_episodes=num_episodes)))