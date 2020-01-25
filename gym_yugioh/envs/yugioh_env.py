"""
Standard Yu-Gi-Oh! environment enabling experimentation with RL agents that are
able to learn how to play the game. This is specifically achieved through the
use of openAI gym to set up the environment.

This standard difficulty will evolve as the project and environment's
development progress.
"""


import gym
from gym import error, spaces, utils
from gym.utlis import seeding

import logging
logger = logging.getLogger(__name__)


class YugiohEnv(gym.Env):
    """
    Standard difficulty Yu-Gi-Oh! environment.
    """
    metadata = {'render.modes': ['human']}

    def __init__(self):
        pass

    def step(self, action):
        """
        Evolve the state of the duel a single step forward.
        """

        pass

    def reset(self):
        """
        Reset the duel to an initial state.
        """

        pass

    def render(self, mode='human'):
        """
        Visualize the current state of the duel.
        """

        pass

    def close(self):
        """
        Finish the duel in its current state and empty the current context as
        necessary.
        """

        pass

