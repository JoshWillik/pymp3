#! /bin/bash
for i in *
do
  echo $i
  if [[ ! "$i" == "lar.mp3" && ${i#*.} == "mp3" ]]; then
    echo ${i#*.}
    rm "$i"
    echo $i "deleted"
  fi
done
cp lar.mp3 foo.mp3
sleep 2m
