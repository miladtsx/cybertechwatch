#!/bin/bash

printf "Installing requirements ...\n"
printf "#!/bin/bash\n source cyberNewsPyEnv/bin/activate\n python ./main.py\n deactivate" > run.sh
printf "python-docx>=0.8.7\n feedparser>=5.2.1\n python-dateutil>=2.7.3\n" > requirements.txt

python -m pip install virtualenv --user
python -m virtualenv cyberNewsPyEnv
source cyberNewsPyEnv/bin/activate

python -m pip install -r requirements.txt
rm requirements.txt
chmod +x run.sh

printf "Done.\n\nRun './run.sh' to get latest cybernews.\n"
