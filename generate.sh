#!/bin/sh

set -eux

PACKAGE_VERSION="${PACKAGE_VERSION:=3.0.0}"

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
