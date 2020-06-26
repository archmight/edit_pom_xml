import os
import xml.etree.ElementTree as etree
from xml.dom import minidom


class EditingPom:
    def __init__(self, project_path, file_names, local_repo_dir_name):

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


    def add_install_plugins(self):
        build_path = "{" + "{}".format(self.namespace1) + "}build"
        build = self.root.find(build_path)
        plugins_path = "{" + "{}".format(self.namespace1) + "}plugins"
        plugins = build.find(plugins_path)


        ### make xml wrapper -  add plugin, executions ###

        plugin = etree.Element("plugin")
        group_id = etree.SubElement(plugin, 'groupId')
        group_id.text = "org.apache.maven.plugins"
        artifact = etree.SubElement(plugin, 'artifactId')
        artifact.text = "maven-install-plugin"
        executions = etree.SubElement(plugin, 'executions')
        ### end xml wrapper - add plugin, executions ###

        dp = input("want set up dependencies parameters? Yy")

        if dp == 'y' or dp == 'Y':

            grp = None
            artfct = None
            pth = None
            vrsn = None


            for execution_id, file in enumerate(self.file_list):
                executions.append(self.add_install_plugin_to_pom_xml(filename=file, execution_id=execution_id, group_id=grp,
                                                   artifact_id=artfct, path=pth, file_version=vrsn))

        else:
            for execution_id, file in enumerate(self.file_list):
                executions.append(self.add_install_plugin_to_pom_xml(filename=file, execution_id=execution_id))
        plugins.append(plugin)
        self.write_to_pom_file(minidom.parseString(etree.tostring(self.root)))

    def add_install_plugin_to_pom_xml(self, filename, execution_id, group_id=None, artifact_id=None,
                                      path=None, file_version=None):
        if group_id is None:
            group_id = self.group_id
        if artifact_id is None:
            artifact_id = filename[:-8]
        if path is None:
            path = self.repo_name
        if file_version is None:
            file_version = self.version
        return self.create_execution(filename=filename, execution_id=execution_id, path=path, groupId=group_id,
                                     artifactId=artifact_id, file_version=file_version)






    def add_repository(self):
        repo_path = self.create_path("}repositories")
        repositories = self.root.find(repo_path)
        repository = etree.Element("repository")
        xml_repo_id = etree.SubElement(repository, 'id')
        xml_repo_id.text = "repo_name"
        url = etree.SubElement(repository, "url")
        url.text = self.project_path + "/" + self.repo_name
        repositories.append(repository)
        self.write_to_pom_file(minidom.parseString(etree.tostring(self.root)))

    def write_to_pom_file(self, xml_block: minidom):
        s2 = xml_block.toprettyxml('    ', '\n', 'utf-8')
        pom_path = self.project_path + self.pom_file_name
        with open(pom_path, mode='w') as f:
            f.write(s2.decode('utf-8'))

    def create_path(self, name):
        return "{" + self.namespace1 + "}" + name