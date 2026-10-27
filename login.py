# create a login in python
set -euo pipefail

declare -A USERS=(
  [admin]="password123"
)

MAX_ATTEMPTS=3

login() {
  local attempt username password expected remaining

  for ((attempt = 1; attempt <= MAX_ATTEMPTS; attempt++)); do
    read -r -p "Username: " username
    username="${username#"${username%%[![:space:]]*}"}"
    username="${username%"${username##*[![:space:]]}"}"

    read -r -s -p "Password: " password
    echo

    expected="${USERS[$username]:-}"
    if [[ -n "$expected" && "$password" == "$expected" ]]; then
      echo "Welcome, ${username}."
      return 0
    fi

    remaining=$((MAX_ATTEMPTS - attempt))
    if ((remaining > 0)); then
      echo "Invalid username or password. ${remaining} attempt(s) left."
    else
      echo "Too many failed attempts. Access denied."
    fi
  done

  return 1
}

login
