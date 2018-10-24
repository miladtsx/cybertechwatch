#!/bin/bash

echo "Trying to install requirements ...\n"

printf "#!/bin/bash\n python ./main.py" > run.sh

printf "python-docx>=0.8.7\n feedparser>=5.2.1" > requirements.txt

printf "\nInstalling requirements ...\n"
python -m pip install -r requirements.txt 
#rm requirements.txt

printf "Done.\nNow execute run.sh\n"