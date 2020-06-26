import xml.etree.ElementTree as etree
from pom_setup.from_json_to_structure.pom_configuration_structure import PomConfigurationStructure


class CreatingExecution:

    def __init__(self, configuration: PomConfigurationStructure, file_path, execution_id):
        self.configuration = configuration
        self.file_path = file_path
        self.execution_id = execution_id

    def create_execution(self):
        execution = etree.Element('execution')
        execute_id = etree.SubElement(execution, 'id')
        execute_id.text = str(self.execution_id)
        phase = etree.SubElement(execution, 'phase')
        phase.text = "initialize"
        goals = etree.SubElement(execution, 'goals')
        goal = etree.SubElement(goals, 'goal')
        goal.text = "install-file"
        configuration = etree.SubElement(execution, 'configuration')
        ### main part ###
        file = etree.SubElement(configuration, 'file')
        file.text = self.file_path
        group_id = etree.SubElement(configuration, 'groupId')
        group_id.text =self.configuration.group_id
        artifact_id = etree.SubElement(configuration, 'artifactId')
        artifact_id.text = self.configuration.artifact_id
        version = etree.SubElement(configuration, 'version')
        version.text = self.configuration.version
        packaging = etree.SubElement(configuration, 'packaging')
        packaging.text = self.configuration.package
        return execution

