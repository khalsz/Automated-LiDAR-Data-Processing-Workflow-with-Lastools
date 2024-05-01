# importing required libraries 
import os
from os.path import join 
from config import constant_var as const
import logging
import shutil
import os


# initializing logging parameters for error 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(fmt=const.FORMATER)
logger.addHandler(stream_handler)


# LidarDataDir is a class instance for storing directories for saving the processed data.       
class DirectoryManager: #pascal case
    """
    A class for managing directories for storing processed lidar data.

    Attributes:
        base_dir (str): The base directory for lidar data.

    Methods:
        __init__(self, base_dir): Initializes the DirectoryManager.
        create_dir(self): Creates necessary directories.
        del_dir(self): Deletes unnecessary directories.
    """
    
    def __init__(self, base_dir):
        
        """
        Initializes the DirectoryManager.

        Parameters:
            base_dir (str): The base directory for lidar data.
        """     
        # Validating recieved arguments 
        assert os.path.isdir(base_dir), f"lidar raw data base directory {base_dir} not a valid directory"
        filenames = os.listdir(base_dir)
        suffixes = (".las", ".laz")
        assert any(file.endswith(suffixes) for file in filenames), \
            f"lidar raw data base directory {base_dir} contains no valid las file"
        self.raw_lidar_dir = base_dir
        self.dir_basenames = ["lazinfo", "lazsplit", "denoised", "first_return", 
                        "lazground", "canopy_metrics"]
        
        self.dir_var_dic = self.create_dir()
        
        # Assign instance attributes 
        self.raw_data = self.dir_var_dic['raw_lidar_dir']
        self.info_dir = self.dir_var_dic['lazinfo']
        self.lassplit_dir = self.dir_var_dic['lazsplit']
        self.denoised_dir = self.dir_var_dic['denoised']
        self.first_return_dir = self.dir_var_dic['first_return']
        self.lasground_dir = self.dir_var_dic['lazground']
        self.lascanopy_dir = self.dir_var_dic['canopy_metrics']
    
        
    def create_dir(self): 
        """
        Creates necessary directories.

        Returns:
            dict: A dictionary mapping directory names to their paths.
        """
        dir_var_dic = {"raw_lidar_dir": self.raw_lidar_dir} 
        for basename in self.dir_basenames: 
            try: 
                dir_path = join(self.raw_lidar_dir, basename)
                # delete folder if one exists.
                if os.path.exists(dir_path): 
                        shutil.rmtree(dir_path)
                # create new folder
                os.mkdir(dir_path)
                # mapping directory path with respective keys
                dir_var_dic[basename] = dir_path
            except Exception as e: 
                logger.error(f"Error creating directory {dir_path}: {e}")
                raise
        logger.info("Succesfully created all directories")
        return dir_var_dic


    
    def del_dir(self): 
        """
        Deletes unnecessary directories.
        """
        #delete all folders except the raw_lidar, info_dir & lascanopy_dir
        for directory in list(self.dir_var_dic.values())[2:-1]: 
            try: 
                shutil.rmtree(directory)
            except Exception as e: 
                logger.error(f"Error deleting folder {directory}: {e}")
        logger.info("Successfully deleted all unnecessary directories")
        





