# importing required libraries 
import re
import yaml
from dataclasses import dataclass
from typing import Union

# ProcessParam is a class instance for storing parameters used for the process. 
@dataclass
class Params: 
    step_xy: float
    step_z: float
    return_num: int
    ground_class_ignore: float
    max_z: int
    percentile_height: list[int]
    statistics: list[str]
    

@dataclass
class File: 
    yaml_file: str



@dataclass
class ProcessParam: #pascal case
    
    """
    A class representing parameters for performing lidar data processing with lastool.
    
    Attributes 
    ----------
    yaml_file : File
        The YAML configuration file.
    step_xy : float
        Value used within the lasnoise process as step_xy argument.
    step_z : float
        Value used within the lasnoise process as step_z argument.
    return_num : int
        Value used within las2las process as keep_return argument.
    ground_class_ignore : float
        Value used within lasground process as ignore_class argument.
    
    Methods
    -------
    __post_init__(self)
        Initializes attributes and validates input data.
    load_config(self, yaml_file: File) -> dict
        Loads YAML configuration file.
    target_projection(self) -> str
        Extracts raw lidar CRS/projection information from the lasinfo.txt file.
    """
    
    yaml_file: File
    step_xy: float
    step_z: float
    return_num: int
    ground_class_ignore: float
    
    def __post_init__(self):
        
        self.config = self.load_config(self.yaml_file)
        # Validating recieved arguments
        assert self.step_xy > 0, f"step_xy variable {self.step_xy} for the denoising process should be greater than 0!"
        assert self.step_z > 0, f"step_z variable {self.step_z} for the denoising process should be greater than 0!"
        assert self.return_num > 0, f"Specify a return number {self.return_num} !"
        assert self.config["parameter"]["upper_z"] > 0, f"Specify a max_Z value greater than zero!"
        
        # Assign instance attributes 
        self.max_z = self.config["parameter"]["upper_z"]
        self.ignore_class = self.ground_class_ignore
        self.percentile_height = " ".join(map(str, self.config["parameter"]["percentile"]))
        self.statistics = " ".join(self.config["parameter"]["statistics"])
        self.lastooldir = self.config["config_path"]["lastool_folder"]
        
    # function for loading yaml configuration file    
    def load_config (self, yaml_file: File) -> dict:
        """
        Load YAML configuration file.

        Parameters
        ----------
        yaml_file : Any
            The YAML configuration file.

        Returns
        -------
        dict
            Loaded configuration as a dictionary.
        """ 
        with open(yaml_file, 'r') as file: 
            config = yaml.safe_load(file)
            return config
     
    # Function for extracting lidar data crs   
    def target_projection (self): 
        """
        _summary_
        -----------------
        Extract raw lidar crs/projection information from 
        the lasinfo.txt file created via the lasinfo process.  

        Parameters 
        --------------------------------------
        None
        
        Returns:
        -----------------
            _string_: geographic coordinate reference system 
            of the the lidar data. 
        """
        try: 
            with open(self.info_file_path, 'r').readlines() as info:
                for line in info: 
                    # search for 'ProjectedCST' within the lasinfo.txt file. 
                    if re.search("ProjectedCST", line): 
                        # extract the crs from the string
                        crs = int(line.split('-')[0].split(' ')[-2])
                    return crs
            return None
        except Exception as e: 
            print(f"error occured while reading file {self.info_file_path}: {e}")
            return None