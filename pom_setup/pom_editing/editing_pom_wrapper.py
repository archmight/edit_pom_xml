from pom_setup.pom_editing.editing_pom import EditingPom


class EditingPomWrapper:
    """wrapper class above editing pom, """
    def __init__(self, project_path, file_names, local_repo_dir_name, configuration_list):
        self.configuration_list = configuration_list
        self.editing_pom = EditingPom(project_path=project_path, file_names=file_names,
                                      local_repo_dir_name=local_repo_dir_name, configuration_list=configuration_list)

        self.editing_pom.add_install_execution()

    def set_configurations(self):
        pass

        # self.editing_pom = []
        #
        # for a in 123:
        #     self.editing_pom.append(EditingPom(project_path, jars_list, local_repo_directory))

#        self.editing_pom.add_repository()
#        self.editing_pom.add_install_plugins()
