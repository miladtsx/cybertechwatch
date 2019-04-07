#!/bin/bash

printf "Installing requirements ...\n"
printf "#!/bin/bash\n python ./main.py" > run.sh
printf "python-docx>=0.8.7\n feedparser>=5.2.1\n python-dateutil>=2.7.3\n" > requirements.txt

python -m pip install virtualenv --user
python -m virtualenv cyberNewsPyEnv
source cyberNewsPyEnv/bin/activate

python -m pip install -r requirements.txt
rm requirements.txt
chmod +x run.sh
./run.sh

printf "Done.\nFor later uses just do: ./run.sh\n"
