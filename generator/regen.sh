if [ -d "generator" ]
then pushd generator
fi

mkdir tmp

if [ ! -d "tmp/template" ]
then
    echo "Fetching and modifying fastapi template"
    openapi-generator author template -g python-fastapi -o tmp/template
    cp generator/model.mustache tmp/template
fi

if [ ! -f "tmp/2020-09-14.yml" ]
then
    echo "Downloading Plaid yaml"
    curl https://raw.githubusercontent.com/plaid/plaid-openapi/master/2020-09-14.yml > tmp/2020-09-14.yml
fi

echo "Preprocessing the plaid API yaml"
python preprocess.py

echo "Regenerating skeleton"
rm -rf ../skeleton/src/plaid_skel
JAVA_OPTS="-Dlog.level=error" openapi-generator generate -i tmp/preprocessed.yaml -o ../skeleton --package-name plaid_skel -g python-fastapi --skip-validate-spec --global-property models -t tmp/template 2> tmp/errors.txt
touch ../skeleton/src/__init__.py

echo "Postprocessing enums"
python fix_enums.py

popd
