import gym
import time
from rlalgs.algos.vpg.vpg import vpg
from rlalgs.utils.logger import setup_logger_kwargs
from rlalgs.utils.preprocess import preprocess_pong_image

env = "Pong-v0"
training_steps = int(4e7)
batch_size = 5000       # > average complete episode length
epochs = int(training_steps/batch_size)
exp_name = "vpg_pong"
seed = 30
logger_kwargs = setup_logger_kwargs(exp_name, seed=seed)

params = {
    "epochs": epochs,
    "batch_size": batch_size,
    "hidden_sizes": [100, 50, 25],
    "pi_lr": 0.0007,        # the karpathy constant
    "v_lr": 0.0007,
    "gamma": 0.99,
    "seed": seed,
    "render": False,
    "render_last": True,
    "logger_kwargs": logger_kwargs,
    "save_freq": int(epochs/10),
    "overwrite_save": False,
    "preprocess_fn": preprocess_pong_image,
    "obs_dim": 80*80
}

print("\nStarting Pong training using VPG")
start_time = time.time()
print("Start time = {}\n".format(start_time))
vpg(lambda: gym.make(env), **params)
end_time = time.time()
print("\nEnd time = {}\n".format(end_time))
print("Total training time = {}\n".format(end_time - start_time))
