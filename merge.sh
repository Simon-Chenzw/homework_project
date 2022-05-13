usage() {
    cat <<USAGE
Usage:
    $(basename $0) repo url branch

    repo        The name of the existing repository
    url         The url of the existing repository
    branch      The name of the new branch

USAGE
    exit 0
}

[ -z $1 ] && { usage; }

repo=$1
repo_url=$2
branch=$3

git remote add $repo $repo_url
git fetch $repo
git branch $branch $repo/master
git push -u origin $branch
