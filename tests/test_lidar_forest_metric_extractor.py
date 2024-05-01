import unittest
from main_metric_extractor import extract_forest_mectrics
import os

class TestForestMectricsExtractor(unittest.TestCase): 
    """
    Test case class for validating forest canopy metrics extractor.

    This test case class is designed to test the functionality of the forest canopy metrics extractor,
    including the extraction of forest canopy metrics from valid and invalid lidar data files.

    Attributes:
        valid_lidar_dir (str): The directory path containing valid lidar data files.
        invalid_lidar_dir (str): The directory path containing invalid lidar data files.

    Methods:
        setUp(self): Set up the necessary attributes and validate the input data.
        test_valid_metric_extractor(self): Test the forest canopy metrics extraction from valid lidar data.
        test_invalid_metric_extractor(self): Test the forest canopy metrics extraction from invalid lidar data.
    """
    
    def setUp(self) -> None:
        """
        Set up the necessary attributes and validate the input data.

        This method sets up the necessary attributes for the test case and validates the input data.
        It checks if the specified lidar data directories exist and if they are valid directories.

        Raises:
            FileNotFoundError: If one or both of the lidar data directories do not exist.
        """
        
        # Initialize valid and invalid lidar file paths
        self.valid_lidar_dir = "C:/Users/khalsz/Documents/CarbonKeepers/lidar_canopy_metrics/lidar-forest-metrics-extractor/tests/valid_data/"
        self.invalid_lidar_dir = "C:/Users/khalsz/Documents/CarbonKeepers/lidar_canopy_metrics/lidar-forest-metrics-extractor/tests/invalid_data/"
        
        # Check if file exist
        if not (os.path.isdir(self.valid_lidar_dir), os.path.isdir(self.invalid_lidar_dir)): 
            raise FileNotFoundError("one or both of the files does not exist")
        
        
    def test_valid_metric_extractor(self): 
        """testing the validity of function using a valid .laz file"""
        try: 
            extract_forest_mectrics(self.valid_lidar_dir)
        except Exception as e: 
            self.fail(f"Function raises an exception with valid directory {e}")
        
        
    def test_invalid_metric_extractor(self): 
        """testing the validity of function using a invalid .laz file"""
        with self.assertRaises(Exception):
            extract_forest_mectrics(self.invalid_lidar_dir)
            
if __name__ == "__main__": 
    unittest.main()
    
