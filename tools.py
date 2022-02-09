import subprocess
import sys
command = sys.argv[0]

def search_text():
    result = subprocess.run(["grep","-rwl",sys.argv[2],sys.argv[3],])
switch_case = {
  "search_text": search_text,
  2: "summer",
  3: "autumn",
  4: "winter"
}

switch_case.get(sys.argv[1])()
