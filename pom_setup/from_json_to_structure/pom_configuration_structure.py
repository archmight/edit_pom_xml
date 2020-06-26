

class PomConfigurationStructure:

    def __init__(self, file_path, groupId, artifactId, version, packaging):

       self.file_path = file_path
       self.group_id = groupId
       self.artifact_id = artifactId
       self.version = version
       self.package = packaging

        if self.group_id is None:
            self.group_id = "unknown"

        if self.artifact_id is None:
            self.artifact_id = file_path

        if self.version is None:
            self.version = "0.9"

        if self.package is None:
            self.package = "some_package"


    def print(self):
        print(self.file)
        print(self.groupId)
        print(self.artifactId)
        print(self.version)
        print(self.packaging)

    def get_filename(self):
        return self.file
