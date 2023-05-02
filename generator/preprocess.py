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


def remove_unsupported_properties(spec: dict) -> None:
    remove_properties = {
        "LinkTokenCreateRequest": [
            "link_customization_name",
            "android_package_name",
            "institution_data",
            "account_filters",
            "eu_config",
            "institution_id",
            "payment_initiation",
            "deposit_switch",
            "employment",
            "income_verification",
            "auth",
            "transfer",
            "update",
            "identity_verification",
            "user_token",
            "investments",
        ],
        "LinkTokenCreateRequestUser": [
            "legal_name",
            "name",
            "ssn",
            "date_of_birth",
            "address",
            "id_number",
        ],
        "Item": [
            "consent_expiration_time",
            "update_type",
        ],
        "AccountBase": [
            "official_name",
            "verification_status",
            "persistent_account_id",
        ],
        "AccountBalance": [
            "unofficial_currency_code",
            "last_updated_datetime",
        ],
        "NumbersACH": [
            "can_transfer_in",
            "can_transfer_out",
        ],
        "Email": [
            "type",
        ],
        "TransactionsGetRequestOptions": [
            "include_original_description",
            "include_personal_finance_category_beta",
            "include_logo_and_counterparty_beta",
        ],
        "Transaction": [
            "pending_transaction_id",
            "unofficial_currency_code",
            "location",
            "payment_meta",
            "payment_channel",
            "account_owner",
            "authorized_date",
            "authorized_datetime",
        ],
    }

    for schema_name, properties_to_remove in remove_properties.items():
        path = f"components/schemas/{schema_name}/properties/"
        count = 0
        for prop in properties_to_remove:
            count += dpath.delete(spec, path + prop)
        print(f"Deleted {count} properties from {path}")


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
    remove_unsupported_properties(spec)

    print("writing yaml")
    with open(openapi_output_file, "w") as f:
        yaml.dump(spec, f, sort_keys=False)


if __name__ == "__main__":
    main()
