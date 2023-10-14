# assign "project_dir" as the parent directory of this script

project_dir="$(dirname "$(readlink -fm "$0")")"

echo "Project directory: $project_dir"

# iterate over folders in "project_dir" that contains a "make.sh" file

for dir in $(find $project_dir -name "make.sh" -exec dirname {} \;); do
    echo "Making in $dir"
    cd $dir
    bash ./make.sh
done
