import os
import sys
import logging

logging_str = "[%(asctime)s:%(LevelName)s:%(module)s: %(message)s]"

Log_dir ="Logs"
Log_filepath = os.path.join(Log_dir,"running_Logs.Log")
os.makedirs(Log_dir, exist_ok = True)

logging.basicConfig(
    Level = logging.INFO,
    format = logging_str,
    handlers= [logging.FileHandler(Log_filepath),
               logging_str.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("cnnClassifier Logger")
