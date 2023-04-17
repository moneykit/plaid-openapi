## Plaid Compatibility Generator

This repo uses Plaid's OpenAPI spec to generate request and response models, for use in the MoneyKit-Plaid Compatibility API.

## Setup

- Install the [OpenAPI Generator](https://openapi-generator.tech/docs/installation)

## Generating the skeleton

To generate the skeleton, run `generator/regen.sh`, which:
- sets up our custom generator template
- download the latest plaid spec
- preprocesses Plaid's spec to remove things we don't support
- generates the skeleton
- fixes the enums

## Using this Repo

It's a python package.  Import models from it.


## Todo's
- include examples
- x-hidden-from-docs (include_in_schema)
- min/max/length/pattern (le, ge, etc.)
