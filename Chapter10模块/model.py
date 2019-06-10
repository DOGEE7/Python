import sys                                        # 1                                               # 1# 1
import os                                         # 2                                               # 2#10
import webbrowser                                 # 3                                               # 3#11
                                                  # 4                                               # 4#100
args = sys.argv[1:]                               # 5                                               # 5#101
print(' '.join(reversed(args)))                   # 6                                               # 6#110
# python model.py this is a sentence              # 7                                               # 7#111
os.system(r'C:\"Program Files (x86)"\Google\Chrome\Application\chorme.exe')# 8                      # 8#1000
# os.startfile(r'C:\Program Files (x86)\Google\Chrome\Application\chorme.exe')# 9                   # 9#1001
webbrowser.open("https://docs.python.org/3/library/")#10                                            #10#1010
