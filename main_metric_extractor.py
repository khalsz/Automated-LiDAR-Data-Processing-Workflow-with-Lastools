# importing required libraries 

import logging
import os
from config import constant_var as const
from util.commands import LastoolCommands 
from util.process_runner import process_run, handle_func_err
import os

# initializing logging parameters for error 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(fmt=const.FORMATER)
logger.addHandler(stream_handler)




# main function for extract forest canopy metrics from lidar data 
def extract_forest_mectrics( lidar_data_dir): 
    """
    Main function for running all the processes related to forest metrics extraction.

    Parameters:
    -----------
    lidar_data_dir : str
        The directory path containing lidar data files.

    Returns:
    --------
    None
    """
    
    # Define the path to the YAML configuration file
    yaml_file_path = "C:/Users/khalsz/Documents/CarbonKeepers/lidar_canopy_metrics/config/config.yaml"
    
    # Initialize LastoolCommands instance with lidar data directory and YAML file path 
    lt_commands = LastoolCommands(lidar_data_dir, yaml_file_path)
    
    # Change the working directory to the directory containing Lastool files 
    os.chdir(lt_commands.params.lastooldir)  #use lt_command which contains ProcessParams class instace to extract lastool directory  
    
    # Define a list of tuples, each containing a function to run, its argument, and a message
    steps = [ 
        (process_run, lt_commands.lasinfo_CMD, "Lasinfo process step"), 
        (process_run, lt_commands.lassplit_CMD, "Lassplit process step"), 
        (process_run, lt_commands.noiseRemoval_CMD, "Lasnoise process step"), 
        (process_run, lt_commands.las2las_CMD, "Las2las process step"), 
        (process_run, lt_commands.lasground_CMD, "LasGround process step"), 
        (process_run, lt_commands.lasdem, "Las2dem process step"), 
        (process_run, lt_commands.lasindex_CMD, "Lasindex process step"), 
        (process_run, lt_commands.lascanopy_CMD, "Lascanopy process step"), 
        ]
    
    # Iterate over each defined step and run the corresponding function    
    for func, arg, message in steps:
        # If an error occurs in the function, handle it and continue to the next step
        if handle_func_err(func=func, message=message, arg=arg): 
            continue
        else: 
            # If an error occurs, break the loop
            break
    
    # calling the del_dir() funtion of the DirectoryManager which has been instantiated 
    # within LastoolCommands class 
    lt_commands.lid_dir.del_dir() # Call the del_dir() function to clean up directories
    
    
if __name__ == "__main__": 
    extract_forest_mectrics("C:/Users/khalsz/Downloads/drive-download-20240422T082105Z-001/ept_NY5123/ept-data")
    

  