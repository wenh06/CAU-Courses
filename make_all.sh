# assign "project_dir" as the parent directory of this script

project_dir="$(dirname "$(dirname "$(readlink -fm "$0")")")"

# iterate over folders in "project_dir" that contains a "make.sh" file

for dir in $(find $project_dir -name "make.sh" -exec dirname {} \;); do
    echo "Making in $dir"
    cd $dir
    bash ./make.sh
done
