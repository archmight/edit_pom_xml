from pom_setup.from_json_to_structure.pom_configuration_list import ConfigurationList
from pom_setup.from_json_to_structure.pom_configuration_structure import PomConfigurationStructure
from pom_setup.from_json_to_structure.work_with_json import WorkWithJson


class FromJsonToStructure:
    def __init__(self, path_to_config_file):
        self.json_work = WorkWithJson(path_to_config_file)
        self.data = self.json_work.read_file()
        self.structure_list = ConfigurationList()

    def work_with_data(self):
        for element in self.data:
            filename = None
            group_id = None
            artifact_id = None
            version = None
            packaging = None
            for key, values in element.items():

                if "groupId" in values:
                    group_id = values["groupId"]
                if "artifactId" in values:
                    artifact_id = values["artifactId"]
                if "version" in values:
                    version = values["version"]
                if "packaging" in values:
                    packaging = values["packaging"]

            self.structure_list.append(PomConfigurationStructure(file=filename,
                                                                     groupId=group_id, artifactId=artifact_id,
                                                                     version=version, packaging=packaging))

    def get_configuration_list(self):
        return self.structure_list

    def print_jars(self):
        self.structure_list.print()

    def print_filenames(self):
        print(self.structure_list.get_filenames_list())


if __name__ == "__main__":
    a = FromJsonToStructure("/home/gerdon/Desktop/tmp/j_s-o_n/jars_configuration.json")
    a.work_with_data()
    a.print_jars()
    a.print_filenames()
