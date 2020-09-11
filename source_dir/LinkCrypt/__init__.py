import string, random, io

class Error:
  def Error(message):
    print(f"\033[1;91m{message}")
    quit()

class Cryptor:
  def __init__(self):
    self.characters = string.printable

  def FileEncrypted(self, file=None):
    if file == None:
      Error.Error("File was not provided")
    if type(file) == str:
      with open(file) as f:
        content = ''.join(f.readlines())
      try:
        c = int(content[:2])
        return True
      except:
        try:
          c = int(content[:1])
          return True
        except:
          return False
    elif type(file) == io.TextIOWrapper:
      content = ''.join(file.readlines())
      try:
        c = int(content[:2])
        return True
      except:
        try:
          c = int(content[:1])
          return True
        except:
          return False
    else:
      Error.Error("File type is invalid.")
  
  def TextEncrypted(self, text=None):
    if text == None:
      Error.Error("Text was not provided.")
    if type(text) == str:
      try:
        c = int(text[:2])
        return True
      except:
        try:
          c = int(text[:1])
          return True
        except:
          return False
    else:
      Error.Error("Text is not of type string.")

  def Wrap(self, num1, num2, direction):
    if direction == "up":
      while True:
        if num1 > num2:
          num1 -= num2
        else:
          break
    elif direction == "down":
      while True:
        if num1 < 0:
          num1 += num2
        else:
          break
    else:
      Error.Error("Direction is invalid.")
    return num1
  
  def DecryptText(self, text=None):
    if text == None:
      Error.Error("Text was not provided.")
    if type(text) == str:
      try:
        offset = int(text[:2])
        text = text.replace(text[:2], "")
      except:
        offset = int(text[:1])
        text = text.replace(text[:1], "")
      chars = []
      for char in text:
        idx = self.characters.index(char)
        idx -= offset
        idx = self.Wrap(idx, len(self.characters)-1, "down")
        char = self.characters[idx]
        chars.append(char)
      chars = ''.join(chars)
      return chars
    else:
      Error.Error("Text is not of type string.")
  
  def DecryptFile(self, file=None):
    if file == None:
      Error.Error("File was not provided")
    if type(file) == str:
      with open(file) as f:
        content = ''.join(f.readlines())
      with open(file, "w") as f:
        content = self.DecryptText(content)
        f.write(content) 
    elif type(file) == io.TextIOWrapper:
      content = ''.join(file.readlines())
      content = self.DecryptText(content)
      file.write(content)
    else:
      Error.Error("File type is invalid.")
  
  def DecryptFiles(self, files=[]):
    if files == []:
      Error.Error("Files were not provided")
    if type(files) == list:
      for file in files:
        self.DecryptFile(file)
    else:
      Error.Error("Files were not put in list format.")

  def EncryptText(self, text=None):
    if text == None:
      Error.Error("Text was not provided.")
    if type(text) == str:
      offset = random.randint(1, len(self.characters))
      chars = []
      for char in text:
        idx = self.characters.index(char)
        idx += offset
        idx = self.Wrap(idx, len(self.characters)-1, "up")
        char = self.characters[idx]
        chars.append(char)
      chars = ''.join(chars)
      return str(offset) + chars
    else:
      Error.Error("Text is not of type string.")
  
  def EncryptFile(self, file=None):
    if file == None:
      Error.Error("File was not provided")
    if type(file) == str:
      with open(file) as f:
        content = ''.join(f.readlines())
      with open(file, "w") as f:
        content = self.EncryptText(content)
        f.write(content) 
    elif type(file) == io.TextIOWrapper:
      content = ''.join(file.readlines())
      content = self.EncryptText(content)
      file.write(content)
    else:
      Error.Error("File type is invalid.")
    
  def EncryptFiles(self, files=[]):
    if files == []:
      Error.Error("Files were not provided")
    if type(files) == list:
      for file in files:
        self.EncryptFile(file)
    else:
      Error.Error("Files were not put in list format.")
