from pom_setup.from_json_to_structure.from_json_to_structure import FromJsonToStructure


class FromJsonToStructureWrapper:
    def __init__(self, path_to_config_file):
        self.from_json_to_structure = FromJsonToStructure(path_to_config_file)
        self.from_json_to_structure.work_with_data()

    def get_filenames_list(self):
        return self.from_json_to_structure.structure_list.get_filenames_list()

    def configuration_list(self):
        return self.from_json_to_structure.structure_list
