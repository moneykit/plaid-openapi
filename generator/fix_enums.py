from pathlib import Path
import json

def fix_enums():
    fixed = 0
    for p in Path("../skeleton/src/plaid_skel/models").glob("*.py"):
        code = p.read_text()
        code = code.split("# PRE-CLEANUP ENUM", maxsplit=2)
        if len(code) > 1:
            name = code[1].strip()
            # "if v" required because Plaid sometimes null in their enum list, for some reason
            vals = [v for v in json.loads(code[2])['enum'] if v]
            p.write_text("\n".join((
                code[0].strip(),
                "\nfrom strenum import StrEnum\n",
                f'{name} = StrEnum("{name}", names={vals})'
            )))
            fixed = fixed + 1
    print(f"{fixed=}")


fix_enums()