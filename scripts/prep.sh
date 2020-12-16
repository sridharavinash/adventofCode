#!/bin/bash
# usage: ./prep.sh python/2020/day12
set -e

if [ $# -eq 0 ]; then
  echo "usage: ./prep.sh python/2020/day31"
  echo 
  exit 1
fi

RELATIVE_PATH=$1
DAY=$(basename "$RELATIVE_PATH")

echo "Creating ${RELATIVE_PATH}..."
mkdir -p "$RELATIVE_PATH"

echo "Creating files..."

cat <<EOF > "$RELATIVE_PATH/$DAY.py" 
import itertools

def process_input_file(filename):
  for l in open(filename):
    line = l.strip()
    yield line

def part1(input):
  pass

def part2(input):
  pass

if __name__ == "__main__":
  inp = process_input_file("test.txt")
  part1(inp)
  #part2(inp)
EOF

touch "$RELATIVE_PATH/test.txt"
touch "$RELATIVE_PATH/input.txt"




