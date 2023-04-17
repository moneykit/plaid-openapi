from pathlib import Path
import re

# compares fields between generated models and hand-created models
def compare():
    for p1 in Path("skeleton/src/plaid_skel/models").glob("*.py"):
        try:
            p2 = Path("../moneykit-api/app/api_plaid_compatible/plaid_models/", p1.name)
            code1 = p1.read_text()
            fields1 = {name:(typ, default) for name, typ, default in re.findall("(\w+): (.+?) = Field\(.+(default=[^,)]+)?", code1)}
            code2 = p2.read_text()
            fields2 = {name:(typ, default) for name, typ, default in re.findall("(\w+): (.+?) = Field\(.+(default=[^,)]+)?", code2)}
            for n, (t, d) in fields1.items():
                if n not in fields2:
                    print(f"{p1.name} field {n}: {t} is not in plaid_models")
                    continue
                t2, d2 = fields2[n]
                if t != t2:
                    print(f"{p1.name} field {n}: {t} is {t2} in plaid_models")
                if d != d2:
                    print(f"{p1.name} field {n} default is {d} but {d2} in plaid_models")
            for n2, (t2, d2) in fields2.items():
                if n2 not in fields1:
                    print(f"{p1.name} field {n2} is not in generated model")
        except FileNotFoundError:
            pass


compare()