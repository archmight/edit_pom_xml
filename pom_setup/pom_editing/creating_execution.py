import xml.etree.ElementTree as etree
from pom_setup.from_json_to_structure.pom_configuration_structure import PomConfigurationStructure


class CreatingExecution:

    def __init__(self, configuration: PomConfigurationStructure, file_path, execution_id):
        self.configuration = configuration
        self.execution = self.create_execution(file_path=file_path, execution_id=execution_id,
                                               groupId=self.configuration.group_id,
                                               artifactId=self.configuration.artifact_id,
                                               file_version=configuration.version,
                                               packaging_type=self.configuration.package)

    def create_execution(self, file_path, execution_id, groupId, artifactId, file_version, packaging_type):
        execution = etree.Element('execution')
        execute_id = etree.SubElement(execution, 'id')
        execute_id.text = str(execution_id)
        phase = etree.SubElement(execution, 'phase')
        phase.text = "initialize"
        goals = etree.SubElement(execution, 'goals')
        goal = etree.SubElement(goals, 'goal')
        goal.text = "install-file"
        configuration = etree.SubElement(execution, 'configuration')
        ### main part ###
        file = etree.SubElement(configuration, 'file')
        file.text = file_path
        group_id = etree.SubElement(configuration, 'groupId')
        group_id.text = groupId
        artifact_id = etree.SubElement(configuration, 'artifactId')
        artifact_id.text = artifactId
        version = etree.SubElement(configuration, 'version')
        version.text = file_version
        packaging = etree.SubElement(configuration, 'packaging')
        packaging.text = packaging_type
        return execution

