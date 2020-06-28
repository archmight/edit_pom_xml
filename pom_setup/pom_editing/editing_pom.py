import os
import platform
import xml.etree.ElementTree as etree
from xml.dom import minidom

from pom_setup.from_json_to_structure.pom_configuration_list import ConfigurationList
from pom_setup.pom_editing.creating_execution import CreatingExecution


class EditingPom:
    def __init__(self, project_path, file_names, local_repo_dir_name, configuration_list: ConfigurationList):

        self.pom_file_name = "/pom.xml"
        self.version = "1.0"
        self.group_id = "ru.lanit.jcp"
        self.repo_name = local_repo_dir_name
        self.namespace1 = "http://maven.apache.org/POM/4.0.0"
        etree.register_namespace('', self.namespace1)
        self.namespace2 = "http://www.w3.org/2001/XMLSchema-instance"
        etree.register_namespace('xsi', self.namespace2)
        self.namespace3 = "http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"
        etree.register_namespace('schemaLocation', self.namespace3)
        self.project_path = project_path
        self.tree = etree.parse(os.path.join(self.project_path, "pom.xml"))
        self.root = self.tree.getroot()
        self.file_list = file_names
        self.path_split_char = self.set_path_split_char()

        self.configuration_list = configuration_list


    def add_install_execution(self):
        build_path = self.create_path("build")
        build = self.root.find(build_path)
        plugins_path = self.create_path("plugins")
        plugins = build.find(plugins_path)

        ### make xml wrapper -  add plugin, executions ###

        plugin = etree.Element("plugin")
        group_id = etree.SubElement(plugin, 'groupId')
        group_id.text = "org.apache.maven.plugins"
        artifact = etree.SubElement(plugin, 'artifactId')
        artifact.text = "maven-install-plugin"
        executions = etree.SubElement(plugin, 'executions')
        ### end xml wrapper - add plugin, executions ###

        for execution_id, Configuration in enumerate(self.configuration_list.get_list()):
            file_path = str(self.repo_name) + str(self.path_split_char) + str(Configuration.filename)
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", file_path)
            executions.append(self.add_install_plugin_to_pom_xml(
                    configuration=Configuration, file_path=file_path, execution_id=execution_id)
                              )
        ### +++ ###
        plugins.append(plugin)
        self.write_to_pom_file(minidom.parseString(etree.tostring(self.root)))
        ### +++ ###

    def add_install_plugin_to_pom_xml(self, configuration,  file_path, execution_id):
        creating_execution = CreatingExecution(configuration=configuration, file_path=file_path, execution_id= execution_id)
        return creating_execution.create_execution()


    def write_to_pom_file(self, xml_block: minidom):
        s2 = xml_block.toprettyxml('    ', '\n', 'utf-8')
        pom_path = self.project_path + self.pom_file_name
        with open(pom_path, mode='w') as f:
            f.write(s2.decode('utf-8'))

    def create_path(self, name):
        return "{" + self.namespace1 + "}" + name

    def set_path_split_char(self):
        """method to correctly """
        if platform.system() == 'Windows':
            return '\\'
        elif platform.system() == 'Linux':
            return '/'
        else:
            print("WAIT FOR ERROR(class creating_repository, method set_path_split_char): not defined os.name=" + platform.system())


    # def add_repository(self):
    #     repo_path = self.create_path("repositories")
    #     repositories = self.root.find(repo_path)
    #     repository = etree.Element("repository")
    #     xml_repo_id = etree.SubElement(repository, 'id')
    #     xml_repo_id.text = "repo_name"
    #     url = etree.SubElement(repository, "url")
    #     url.text = self.project_path + "/" + self.repo_name
    #     repositories.append(repository)
    #     self.write_to_pom_file(minidom.parseString(etree.tostring(self.root)))

