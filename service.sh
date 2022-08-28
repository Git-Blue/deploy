#! /bin/sh

BIN="python ./control.py"
FILE=test.txt

action=$1
case "$action" in
stop)
    $BIN stop --file $FILE
    ;;
version)
    $BIN --version
    ;;
*)
    echo $action
    $BIN --help
    ;;
esac
