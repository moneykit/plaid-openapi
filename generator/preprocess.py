import pathlib
import sys

import dpath
import yaml

SCRIPT_DIR = pathlib.Path(__file__).parent


def main() -> None:
    print("reading yaml")
    if len(sys.argv) != 3:
        print("Usage: python preprocess.py OPENAPI_INPUT_FILE OPENAPI_OUTPUT_FILE")
        sys.exit(1)

    openapi_input_file = sys.argv[1]
    openapi_output_file = sys.argv[2]

    with open(openapi_input_file, "r") as f:
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
    with open(openapi_output_file, "w") as f:
        yaml.dump(y, f, sort_keys=False)


if __name__ == "__main__":
    main()