import os

from ticket import app
# On IBM Cloud Cloud Foundry, get the port number from the environment variable PORT
# When running this app on the local machine, default the port to 8000
port = int(os.getenv('PORT', 8000))
os.system("init_db.py")

if __name__ == '__main__':
  app.run(host='0.0.0.0',port=port)
