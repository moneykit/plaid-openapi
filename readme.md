## Plaid Compatibility Generator

This repo uses Plaid's OpenAPI spec to generate request and response models, for use in the MoneyKit-Plaid Compatibility API.

## Setup

- Install the [OpenAPI Generator](https://openapi-generator.tech/docs/installation)

## Generating the skeleton

To generate the skeleton, run `generator/regen.sh`, which:
- sets up our custom generator template
- downloads the latest Plaid spec
- preprocesses Plaid's spec to remove things we don't support
- generates the skeleton
- fixes the enums

## Using this Repo

It's a python package.  Import models from it.

In the moneykit-api repo, we currently require it in `pyproject.toml` with the commit SHA we want

```
plaid-openapi = { git = "https://github.com/moneykit/plaid-openapi", rev = "5722fdfd2742082d301206f69c29d69d72a56116" }
```

If you update this repo, you might also want to update the desired version in the moneykit-api repo.

**Note** that for easily testing changes locally, you can modify this repo, then go to moneykit-api
and there use `pip install -e ../plaid-openapi` (or wherever your local copy of this repo is).  That
will temporarily install your local repo into the moneykit-api virtualenv.

## Todo's
- include examples
- x-hidden-from-docs (include_in_schema)
- min/max/length/pattern (le, ge, etc.)
