import sys

from pom_setup.wrapper import Wrapper

if __name__ == "__main__":
    dependencies_directory = sys.argv[1]
    project_path = sys.argv[2]
    json_config_path = "/home/gerdon/Desktop/tmp/j_s-o_n/jars_configuration.json"
    wrapper = Wrapper(dependencies_directory, project_path, json_config_path)
