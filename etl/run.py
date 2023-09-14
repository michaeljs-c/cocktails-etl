import config
from pipeline import run_pipeline, data_sources
from models import Session, engine
import argparse

if __name__ == '__main__':
    # TODO pass in config file reference instead of having it contained in the code
    
    # parser = argparse.ArgumentParser(description="Run a data pipeline using a config file.")
    # parser.add_argument("config_file", type=str, help="Path to the config file")
    # args = parser.parse_args()
        
    conf = config.__dict__
    run_pipeline(Session(), conf, data_sources)
