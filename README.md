
# Mutual Brainwave Lab Visuals

The visualization app is currently in development. The Mutual Brainwave neurogame gives a visual feedback when the
correlation score of the two players reaches a certain threshold, represented by the two heads overlapping when the value is close to 1.
While the threshold is above 0.90, the players score points.

To run the current application, please refer to the installation guide of [HybridHarmony](https://github.com/RhythmsOfRelating/HybridHarmony/blob/master/README.md) 
to set up Python and pipenv on your machine.
Then open a command console (CMD / Terminal / Git Bash) in the root folder of Mutual Brainwave Lab Visuals and run the following command:

`pipenv install`

or eventually if your installation of pipenv is not available globally:

`python37 -m pipenv install`

Then simply run the following command to start the app:

`python37 main.py`

The app expects an LSL stream called "RValues" that can be generated or opened using [HybridHarmony](https://github.com/RhythmsOfRelating/HybridHarmony)

## Development Roadmap ##
The app is currently under development and as it is, it will just start running without any possibility to change configurations.
The following features are WIP and will be released in the order presented

- [IMPL] Basic GUI with head placeholders
- [IMPL] LSL data receiver
- [IMPL] Multi-threading of the receiver process
- [IMPL] Visual update based on the RValues
- [IMPL] Score system
- [WIP] Adjustable view settings
- [WIP] Adjustable game settings
- [WIP] Adjustable window size
- [WIP] OSC data receiver
- [WIP] Calibration scene
- [WIP] Smoothing animations
- [WIP] Advanced game scenarios
