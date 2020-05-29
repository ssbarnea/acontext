# This is a fake {m} module used to make ansible(-lint) happy
from ansible.module_utils.basic import AnsibleModule


def main():
    return AnsibleModule(
        argument_spec=dict(
            data=dict(default=None),
            path=dict(default=None, type=str),
            file=dict(default=None, type=str),
        )
    )
