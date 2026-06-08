from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.greet_utils import build_message

DOCUMENTATION = """
  module: greet
  short_description: Returns a greeting message
  options:
    name:
      description: Name to greet
      required: true
    greeting:
      description: Greeting word to use
      default: Hello
"""


def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type="str", required=True),
            greeting=dict(type="str", default="Hello"),
        )
    )

    # build_message lives in module_utils/greet_utils.py
    message = build_message(module.params["name"], module.params["greeting"])
    module.exit_json(changed=False, message=message)


if __name__ == "__main__":
    main()
