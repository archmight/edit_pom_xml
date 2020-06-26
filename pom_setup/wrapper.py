from pom_setup.creating_repository.creating_repository_wrapper import CreatingRepoWrapper
from pom_setup.from_json_to_structure.from_json_to_structure_wrapper import FromJsonToStructureWrapper
from pom_setup.pom_editing.editing_pom_wrapper import EditingPomWrapper


class Wrapper:
    def __init__(self, dependencies_directory: str, project_path: str, json_config_path):

        self.repository_work = CreatingRepoWrapper(dependencies_directory, project_path)
        jars_list = self.repository_work.get_jars_list()
        local_repo_directory = self.repository_work.get_local_repo_dir_name()

        from_json_to_wrapper = FromJsonToStructureWrapper(json_config_path)

        print(from_json_to_wrapper.get_filenames_list())
        conf_list = from_json_to_wrapper.configuration_list()
        self.pom = EditingPomWrapper(project_path=project_path,configuration_list=conf_list)

