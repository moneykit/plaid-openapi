set -e
set -o pipefail

GENERATOR_VERSION=v6.5.0
PACKAGE_NAME="plaid_skel"
CONTAINER_NAME="plaid-skel-builder"
DOCKER_OUTPUT_DIR="/tmp/skeleton"

openapi_generator()
{
    set +e
    docker rm $CONTAINER_NAME 2> /dev/null
    set -e
    docker run \
        --name $CONTAINER_NAME \
        -v "${PWD}/":/generator_input/ \
        -e JAVA_OPTS="-Dlog.level=error" \
        openapitools/openapi-generator-cli:$GENERATOR_VERSION \
        "$@"
}


if [ -d "generator" ]
then pushd generator
fi

mkdir -p tmp

if [ ! -d "tmp/template" ]
then
    echo "Fetching fastapi template"
    openapi_generator author template -g python-fastapi -o /generator_input/tmp/template
fi

if [ ! -f "2020-09-14.yml" ]
then
    echo "Downloading latest Plaid yaml"
    curl https://raw.githubusercontent.com/plaid/plaid-openapi/master/2020-09-14.yml > 2020-09-14.yml
fi

echo "modifying fastapi template with customized_template"
cp customized_template/model.mustache tmp/template

echo "Preprocessing the plaid API yaml"
python preprocess.py 2020-09-14.yml 2020-09-14-processed.yml

echo "Regenerating skeleton"
rm -rf ../skeleton/src/plaid_skel

openapi_generator \
    generate -i /generator_input/2020-09-14-processed.yml \
    -g python-fastapi  \
    --package-name $PACKAGE_NAME \
    --skip-validate-spec \
    --global-property models \
    --template-dir /generator_input/tmp/template/ \
    -o $DOCKER_OUTPUT_DIR \
    2> tmp/errors.txt

docker cp $CONTAINER_NAME:$DOCKER_OUTPUT_DIR ../
touch ../skeleton/src/plaid_skel/__init__.py
touch ../skeleton/src/plaid_skel/py.typed

echo "Postprocessing enums"
python fix_enums.py

popd
