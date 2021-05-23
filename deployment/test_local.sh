#!/bin/bash
# install_locally.sh
# Install locally for testing

cd ../

# Remove the env dir if it exists
if [ -d "env" ]; then rm -rf env; fi

virtualenv -p python3 env
. env/bin/activate
pip install dist/rtsparty-*.tar.gz
pip install ipython

ipython
