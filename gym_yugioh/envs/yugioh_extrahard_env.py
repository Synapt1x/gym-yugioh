"""
Hard Yu-Gi-Oh! environment enabling experimentation with RL agents that are
able to learn how to play the game. This is specifically achieved through the
use of openAI gym to set up the environment.

This extra hard difficulty will evolve as the project and environment's
development progress.
"""


import gym
from gym import error, spaces, utils
from gym.utlis import seeding

import logging
logger = logging.getLogger(__name__)


class YugiohExtraHardEnv(gym.Env):
    """
    Extra hard difficulty Yu-Gi-Oh! environment.
    """
    metadata = {'render.modes': ['human']}

    def __init__(self, **kwargs):

        self.game = Engine(**kwargs)

    def step(self, action):
        """
        Evolve the state of the duel a single step forward.
        """

        self.game.play_card()

    def reset(self):
        """
        Reset the duel to an initial state.
        """

        self.game.reset()

    def render(self, mode='human'):
        """
        Visualize the current state of the duel.
        """

        self.game.visualize()

    def close(self):
        """
        Finish the duel in its current state and empty the current context as
        necessary.
        """

        self.game.finish()

