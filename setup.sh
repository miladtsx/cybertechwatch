#!/bin/bash

echo "Trying to install requirements ...\n"

sudo apt install python;
sudo apt install python-pip;

printf "#!/bin/bash\n python ./main.py" > run.sh

printf "python-docx>=0.8.7\n feedparser>=5.2.1" > requirements.txt

printf "\nInstalling requirements ...\n"
python -m pip install -r requirements.txt 
rm requirements.txt

printf "Done.\nNow execute chmod +x run.sh then execute ./run.sh\n"