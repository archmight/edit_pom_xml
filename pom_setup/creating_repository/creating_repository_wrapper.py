from pom_setup.creating_repository.creating_repository import CreatingRepository


class CreatingRepoWrapper:
    """ create local repo and add necessary """

    def __init__(self, jars_directory: str, project_path: str):
        self.creating_repository = CreatingRepository(jars_directory=jars_directory, project_path=project_path)
        self.creating_repository.mkdir_repository()
        self.creating_repository.find_cp_and_set_jars_list()

    def get_jars_list(self):
        return self.creating_repository.jars_list

    def get_local_repo_dir_name(self):
        return self.creating_repository.local_repo_path
