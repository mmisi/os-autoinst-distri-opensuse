#!/bin/bash
#
# Prepare test catalog rst file by parsing *.pm files
#

TEST_REPO_BASE="https://github.com/os-autoinst/os-autoinst-distri-opensuse/tree/master/tests/security/"

cd ..
pwd

TESTCATFILE=doc/testcatalog.rst

echo -e "Test catalog\n============" > "$TESTCATFILE"

# find files which have #\ marker
for f in $(find ./ -type f -exec grep -il "^#\\\\" {} ';'); do
    echo "found documented file: $f"
    filename=$(basename "$f")
    filename="${filename%.*}"
    echo "Test name: $filename" >> "$TESTCATFILE"
    echo -e "\n\`source <$TEST_REPO_BASE${f#./*}>\`_\n" >> "$TESTCATFILE"

    # extract text between #\ and #/ markers and strip leading #
    sed -n '/#\\/, /#\//{ /#\\/! { /#\//! p } }' "$f" | sed 's/^#//g' >> "$TESTCATFILE"

done


