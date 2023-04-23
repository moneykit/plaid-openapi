import pathlib
import sys

import dpath
import yaml

SCRIPT_DIR = pathlib.Path(__file__).parent


def expose_only_supported_products(spec: dict) -> None:
    path = "components/schemas/Products/enum"
    available: set[str] = set(dpath.get(spec, path))
    assert available, f"Missing {path}"
    supported = set(["assets", "auth", "balance", "identity", "transactions"])
    assert supported.issubset(available)
    dpath.set(spec, path, list(supported))


def expose_only_supported_country_codes(spec: dict) -> None:
    path = "components/schemas/CountryCode/enum"
    available: set[str] = set(dpath.get(spec, path))
    assert available, f"Missing {path}"
    supported = set(["US", "GB", "CA"])
    assert supported.issubset(available)
    dpath.set(spec, path, list(supported))


def main() -> None:
    print("reading yaml")
    if len(sys.argv) != 3:
        print("Usage: python preprocess.py OPENAPI_INPUT_FILE OPENAPI_OUTPUT_FILE")
        sys.exit(1)

    openapi_input_file = sys.argv[1]
    openapi_output_file = sys.argv[2]

    with open(openapi_input_file, "r") as f:
        spec = yaml.safe_load(f)

    expose_only_supported_products(spec)
    expose_only_supported_country_codes(spec)

    # delete fields we don't yet support
    # NOTE this just eliminates all fields with these names.
    # E.g., it eliminates ClientProvidedTransaction.location, which we might one day want.
    # If you need to be precise, use more exact expressions.
    for loc in ["**/location", "**/payment_meta", "**/payment_channel"]:
        try:
            count = dpath.delete(spec, loc)
        except dpath.exceptions.PathNotFound:
            count = 0
        print("deleted", count, loc)

    print("writing yaml")
    with open(openapi_output_file, "w") as f:
        yaml.dump(spec, f, sort_keys=False)


if __name__ == "__main__":
    main()
