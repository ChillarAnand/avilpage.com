<!--
.. title: Grip On Grep
.. slug: grip-on-grep
.. date: 2018-11-08 12:31:03 UTC+05:30
.. tags: draft
.. category:
.. link:
.. description: 20+ pratical tips to master grep command line utility
.. type: text
-->


grep 'regexp' filename

ps -ef | grep firefox
tail -f /var/log/messages | grep WARNING

-i, --ignore-case

-l, --files-with-matches

-o, --only-matching

-n, --line-number

 -A 3
 -B 3
 -C 3
cat filename | grep regexp | grep regexp2
cat filename | grep regexp | grep -v regexp2

grep a input | grep b | grep -v c | grep d

awk '/a/ && /b/ && !/c/ && /d/' input

# Antipatterns

## Grep directly
cat book.txt | grep 'quickly'
grep 'quickly' book.txt

## Get grep count

cat book.txt | grep 'quickly' | wc -l
cat book.txt | grep 'quickly' -c

## Only string match

grep "string" filename
grep -F "string" filename


grep -f pattern.txt file.txt


$ grep -v -e "a" -e "b" -e "c" test-file.txt

exclude grep in ps
ps aux | grep "[f]nord"
pgrep fnord

zgrep
ngrep
fgrep
egrep
123
