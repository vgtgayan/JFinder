#!/bin/csh -f

setenv CERBERUS_HOME "/remote/cerberus/latest"
setenv PATH "/u/`whoami`/.local/bin/:$PATH"

bash $CERBERUS_HOME/bin/CMLP_jupyter.sh
