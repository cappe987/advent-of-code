

do_day() {
	cd $1
	echo "===== Day $1 ====="
	python3 main.py
	cd ..
}

if [ "$#" -ne 0 ]; then
	do_day $1
	exit 0
fi

for i in $(seq 1 25); do
	dir=$(printf "%02d" $i)
	if [ -d "$dir" ]; then
		do_day $dir
	fi
done
