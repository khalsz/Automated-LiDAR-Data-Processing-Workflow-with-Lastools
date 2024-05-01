import subprocess
import logging
from config import constant_var as cons


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(fmt=cons.FORMATER)
logger.addHandler(stream_handler)

#process_run is used to run each process step
def process_run(cmd: str): 
    """
    Execute a command using subprocess.

    Parameters 
    ----------
    cmd : str
        The command to be executed.

    Returns
    -------
    tuple
        Tuple containing the stdout and stderr from the process.
    """
    out=subprocess.PIPE 
    err=subprocess.PIPE
    p = subprocess.Popen(cmd, stdout=out, stderr = err)
    stdout, stderr = p.communicate()
    if p.returncode == 0:
        print(f"process {cmd.split(' ')[0]} successfully executed")
        return stdout, ''
    else: 
        logger.error(f"Error running process {cmd.split(' ')[0]}. The process returns code: {p.returncode} with error: {stderr} ")
        return '', stderr



def handle_func_err(func,  message, arg=None): 
    """
    Handle errors for a given function.

    Parameters 
    ----------
    func : function
        The function to be executed.
    arg : str or int, optional
        The argument for the function, by default None.
    message : str
        A message describing the operation/task being run.

    Returns
    -------
    bool
        True if the operation succeeds, False otherwise.
    """
    if arg is None: 
        _, stderr = func()
    if arg is not None: 
        _, stderr = func(arg) 
    if stderr != '': 
        error_mssg = f" {message} encountered an error {stderr}"
        return logger.error(error_mssg)
    else: 
        return True
