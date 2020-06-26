from pom_setup.from_json_to_structure.pom_configuration_structure import PomConfigurationStructure


class ConfigurationList:
    def __init__(self):
        self.structure_list = []

    def append(self, pom_configuration: PomConfigurationStructure):
        self.structure_list.append(pom_configuration)

    def get_list(self):
        return self.structure_list

    def print(self):
        for _ in self.structure_list:
            _.print()

    def get_filenames_list(self):
        filenames = []
        for _ in self.structure_list:
            filenames.append(_.get_filename())

        return filenames
