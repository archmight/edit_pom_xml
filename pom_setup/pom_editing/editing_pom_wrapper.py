from pom_setup.pom_editing.editing_pom import EditingPom


class EditingPomWrapper:

    def __init__(self, configuration_list):

        self.configuration_list = configuration_list
        self.editing_pom = EditingPom()



    def set_configurations(self):


        # self.editing_pom = []
        #
        # for a in 123:
        #     self.editing_pom.append(EditingPom(project_path, jars_list, local_repo_directory))

#        self.editing_pom.add_repository()
#        self.editing_pom.add_install_plugins()