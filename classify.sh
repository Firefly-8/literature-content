#!/bin/sh
# Classify poems into grade subdirectories

BASE="content/poems"

# Primary: 一年级5 / 二年级15 / 三年级15 / 四年级15 / 五年级15 / 六年级9
classify_primary() {
    section_dir="$BASE/primary"
    grades="一年级 5 二年级 15 三年级 15 四年级 15 五年级 15 六年级 9"

    # Get sorted list of files
    files=$(ls "$section_dir"/*.md 2>/dev/null | xargs -n1 basename | sort -t'-' -k1 -n)
    idx=0

    set -- $grades
    while [ $# -ge 2 ]; do
        grade_name="$1"
        count="$2"
        shift 2

        mkdir -p "$section_dir/$grade_name"
        i=0
        while [ $i -lt $count ]; do
            file=$(echo "$files" | sed -n "$((idx+1))p")
            if [ -z "$file" ]; then
                break
            fi
            mv "$section_dir/$file" "$section_dir/$grade_name/$file"
            idx=$((idx+1))
            i=$((i+1))
        done
    done
}

# Middle: 七年级25 / 八年级26 / 九年级26
classify_middle() {
    section_dir="$BASE/middle"
    grades="七年级 25 八年级 26 九年级 26"

    files=$(ls "$section_dir"/*.md 2>/dev/null | xargs -n1 basename | sort -t'-' -k1 -n)
    idx=0

    set -- $grades
    while [ $# -ge 2 ]; do
        grade_name="$1"
        count="$2"
        shift 2

        mkdir -p "$section_dir/$grade_name"
        i=0
        while [ $i -lt $count ]; do
            file=$(echo "$files" | sed -n "$((idx+1))p")
            if [ -z "$file" ]; then
                break
            fi
            mv "$section_dir/$file" "$section_dir/$grade_name/$file"
            idx=$((idx+1))
            i=$((i+1))
        done
    done
}

# High: 高一30 / 高二32 / 高三33
classify_high() {
    section_dir="$BASE/high"
    grades="高一 30 高二 32 高三 33"

    files=$(ls "$section_dir"/*.md 2>/dev/null | xargs -n1 basename | sort -t'-' -k1 -n)
    idx=0

    set -- $grades
    while [ $# -ge 2 ]; do
        grade_name="$1"
        count="$2"
        shift 2

        mkdir -p "$section_dir/$grade_name"
        i=0
        while [ $i -lt $count ]; do
            file=$(echo "$files" | sed -n "$((idx+1))p")
            if [ -z "$file" ]; then
                break
            fi
            mv "$section_dir/$file" "$section_dir/$grade_name/$file"
            idx=$((idx+1))
            i=$((i+1))
        done
    done
}

echo "=== Classifying primary ==="
classify_primary
echo "=== Classifying middle ==="
classify_middle
echo "=== Classifying high ==="
classify_high
echo "=== Done ==="
