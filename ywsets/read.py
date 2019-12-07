def read():
  d = {}
  with open('metadata','r') as f:
    for line in f:
      line = line.strip()
      name,location = line.split(':')
      d[name] = location

  return d

def readset(s):
  d = read()
  return d[s]
