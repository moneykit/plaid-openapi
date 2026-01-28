import pathlib
import sys

import dpath
import yaml

SCRIPT_DIR = pathlib.Path(__file__).parent


def expose_only_supported_products(spec: dict) -> None:
    path = "components/schemas/Products/enum"
    available: set[str] = set(dpath.get(spec, path))
    assert available, f"Missing {path}"
    supported = set(["auth", "balance", "identity", "transactions"])
    assert supported.issubset(available)
    dpath.set(spec, path, list(supported))


def expose_only_supported_country_codes(spec: dict) -> None:
    path = "components/schemas/CountryCode/enum"
    available: set[str] = set(dpath.get(spec, path))
    assert available, f"Missing {path}"
    supported = set(["US", "GB", "CA"])
    assert supported.issubset(available)
    dpath.set(spec, path, list(supported))


def remove_unsupported_products(spec: dict) -> None:
    # schema pattern -> endpoint path pattern
    # key: pattern to match in schema names (e.g., "Beacon" matches "BeaconUser")
    # value: pattern to match in endpoint paths (e.g., "/beacon/" matches "/beacon/user/create")
    unsupported_products = {
        "Beacon": "/beacon/",
        "CRA": "/cra/",
        "Check": "/check/",
        "ConsumerReport": "/consumer_report/",
        "Credit": "/credit_",
        "AssetReport": "/asset_report/",
        "PaymentInitiation": "/payment_initiation/",
        "DepositSwitch": "/deposit_switch/",
        "Income": "/income/",
        "Employment": "/employment/",
        "Transfer": "/transfer/",
        "IdentityVerification": "/identity_verification/",
        "WatchlistScreening": "/watchlist_screening/",
        "Monitor": "/monitor/",
        "DashboardUser": "/dashboard_user/",
        "Application": "/application/",
        "Relay": "/relay/",
        "Layer": "/layer/",
        "Network": "/network/",
        "VirtualAccount": "/virtual_account",
    }
    
    paths_to_remove = []
    for path in spec.get("paths", {}).keys():
        for schema_pattern, path_pattern in unsupported_products.items():
            if path_pattern in path:
                paths_to_remove.append(path)
                break
    
    for path in paths_to_remove:
        del spec["paths"][path]
    
    schemas_to_remove = []
    for schema_name in list(spec.get("components", {}).get("schemas", {}).keys()):
        for schema_pattern in unsupported_products.keys():
            if schema_pattern in schema_name:
                schemas_to_remove.append(schema_name)
                break
    
    for schema_name in schemas_to_remove:
        del spec["components"]["schemas"][schema_name]
    
    print(f"Removed {len(paths_to_remove)} unsupported endpoints and {len(schemas_to_remove)} unsupported schemas")


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
            # "deposit_switch",
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
            "include_personal_finance_category_beta",
            "include_logo_and_counterparty_beta",
        ],
        "TransactionsSyncRequestOptions": [
            "include_logo_and_counterparty_beta",
        ],
        "TransactionBase": [
            "unofficial_currency_code",
            "check_number",
            "location",
            "payment_meta",
            "pending_transaction_id",
            "account_owner",
            "transaction_type",
            "logo_url",
            "website",
        ],
        "Transaction/allOf/[1]": [
            "payment_channel",
            "authorized_date",
            "authorized_datetime",
            "transaction_code",
            "counterparties",
            "personal_finance_category_icon_url",
        ],
        "InstitutionsGetByIdRequest": [
            "country_codes",
        ],
        "InstitutionsGetByIdRequestOptions": [
            "include_optional_metadata",
            "include_status",
            "include_auth_metadata",
            "include_payment_initiation_metadata",
        ],
        "Institution": [
            "products",
            "logo",
            "routing_numbers",
            "dtc_numbers",
            "oauth",
            "status",
            "payment_initiation_metadata",
            "auth_metadata",
        ],
    }

    for schema_name, properties_to_remove in remove_properties.items():
        path = f"components/schemas/{schema_name}/properties/"
        count = 0
        for prop in properties_to_remove:
            count += dpath.delete(spec, path + prop)
        print(f"Deleted {count} properties from {path}")


def add_properties_as_required(spec: dict) -> None:
    required_properties = {
        "LinkTokenCreateRequest": [
            "redirect_uri",
        ],
    }

    for schema_name, required_properties in required_properties.items():
        path = f"components/schemas/{schema_name}/required"
        count = 0
        for prop in required_properties:
            existing_req_props: set[str] = set(dpath.get(spec, path))
            assert existing_req_props, f"Missing {path}"
            existing_req_props.add(prop)
            dpath.set(spec, path, list(existing_req_props))
        count += len(prop)
        print(f"Added {count} properties as required to {path}")


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
    remove_unsupported_products(spec)
    remove_unsupported_properties(spec)
    add_properties_as_required(spec)

    print("writing yaml")
    with open(openapi_output_file, "w") as f:
        yaml.dump(spec, f, sort_keys=False)


if __name__ == "__main__":
    main()
