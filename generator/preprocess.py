import pathlib

import dpath
import yaml

SCRIPT_DIR = pathlib.Path(__file__).parent

print("reading yaml")
with open(SCRIPT_DIR / "tmp" / "2020-09-14.yml", "r") as f:
    y = yaml.safe_load(f)


# delete fields we don't yet support
# NOTE this just eliminates all fields with these names.
# E.g., it eliminates ClientProvidedTransaction.location, which we might one day want.
# If you need to be precise, use more exact expressions.

for loc in ["**/location",
            "**/payment_meta",
            "**/payment_channel"
            ]:
    try:
        count = dpath.delete(y, loc)
    except dpath.exceptions.PathNotFound:
        count = 0
    print("deleted", count, loc)


print("writing yaml")
with open("tmp/preprocessed.yaml", "w") as f:
    yaml.dump(y, f, sort_keys=False)
