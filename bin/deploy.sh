#!/bin/bash
shopt -s nullglob

ENVIRONMENTS=( hosts/* )
ENVIRONMENTS=( "${ENVIRONMENTS[@]##*/}" )

show_usage() {
  echo "Usage: deploy <environment> <site name> [options]

<environment> is the environment to deploy to ("staging", "production", etc)
<site name> is the site to deploy (name defined in "sites")
[options] is any number of parameters that will be passed to ansible-playbook

Available environments:
`( IFS=$'\n'; echo "${ENVIRONMENTS[*]}" )`

Examples:
  deploy staging example.com
  deploy production example.com
  deploy staging example.com -vv -T 60
"
}

[[ $# -lt 2 ]] && { show_usage; exit 127; }

for arg
do
  [[ $arg = -h ]] && { show_usage; exit 0; }
done

ENV="$1"; shift
SITE="$1"; shift
EXTRA_PARAMS=$@
DEPLOY_CMD="ansible-playbook deploy.yml -e env=$ENV -e site=$SITE $EXTRA_PARAMS"
HOSTS_FILE="hosts/$ENV"

if [[ ! -e $HOSTS_FILE ]]; then
  echo "Error: $ENV is not a valid environment ($HOSTS_FILE does not exist)."
  echo
  echo "Available environments:"
  ( IFS=$'\n'; echo "${ENVIRONMENTS[*]}" )
  exit 1
fi

$DEPLOY_CMD
