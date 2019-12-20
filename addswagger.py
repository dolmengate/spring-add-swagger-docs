import os
import sys
from typing import List

cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(1, os.path.join(cwd, '..', 'perfec2'))

import perfec2

repos_root = '/Users/sroman/repos/'
repos = [
    # 'aa-cfr-api',
    # 'aa-com-api',
    # 'aa-con-api',
    # 'aa-iss-api',
    # 'aa-per-api',
    # 'aa-prl-api',
    # 'address-api',
    # 'ams-search-api',
    # 'apppolicy-api',
    # 'contact-api',
    # 'identifier-api',
    # 'issue-api',
    # 'organization-api',
    # 'organizationgroup-api',
    # 'person-api',
    # 'role-api',
    # 'tag-api'
    # 'issuesby100m-api',
    # 'issuesby5m-api',
    # 'authorization-api',
    # 'authentication-api'
]


def refactor_controller(lines: List[str]):
    pass


def main():
    for repo in repos:
        for root, dirs, files in os.walk(f'{repos_root}/{repo}/src/'):
            for f in files:
                if f.endswith('.java'):
                    perfec2.process_file(os.path.join(root, f), refactor_controller)


if __name__ == '__main__':
    main()
