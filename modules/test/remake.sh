#! /bin/sh
for i in *.mp3
do
  echo $i
  if [ ! "$i" = "lar.mp3" ]; then
    rm $i
  fi
done
cp lar.mp3 foo.mp3
