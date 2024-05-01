
# Importing libraries
from directories.dir_creator import DirectoryManager
from util.parameters import ProcessParam
from config import constant_var as const


class LastoolCommands: 
    """
    A class for managing and initializing Lastools commands.

    This class manages the initialization of Lastools commands for processing lidar data.
    It provides methods to initialize different Lastools commands for various processing steps.

    Attributes:
        lidar_data_dir (str): The directory path containing lidar data files.
        config_yaml (str): The path to the configuration YAML file.

    Methods:
        initialize_command(self): Initialize the Lastools commands for lidar data processing.
    """
    
    def __init__(self, lidar_data_dir: str, config_yaml: str): 
        """
        Initialize the LastoolCommands instance.

        Args:
            lidar_data_dir (str): The directory path containing lidar data files.
            config_yaml (str): The path to the configuration YAML file.
        """
        self.lid_dir = DirectoryManager(lidar_data_dir)
        self.params = ProcessParam(step_xy=const.XY_STEP, step_z=const.Z_STEP, 
                        return_num=const.RETURN_NUMBER, 
                        ground_class_ignore=const.LASGOURND_CLASS, yaml_file=config_yaml)
        
        self.initialize_command()
        
    def initialize_command(self): 
        """
        Initialize Lastools commands for lidar data processing.

        This method initializes different Lastools commands for various processing steps,
        including lasinfo, lassplit, lasnoise, las2las, lasground, lasindex, lascanopy, and lasdem.
        """
        # Initializing process for lasinfo to get details about the lidar (laz) data
        self.lasinfo_CMD = f'lasinfo -i {self.lid_dir.raw_data}\*.laz ' \
                f'-odir {self.lid_dir.info_dir} -odix _info -otxt'              
            
        # Initializing process for lassplit to split the data into several compressed LAZ_file output
        # containing 5 million points. 
        self.lassplit_CMD = f'lassplit -i {self.lid_dir.raw_data}\*.laz ' +\
                    f'-odir {self.lid_dir.lassplit_dir} -olaz -split 5000000'
                    
        # Initializing process for lasnoise to to remove noise and outlier from the laz files
        self.noiseRemoval_CMD = f'lasnoise -i {self.lid_dir.lassplit_dir}\*.laz -step_xy {self.params.step_xy} '\
                f'-step_z {self.params.step_z} -remove_noise -odir {self.lid_dir.denoised_dir} -olaz' 
            
            
        # Initializing process for las1las to to filter out points with z value above 10m
        self.las2las_CMD = f'las2las -i {self.lid_dir.denoised_dir}\*.laz -odir {self.lid_dir.first_return_dir} '\
                f'-keep_return {self.params.return_num} -olaz' 
                
        # Initializing process for lasground to get the ground level of the data 
        self.lasground_CMD = f'lasground -i {self.lid_dir.first_return_dir}\*.laz -ignore_class 7 '\
            f'-cutoff_z_above {self.params.max_z} -compute_height -replace_z -odir ' \
            f'{self.lid_dir.lasground_dir} -olaz' 

        # Initializing process for lasindex to index the lidar height data for faster processing
        self.lasindex_CMD = f'lasindex -i {self.lid_dir.lasground_dir}\*.laz'  


        # Initializing process for lascanopy to calculate forestry metrics of points and grids them into raster
        self.lascanopy_CMD = f'lascanopy -i {self.lid_dir.lasground_dir}\*.laz -step 3 {self.params.statistics} ' \
            f'-p {self.params.percentile_height} -otif -o {self.lid_dir.lascanopy_dir}/.tif'
            
        # Initializing process for las2dem to calculate vegetation point cloud elevation and grid them into raster    
        self.lasdem = f'las2dem -i {self.lid_dir.first_return_dir}\*.laz -keep_first -drop_class 7 -step 3 -elevation '\
                f'-otif -o {self.lid_dir.lascanopy_dir}/ele.tif'
                


