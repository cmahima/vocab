#! /bin/bash
echo Can you recognize this image?
python3 speak2.py
(feh /home/mahima/test5.jpg&) && (sleep 3 && pkill feh)
#./run2.sh
script -c "python3 recognize.py" files.txt #& script -c "python3 /home/mahima/game/tensorflow-for-poets-2/scripts/label_image.py --image test2.jpg" file.txt ; fg
#python3 recognize.py > files.txt
cd tensorflow-for-poets-2
python3 scripts/label_image.py --image test5.jpg > /home/mahima/game/file.txt
cd /home/mahima/game/search
python3 match.py
cd /home/mahima/game
