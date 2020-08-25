import pandas as pd
import numpy as np
import warnings
import sys
import re

def parse_str2num(str_to_parse, mute_warning=False, scale=1):
    """Convert string type column into numeric.
    """
    # Check if numeric type argument is passed
    if isinstance(str_to_parse, (int, float, complex)) and not isinstance(str_to_parse, bool):
        warnings.warn("Numeric argument passed. No conversion performed and original series is returned.")
        return str_to_parse
    
    # Raise error if passed type is not numeric or string
    elif not isinstance(str_to_parse, str):
        raise TypeError("Expected str argument. Received {0} type.".format(str(type(str_to_parse)).split("'")[1]))
  
    # Replace all white space, commas
    multiplier = 1
    str_intm = re.sub("\s|,", "", str_to_parse).lower()
    
    # Check if any multiplier
    if re.search('b$|bil$|billion$', str_intm) != None:
        multiplier = 1e9
        
    elif re.search('m$|mil$|million$', str_intm) != None:
        multiplier = 1e6
    
    elif re.search('k$', str_intm) != None:
        multiplier = 1e3
        
    # Perform conversion
    str_parsed = multiplier/scale * pd.to_numeric(re.sub("[^0-9|\.]", "", str_intm))
    
    return str_parsed