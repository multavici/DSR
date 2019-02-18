#%%
import gym
import numpy as np

from gym.envs.registration import register
register(
    id='FrozenLakeNotSlippery-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4', 'is_slippery': False}
)

#%%
#env = gym.make('FrozenLake-v0')
env = gym.make('FrozenLakeNotSlippery-v0')

env.render()

#%%
def value_iteration(env, gamma=1.0):
    # initialize value table with zeros
    value_table = np.zeros(env.observation_space.n)
    # setting number of iterations and treshold
    num_iterations=100000
    treshold = 1e-20
    
    value_table_history = np.ndarray((1000,16))
    for i in range(num_iterations):
        updated_value_table = np.copy(value_table)

        for state in range(env.observation_space.n):
            Q_value = []
            for action in range(env.action_space.n):
                next_states_rewards = []
                for next_s in env.P[state][action]:
                    trans_prob, next_state, reward_prob, _ = next_s
                    next_states_rewards.append(
                        trans_prob * (reward_prob + gamma * updated_value_table[next_state]))
                Q_value.append(np.sum(next_states_rewards))

            value_table[state] = max(Q_value)
            value_table_history[i][state]

        if(np.sum(np.fabs(updated_value_table - value_table)) <= treshold):
            print(f'Value iteration converging at iteration: {i + 1}')
            break
    
    return value_table

#%%
def extract_policy(value_table, gamma=1.0):
    # initializing the policy table
    policy = np.zeros(env.observation_space.n)
    
    for state in range(env.observation_space.n):
        # initizalizing the Q_table for each state
        Q_table = np.zeros(env.action_space.n)
        
        # compute Q value for each action of the state
        for action in range(env.action_space.n):
            for next_s in env.P[state][action]:
                trans_prob, next_state, reward_prob, _ = next_s
                Q_table[action] += (trans_prob 
                    * (reward_prob + gamma * value_table[next_state]))
            
        # select the action that has the maximum Q-value for finding the optimal policy
        policy[state] = np.argmax(Q_table)
            
    return policy

#%%
optimal_value_function = value_iteration(env, gamma=0.9)
print(optimal_value_function.reshape(4,4))

#%%
policy = extract_policy(optimal_value_function, gamma=0.9)
print(policy)

#%%
d = {
    0: "←",
    1: "↓",
    2: "→",
    3: "↑",
}

s = []
for value in policy:
    s.append(d[value])

np.array(s).reshape(4,4)