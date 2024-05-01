# importing required libraries 
import logging

# the -step_xy parameter used in the lasnoise tool command for denoising lidar data
XY_STEP = 4

# the -step_z parameter used in the lasnoise tool command for denoising lidar data
Z_STEP = 4

# the -keep_return parameter used in the las2las tool command indicating the 
# lidar data return to keep
RETURN_NUMBER = 1


# the -ignore_class parameter used the in the lasground tool command for indicating the 
# lidar data class to ignore in the lasground data processing step 
LASGOURND_CLASS = 7


# format for logging task error or informatio 
FORMATER = logging.Formatter('%(asctime)s:%(name)s:%(funcName)s:%(message)s')




