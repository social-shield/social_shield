#import modules necessary for reading data from CSV and JSON file
import pandas as pd
import json

class ReadData:
  """
  Class for loading a data from a file
  It can be used for CSV files and JSON files
  """

  def load_data(self, file_path):
    """
    method to load the data from a file

    :param file_path: Path of the file to be read from
    :type file_path: str

    The NotImplementedError is a signal to whoever is using this class
    that they need to subclass 'ReadData' 
    and implement their own version of the 'load_data()' method.
    """
    raise NotImplementedError("Subclasses must implement 'load_data()' function")
  
class ReadCSV(ReadData):
  """
  Instantiate a read operation from a CSV file

  'ReadData' class is taken as parameter for 'ReadCSV' file
  It can use all the methods from the ReadData class
  """

  def load_data(self, file_path):
    """
    Method to load the data from CSV file to pandas
    """
    return pd.read_csv(file_path)
  
class ReadJSON(ReadData):
  """
  Instantiate a read operation from a JSON file

  'ReadData' class is taken as parameter for ReadCSV file
  It can use all the methods from the ReadData class
  """

  def load_data(self, file_path):
    """
    Method to load data from JSON file 
    """

    with open(file_path, 'r') as jfile:
      data = json.load( jfile )
    return data
  
class Scams:
  """
  Acts as a wrapper around the functionality provided by the 'ReadCSV'
  """
  def __init__(self):
    """
    Constructor

    Instance variable 'loader' is initialized with instance of 'ReadCSV' class
    """
    self.loader = ReadCSV()
  
  def load_data(self, file_path):
    """
    Method responsible for loading data from a file
    Uses 'load_data()' method of 'ReadCSV' class

    :param file_path: Path of the file to be read from

    Stores the data in the instance 'self.loader'
    """
    return self.loader.load_data(file_path)
  
  def get_word_index(self, data):
    pass

class BiNetwork50:
  """
  Similar to Scams class but for the JSON file 'BiNetwork50'
  """
  def __init__(self):
    """
    Constructor

    Instance variable 'loader' is initialized with instance of 'ReadJSON' class
    """
    self.loader = ReadJSON()

  def load_data(self, file_path):
    """
    Method responsible for loading data from a file
    Uses load_data() method of 'ReadJSON' class

    :param file_path: Path of the file to be read from

    Stores the data in the instance 'self.loader'
    """
    return self.loader.load_data(file_path)
  
  def get_node_character(self):
    pass

class UniNetwork150:
  """
  Works the same as BiNetwork50
  """
  def __init__(self):
    """
    Constructor

    Instance variable 'loader' is initialized with instance of 'ReadJSON' class
    """
    self.loader = ReadJSON()

  def load_data(self, file_path):
    """
    Method responsible for loading data from a file
    Uses load_data() method of 'ReadJSON' class

    :param file_path: Path of the file to be read from

    Stores the data in the instance 'self.loader'
    """
    return self.loader.load_data(file_path)
  
  def get_node_character(self):
    pass

#Creating instances of the above classes
scams = Scams()
bi_net = BiNetwork50()
uni_net = UniNetwork150()

#Stores the objects in different instance variables
scams_data = scams.load_data(r'socialshield\datasets\scams.csv')
bi_net_data = bi_net.load_data(r'socialshield\datasets\BiNetwork50.json')
uni_net_data = uni_net.load_data(r'socialshield\datasets\UniNetwork150.json')

"""
Display and Test Cases
Given below are a few test cases where the data from the files are displayed
"""
#To display the first 5 rows from the 'scams.csv' file
print(scams_data.head())

#To display all the details from the 'scams.csv' file
print(scams_data)

#To display a random row from the 'scams.csv' file
data = pd.read_csv(r'socialshield\datasets\scams.csv')
row = data.sample(n = 1)
print(row,'\n')

#Display the first 5 nodes from the 'BiNetwork50.json' file
for key, value in list(bi_net_data.items())[:5]:
    print(f"Node {key}:")
    print(json.dumps(value, indent = 4))
print('\n')

#Display a specific node from 'UniNetwork150.json' file using node_id
node_id = '81'
if node_id in uni_net_data:
  print("Node: ", node_id)
  for key, value in uni_net_data[node_id].items():
    print(f"{key} :")
    print(json.dumps(value, indent = 3))

