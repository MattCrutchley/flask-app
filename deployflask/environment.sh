#! /bin/bash
sudo apt-get update 
sudo apt-get install mysql-server
sudo apt-get install python3
sudo apt-get install python3-venv
sudo apt-get install pip3 -y
echo "enter name for database"
read dbname
echo "enter username for new mysql user"
read sqluser
echo "enter password for new mysql user"
read sqlpass
cd 
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
export DATABASE_URI="mysql+pymysql://${sqluser}:${sqlpass}@127.0.0.1/${dbname}"
echo "enter SECRET_KEY"
read SKEY
export SECRET_KEY="${SKEY}


