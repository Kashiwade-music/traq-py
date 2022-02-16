#!/bin/sh

set -eux

if ! [ $# -eq 1 ]; then
    echo "Usage: ./generate.sh PACKAGE_VERSION"
    echo "e.g. ./generate.sh 3.0.0-0"
    exit 1
fi

PACKAGE_VERSION=$1

# clean
if [ -d ./out ]; then
  rm -rf ./out
fi

# build
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i https://raw.githubusercontent.com/traPtitech/traQ/master/docs/v3-api.yaml \
    -g python \
    -o /local/out \
    -c /local/config.yaml \
    -p packageVersion="${PACKAGE_VERSION}"
