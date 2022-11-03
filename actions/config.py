import configparser

def getDBConfig(ini_file):
  print("[DB ini File]",ini_file)
  config = configparser.ConfigParser()
  config.read(ini_file)
  db_dir = config['SQLite']['db_dir']
  db_name = config['SQLite']['db_name']
  dbpath = f'{db_dir}/{db_name}'
  return dbpath

