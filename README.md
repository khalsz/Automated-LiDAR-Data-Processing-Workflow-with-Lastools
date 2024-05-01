# Automated LiDAR Data Processing Workflow with Lastools
## Overview
This project aims to automate the processing of LiDAR (Light Detection and Ranging) data using Lastools, a suite of command-line tools for LiDAR data processing. The automated workflow includes various steps such as noise removal, ground classification, and canopy metric extraction, ultimately facilitating the analysis of forest canopy characteristics for biomass estimation.

## Project Structure
The project consists of several components organized into modules:

1. **Data Processing Modules**: These modules contain scripts and classes for executing specific tasks in the LiDAR data processing workflow.
    - **`DirectoryManager`**: Manages directories for storing processed LiDAR data.
    - **`ProcessParam`**: Represents parameters for performing LiDAR data processing.
    - **`LastoolCommands`**: Facilitates the execution of Lastools commands for data processing.
2. **Utility Modules**: These modules contain utility functions and classes used across the project.
    - **`commands`**: Defines Lastools commands and related functions.
    - **`process_runner`**: Implements functions for running subprocesses and handling errors.
3. **Configuration**: The config directory contains configuration files, including constant variables and YAML configuration for Lastools parameters.

## Usage
To use this automated LiDAR data processing workflow:

1. Clone the repository to your local machine.
2. Install the required dependencies. 
3. Configure the YAML file (`config.yaml`) with the desired parameters for Lastools processing.
4. Run the `extract_forest_metrics.py` script, providing the path to the directory containing the raw LiDAR data as an argument.
5. Monitor the execution of the automated workflow, which will perform noise removal, ground classification, canopy metric extraction, and other relevant processes.

## Requirements
Ensure you have the following dependencies installed:

- Python 3.x
- Lastools (download and install from the official website)

## Testing
Unit tests are provided to validate the functionality of the Lidar Forest Metrics Extractor. Run the tests using the following command: *test_lidar_forest_metric_extractor.py*

## Contributing
Contributions to the Lidar Forest Metrics Extractor project are welcome! If you find any issues or have suggestions for improvements, please submit them via GitHub issues or create a pull request.

## License
This project is licensed under the MIT License.