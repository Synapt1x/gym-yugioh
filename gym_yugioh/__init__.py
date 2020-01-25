from gym.envs.registration import register

register(
    id='yugioh-v0',
    entry_point='gym_yugioh.envs:YugiohEnv',
)
register(
    id='yugioh-extrahard-v0',
    entry_point='gym_yugioh.envs:YugiohExtraHardEnv',
)
