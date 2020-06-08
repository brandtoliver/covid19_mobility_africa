# Change dir
cd ~/HOPE/WorldCovid19/

# execute all python scripts
python pull_data/pull.py
python preprocess_everything.py;

# then build the website
cd covid19.compute.dtu.dk/static;
rsync -av data petem@thinlinc.compute.dtu.dk:/www/sites/covid19.compute.dtu.dk;
