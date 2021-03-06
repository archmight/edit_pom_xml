import json


class WorkWithJson:
    """ class to read-write json data """
    def __init__(self, path_to_config_file):
        """set path to json file data"""
        self.file_path = path_to_config_file

    def create_file(self):
        """useless method"""
        pass

    def read_file(self):
        """read json aand convert into python structure"""
        data = []
        with open(self.file_path, "r") as r_f:
            data = json.loads(r_f.read())

        return data

    def write_file(self):
        """write into file"""
        data = self.set_data()
        with open(self.file_path, 'w') as w_f:
            w_f.write(json.dumps(data, ensure_ascii=False))

    def set_data(self):
        """example write data struct"""
        data = [
            {"ASN1P-1.0.jar": {
                "groupId": "ru.lanit.jcp",
                "artifactId": "ASN1P",
                "version": "1.0",
                "packaging": "jar"
            }},
            {"asn1rt-1.0.jar": {
                "groupId": "ru.lanit.jcp",
                "artifactId": "asn1rt",
                "version": "1.0",
                "packaging": "jar"
            }},
            {"cadessignature-1.0.jar": {
                "groupId": "ru.lanit.jcp",
                "artifactId": "cadessignature",
                "version": "1.0",
                "packaging": "jar"
            }},
            { "JCP-1.0.jar": {
                "groupId": "ru.lanit.jcp",
                "artifactId": "JCP",
                "version": "1.0",
                "packaging": "jar"
            }},
            { "JCPRequest-1.0.jar": {
                "groupId": "ru.lanit.jcp",
                "artifactId": "JCPRequest",
                "version": "1.0",
                "packaging": "jar"
            }}
        ]
        return data


if __name__ == "__main__":
    a = WorkWithJson("/home/gerdon/Desktop/tmp/j_s-o_n/jars_configuration.json")
    a.write_file()
