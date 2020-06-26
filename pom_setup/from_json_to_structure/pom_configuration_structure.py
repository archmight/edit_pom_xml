

class PomConfigurationStructure:

    def __init__(self, file, groupId, artifactId, version, packaging):
        self.file = file
        self.groupId = groupId
        self.artifactId = artifactId
        self.version = version
        self.packaging = packaging

    def print(self):
        print(self.file)
        print(self.groupId)
        print(self.artifactId)
        print(self.version)
        print(self.packaging)

    def get_filename(self):
        return self.file
