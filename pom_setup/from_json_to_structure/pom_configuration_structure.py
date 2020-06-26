

class PomConfigurationStructure:

    def __init__(self, filename, groupId, artifactId, version, packaging):

        self.filename = filename
        self.group_id = groupId
        self.artifact_id = artifactId
        self.version = version
        self.package = packaging

        if self.group_id is None:
            self.group_id = "unknown"

        if self.artifact_id is None:
            self.artifact_id = filename

        if self.version is None:
            self.version = "0.9"

        if self.package is None:
            self.package = "some_package"

    def print(self):
        print(self.filename)
        print(self.group_id)
        print(self.artifact_id)
        print(self.version)
        print(self.package)

    def get_filename(self):
        return self.filename
