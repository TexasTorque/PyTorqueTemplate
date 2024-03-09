# PyTorqueTemplate

Template used for creating a Python project within [FRC 1477, Texas Torque](https://texastorque.org/).

## Using the template

- Create a repository for your project by clicking 'Use this template' on GitHub
- Clone the repository using `git clone [url] --recursive`
- Install RobotPy (if you haven't already)
- Run `py -3 -m robotpy sync` on project creation

## Installing RobotPy

Installing RobotPy currently requires Python 3.12 to be installed on your system, which can be installed from [here](https://www.python.org/downloads/).

On Windows:
- Make sure `py -3 --version` outputs 3.12.x
- Run `py -3 -m pip install robotpy` to install RobotPy

On macOS / Linux:
- Linux requires pip version 20.3 or newer
- Make sure `python3 --version` outputs 3.12.x
- Run `python3 -m pip install robotpy` to install RobotPy

## Deploying code

To deploy code simply run `py -3 -m robotpy deploy` (or the equivalent) in the project directory

## Authors

- [Davey Adams](https://www.github.com/humandavey) (2022-2025)