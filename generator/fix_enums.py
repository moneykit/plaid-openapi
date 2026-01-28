import json
import re
import textwrap
from pathlib import Path


def fix_enums():
    fixed = 0
    for p in Path("../skeleton/src/plaid_skel/models").glob("*.py"):
        code = p.read_text()
        code = code.split("# PRE-CLEANUP ENUM", maxsplit=2)
        if len(code) > 1:
            name = code[1].strip()
            # "if v" required because Plaid sometimes null in their enum list, for some reason
            model_data = json.loads(code[2])
            model_type = model_data['type']
            nullable = model_data.get("nullable", False)
            vals: list[str] = [v for v in model_data['enum'] if v]

            def clean(varStr):
                return re.sub('\\W|^(?=\\d)','_', varStr)
            names = [clean(v.upper()) for v in vals]

            assert model_type == "string", "Not setup to handle other enum types"

            fixed_enum = code[0].strip() + textwrap.dedent(f"""

            from enum import Enum
            """)

            if nullable:
                fixed_enum += textwrap.dedent(f"""

                            from pydantic import GetJsonSchemaHandler
                            from pydantic.json_schema import JsonSchemaValue
                            """)

            fixed_enum += textwrap.dedent(f"""


            class {name}(str, Enum):
            """)

            for name, value in zip(names, vals):
                assert name.isidentifier(), f"{name} is not a valid identifier"
                fixed_enum += f'    {name} = "{value}"\n'

            if nullable:
                fixed_enum += textwrap.dedent("""
                        # Nullable OpenAPI enum
                        @classmethod
                        def __get_pydantic_json_schema__(cls, field_schema: dict, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
                            schema = handler(field_schema)
                            schema["nullable"] = True
                            return schema
                """)

            p.write_text(fixed_enum)

            fixed = fixed + 1
    print(f"{fixed=}")


fix_enums()
