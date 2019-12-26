import os
import sys
from typing import List

from javalang.tree import MethodDeclaration, ClassDeclaration
import traceback

cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, os.path.join(cwd, '..', 'perfec2'))

import perfec2

repos_root = '/Users/sroman/repos'
repos = {
    # 'address-api': "A REST API for operations on Addresses, Address Types and their relationships in AMS. Addresses are used to geographically locate a Person or Organization or for operations on identification purposes. Each Address has a mandatory Address Type.",
    # 'ams-search-api': "A REST API for operations on searching AMS entities by specifying one or more attribute values; e.g.: "
                    # "\"all Persons with last name like 'Johns%'\" or \"all franchises with manufacturer 'Ford'\"\n"
    # 'apppolicy-api': "A REST API for operations on Application Policies and their relationships in AMS. An AppPolicy grants a user access to\n"
                        # " an online marketplace (such as m.com, OVE, or Simulcast) on behalf of an Organization (dealership). Can also represent\n
                        # "other application-level AMS permissions"
    # 'contact-api': "A REST API for operations on Contacts, Contact Types and their relationships in AMS. Contacts are lines of communication\n"
                    # " to Organizations and Persons such as telephone numbers, email addresses, etc. Each Contact has a mandatory Contact Type. \n"
    # 'identifier-api': "A REST API for operations on Identifiers, Identifier Types and their relationships in AMS. Identifiers are used\n"
                        # " in conjunction with an Identifier Type to uniquely identify an Organization or Person. An entity may have many Identifiers \n"
                        # "but never of the same Identifier Type. Pairs of Identifier/IdentifierType are always unique."
    # 'issue-api': "A REST API for operations on Issues and their relationships in AMS. Issues track actions required of an Organization or Person \n"
                    # "such as the submission of legal or identification documents or any condition preventing a person from buying or selling at \n"
    #                   "auction or online."
    # 'organization-api': "A REST API for operations on Organizations and their relationships in AMS. Organizations (dealerships), may be \n"
                        # "related to Organization Groups, Issues, Contacts and can grant Roles to Persons.",
    # 'organizationgroup-api': "A REST API for operations on OrganizationGroups and their relationships in AMS. Organization Groups (franchise groups)\n"
                                # "may be related to Persons, Organizations, and Application Policies. A relationship between an Organization Group\n"
    #                             "and Organization (OrganizationGroupMember) may have its own attributes.",
    'person-api': "A REST API for operations on Persons and their relationships in AMS. Persons may be related \n"
                  "to Identifiers, Contacts, Issues, Addresses, and can have Roles assigned to them by Organizations.",
    # 'role-api': "A REST API for operations on Roles and their relationships in AMS. Roles grant permissions to Persons on behalf"
    #                 " of Organizations.",
    # 'tag-api': "A REST API for operations on Tags and their relationships in AMS. Tags may be related \n"
                   # "to Organizations to help establish hierarchies or add other metadata.",
    # 'authorization-api': "An API for verifying authorization with AMS.",
    # 'authentication-api': "An API for authenticating with AMS."
}


def props_for_method(m: MethodDeclaration) -> dict:
    if perfec2.util.is_getbyuid_web_endpoint(m):
        print(f'{m.name} is_getbyuid_web_endpoint')
        return {
            'nickname': '"Retrieve xxx"',
            'value': '"Retrieve an existing xxx"',
            'notes': '"Retrieves an existing xxx by its uid. "',
            'response': 'Object.class',
            'code': 200
        }
    elif perfec2.util.is_deletebyuid_web_endpoint(m):
        print(f'{m.name} is_deletebyuid_web_endpoint')
        return {
            'nickname': '"Delete xxx"',
            'value': '"Delete an existing xxx"',
            'notes': '"Deletes an existing xxx by its uid. "',
            'response': 'Void.class',
            'code': 204
        }
    elif perfec2.util.is_updatebyuid_web_endpoint(m):
        print(f'{m.name} is_updatebyuid_web_endpoint')
        return {
            'nickname': '"Update xxx"',
            'value': '"Update an existing xxx"',
            'notes': '"Updates an existing xxx by its uid with the supplied properties. Unknown properties are ignored."',
            'response': 'Object.class',
            'code': 200
        }
    elif perfec2.util.is_create_web_endpoint(m):
        print(f'{m.name} is_create_web_endpoint')
        return {
            'nickname': '"Create xxx"',
            'value': '"Create a new xxx entity"',
            'notes': '"Creates a new xxx with the supplied properties. Unknown properties are ignored. "',
            'response': 'Object.class',
            'code': 201
        }
    elif perfec2.util.is_associate_web_endpoint(m):
        print(f'{m.name} is_associate_web_endpoint')
        return {
            'nickname': '"Associate xxx and yyy"',
            'value': '"Associate existing xxx and yyy"',
            'notes': '"Creates a relationship between existing xxx and yyy. "',
            'response': 'Object.class',
            'code': 200
        }
    elif perfec2.util.is_disassociate_web_endpoint(m):
        print(f'{m.name} is_disassociate_web_endpoint')
        return {
            'nickname': '"Associate xxx and yyy"',
            'value': '"Associate existing xxx and yyy"',
            'notes': '"Creates a relationship between existing xxx and yyy. "',
            'response': 'Void.class',
            'code': 204
        }
    elif perfec2.util.is_create_and_associate_web_endpoint(m):
        print(f'{m.name} is_create_and_associate_web_endpoint')
        return {
            'nickname': '"Create xxx and associate yyy"',
            'value': '"Create xxx and associate with an existing yyy"',
            'notes': '"Creates a new xxx and associates it with an existing yyy. "',
            'response': 'Object.class',
            'code': 201
        }
    elif perfec2.util.is_get_associations_web_endpoint(m):
        print(f'{m.name} is_get_associations_web_endpoint')
        return {
            'nickname': '"Retrieve xxx associated yyy"',
            'value': '"Retrieve existing yyys associated with xxx"',
            'notes': '"Retrieves existing yyyx associate with existing xxx. "',
            'response': 'Object.class',
            'code': 200
        }
    elif perfec2.util.is_get_type_by_key_web_endpoint(m):
        print(f'{m.name} is_get_type_by_key_web_endpoint')
        return {
            'nickname': '"Retrieve xxx Type by key"',
            'value': '"Retrieve existing xxx Type by key"',
            'notes': '"Retrieves existing xxx Type with a given key. "',
            'response': 'Object.class',
            'code': 200
        }
    elif perfec2.util.is_delete_type_by_key_web_endpoint(m):
        print(f'{m.name} is_delete_type_by_key_web_endpoint')
        return {
            'nickname': '"Delete xxx Type by key"',
            'value': '"Delete existing xxx Type by key"',
            'notes': '"Deletes existing xxx Type with a given key. "',
            'response': 'Object.class',
            'code': 204
        }
    elif perfec2.util.is_update_type_by_key_web_endpoint(m):
        print(f'{m.name} is_update_type_by_key_web_endpoint')
        return {
            'nickname': '"Update xxx Type by key"',
            'value': '"Update existing xxx Type by key"',
            'notes': '"Updates existing xxx Type with a given key. "',
            'response': 'Object.class',
            'code': 200
        }
    elif perfec2.util.is_create_type_by_key_web_endpoint(m):
        print(f'{m.name} is_create_type_by_key_web_endpoint')
        return {
            'nickname': '"Create new xxx Type by key"',
            'value': '"Create a new xxx Type by key"',
            'notes': '"Creates a new xxx Type with a given key. "',
            'response': 'Object.class',
            'code': 201
        }
    elif perfec2.util.is_associate_type_with_entity_web_endpoint(m):
        print(f'{m.name} is_associate_type_with_entity_web_endpoint')
        return {
            'nickname': '"Associate xxx Type with xxx"',
            'value': '"Associate an existing xxx Type with an existing xxx"',
            'notes': '"Associates an existing xxx Type with an existing xxx."',
            'response': 'Object.class',
            'code': 200
        }
    elif perfec2.util.is_disassociate_type_with_entity_web_endpoint(m):
        print(f'{m.name} is_disassociate_type_with_entity_web_endpoint')
        return {
            'nickname': '"Disassociate xxx Type from xxx"',
            'value': '"Disassociate an existing xxx Type from an existing xxx"',
            'notes': '"Disassociates an existing xxx Type from an existing xxx."',
            'response': 'Object.class',
            'code': 204
        }
    elif perfec2.util.is_get_type_associations_web_endpoint(m):
        print(f'{m.name} is_get_type_associations_web_endpoint')
        return {
            'nickname': '"Retrieve xxx by xxx Type key"',
            'value': '"Retrieve existing xxxs of given xxx Type by key"',
            'notes': '"Retrieves all xxx associated with existing xxx Type by key. "',
            'response': 'Object.class',
            'code': 200
        }
    else:
        print(f'{m.name} is unknown <<<========================')
        return {
            'nickname': '""',
            'value': '""',
                        'notes': '""',
            'response': 'Object.class',
            'code': 999
        }


def request_mapping_props(m: MethodDeclaration) -> dict:
    if perfec2.util.method_has_annotation(m, 'PostMapping'):
        post_mapping = perfec2.util.get_method_annotation(m, 'PostMapping')
        path = perfec2.util.get_annotation_property(post_mapping)
        return {'value': path, 'method': 'RequestMethod.POST'}

    if perfec2.util.method_has_annotation(m, 'GetMapping'):
        post_mapping = perfec2.util.get_method_annotation(m, 'GetMapping')
        path = perfec2.util.get_annotation_property(post_mapping)
        return {'value': path, 'method': 'RequestMethod.GET'}

    if perfec2.util.method_has_annotation(m, 'PutMapping'):
        post_mapping = perfec2.util.get_method_annotation(m, 'PutMapping')
        path = perfec2.util.get_annotation_property(post_mapping)
        return {'value': path, 'method': 'RequestMethod.PUT'}


def use_RequestMapping_only(lines: [str]) -> [str]:
    perfec2.replace_annotation_on_members(perfec2.this_clazz(), 'methods', lines,
                                          'PostMapping', 'RequestMapping', request_mapping_props, oneline=True)

def use_RestController_only(lines: [str]) -> [str]:
    if perfec2.get_class_annotation(perfec2.this_clazz(), 'Controller'):
        perfec2.remove_node_annotation(perfec2.this_clazz(), 'Controller', lines)
        perfec2.add_node_annotation(perfec2.this_clazz(), 'RestController', lines)


def add_link_to_readme():
    # todo
    pass


# fixme some methods are using @PutMapping or @GetMapping instead of @RequestMapping
def refactor_controller(lines: List[str]) -> List[str]:
    """
    within this method we have access to the lines of the file being processed
    and the compilation unit itself
    :param lines:   provided by perfec2.process_file()
    :return:
    """
    clazz = perfec2.this_clazz()
    print(f'annotating {clazz.name}')
    use_RestController_only(lines)
    use_RequestMapping_only(lines)
    do_swagger_annotations(lines)
    class_RequestMapping_produces_consumes(lines)

    return lines


def do_swagger_annotations(lines):
    perfec2.annotate_methods_having_annotation(perfec2.this_clazz(), lines, 'RequestMapping', 'ApiOperation', props_for_method)
    perfec2.add_import('io.swagger.annotations.ApiOperation', lines)


def class_RequestMapping_produces_consumes(lines):
    # fix class-level annotation
    try:
        req_mapping_anno = perfec2.get_class_annotation(perfec2.this_clazz(), 'RequestMapping')
        path = perfec2.util.get_annotation_property(req_mapping_anno)
        new_anno_props = {
            'value': path,
            'produces': '"application/json"',
            'consumes': '"application/json"',
        }
        perfec2.remove_node_annotation(perfec2.this_clazz(), 'RequestMapping', lines)
        perfec2.add_node_annotation(perfec2.this_clazz(), 'RequestMapping', lines, anno_props=new_anno_props, oneline=True)
    except Exception as e:
        print(traceback.format_exc())


def refactor_pom(xml_path: str, repo: str):
    new_plugins_lines = [
        '<plugin>\n',
        '    <groupId>io.swagger.codegen.v3</groupId>\n',
        '    <artifactId>swagger-codegen-maven-plugin</artifactId>\n',
        '    <version>3.0.14</version>\n',
        '    <executions>\n',
        '        <execution>\n',
        '            <phase>process-classes</phase>\n',
        '            <goals>\n',
        '                <goal>generate</goal>\n',
        '            </goals>\n',
        '            <configuration>\n',
        '                <inputSpec>${apidocs.directory}/swagger.json</inputSpec>\n',
        '                <language>html</language>\n',
        '                <output>${apidocs.directory}</output>\n',
        '            </configuration>\n',
        '        </execution>\n',
        '    </executions>\n',
        '</plugin>\n',
        '<plugin>\n',
        '    <groupId>com.github.kongchen</groupId>\n',
        '    <artifactId>swagger-maven-plugin</artifactId>\n',
        '    <version>${swagger-maven-plugin-version}</version>\n',
        '    <configuration>\n',
        '        <apiSources>\n',
        '            <apiSource>\n',
        '                <springmvc>true</springmvc>\n',
        '                <locations>com.coxautoinc.acctmgmt</locations>\n',
        '                <info>\n',
        '                    <title>${name}</title>\n',
        '                    <version>${build.version}</version>\n',
        '                    <description>\n',
        '                        {}\n'.format(repos[repo]),
        '                    </description>\n',
        '                    <contact>\n',
        '                        <email>accmt@coxautoinc.com</email>\n',
        '                        <name>Cox Auto Account Management Development Team</name>\n',
        '                        <url>Please contact the product group for Account Management</url>\n',
        '                    </contact>\n',
        '                    <license>\n',
        '                        <url>http://www.coxautoinc.com</url>\n',
        '                        <name>Cox Automotive, Inc.</name>\n',
        '                    </license>\n',
        '                </info>\n',
        '                <swaggerDirectory>${apidocs.directory}</swaggerDirectory>\n',
        '            </apiSource>\n',
        '        </apiSources>\n',
        '    </configuration>\n',
        '    <executions>\n',
        '        <execution>\n',
        '            <phase>compile</phase>\n',
        '            <goals>\n',
        '                <goal>generate</goal>\n',
        '            </goals>\n',
        '        </execution>\n',
        '    </executions>\n',
        '</plugin>\n']
    new_properties_lines = [
        '<swagger-maven-plugin-version>3.1.7</swagger-maven-plugin-version>\n',
        '<swagger.annotations.version>1.5.24</swagger.annotations.version>\n',
        '<apidocs.directory>${project.basedir}/src/main/resources/static/${name}</apidocs.directory>\n'
    ]
    with open(xml_path, 'r+') as pomfile:
        lines = pomfile.readlines()

        for i, line in enumerate(lines):
            if '</properties>' in line:
                lines = perfec2.util.match_indentation_and_insert(new_properties_lines, i, lines, indent_mod=4)
                break

        for i, line in enumerate(lines):
            if '</plugins>' in line:
                lines = perfec2.util.match_indentation_and_insert(new_plugins_lines, i, lines, indent_mod=4)
                break

        perfec2.util.write_file(lines, pomfile)


def main():
    for repo in repos:
        full_dir = f'{repos_root}/{repo}'
        for root, dirs, files in os.walk(full_dir):
            for f in files:
                if f.endswith('Controller.java'):
                    perfec2.process_file(os.path.join(root, f), refactor_controller)
                elif f == 'pom.xml':
                    refactor_pom(os.path.join(root, f), repo)
        # perfec2.util.mvn_clean_install(full_dir)
        # add_link_to_readme(full_dir)


if __name__ == '__main__':
    main()
