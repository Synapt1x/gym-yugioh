# gym-yugioh

This openAI gym environment defines the operation of stepping through a
Yu-Gi-Oh! duel. This can be a multi-agent or single-agent domain with discrete
state and action spaces.

## Background

Yu-Gi-Oh! is a trading card game originally developed by Konami in 1999 that is
based on the game of Duel Monsters as part of the *Yu-Gi-Oh!* series originating
in 1996. More information can be viewed [here](https://en.wikipedia.org/wiki/Yu-Gi-Oh!_Trading_Card_Game).

## Goals

The goal of developing this environment is to develop agents that are able to
learn how to play through duels to win, particularly under varying conditions:

* using meta-learning to adapt strategies and side-decking cards as necessary,
* adjusting playstyle to adapt to the opponents' playstyle,
* developing novel strategies and card combos,
* designing novel decks and strategies to achieve better dueling results.

## Getting Started

Using this environment will mirror the instructions outlined by openAI gym
[here](https://github.com/openai/gym).

### Prerequisites

In order for this environment to run the following packages are required:

```
gym
pytest
```

### Installing

To install the environment the following is sufficient to run from root:

```
pip install -e gym-yugioh
```
and then creation of the environment to train and run the environment can be
achieved as follows:

```
gym.make('gym_yugioh:yugioh-v0')
```
for the standard difficulty duel environment, or

```
gym.make('gym_yugioh:yugioh-extrahard-v0')
```
for the more difficult duel environment.

## Testing

If you wish to ensure the package is fully functional and that additional
features that are added do not introduce breaks in the overall structure of the
code, pytests can be run as follows:

```
pytest tests
```

## Contributing

TBD

## Versioning

SemVer is used for formatting version numbersFor the versions available, see the tags on this repository.

## Authors

* **Chris Cadonic** - *Initial work* - [github_page](https://github.com/Synapt1x)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

I have to thank openAI gym for providing a framework that enables one to add
custom environments such as the one developed herein.

I also have to thank Konami for developing such a finely-crafted trading card
game that introduces a varied and incredibly complex game that continues to
improve and maintain itself as an interesting problem to solve for an RL agent.
