#! /bin/bash


#echo Hi... Welcome to the game MAHIMA
#sleep 1
#echo Can you recognize this image?
#sleep 1
#feh /home/mahima/test2.jpg
python3 speak.py
(feh /home/mahima/test6.jpg&) && (sleep 3 && pkill feh)
#./run2.sh
script -c "python3 recognize.py" files.txt #& script -c "python3 /home/mahima/game/tensorflow-for-poets-2/scripts/label_image.py --image test2.jpg" file.txt ; fg
#python3 recognize.py > files.txt
cd tensorflow-for-poets-2
python3 scripts/label_image.py --image test6.jpg > /home/mahima/game/file.txt
cd /home/mahima/game/search
python3 match.py
cd /home/mahima/game
sleep 2
./run2.sh
sleep 2
./run3.sh

