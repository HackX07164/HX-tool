import os,sys,time
############style####################
# Set Colors ######

N = '\033[0m'

W = '\033[1;37m'

B = '\033[1;34m'

R = '\033[1;31m'

G = '\033[1;32m'

Y = '\033[1;33m'

C = '\033[1;36m'

##################
os.system ("clear")
print (R+"""
         .-""-.
        / .--. \\
       / /    \ \\
       | |    | |
       | |.-""-.|
       ///`.::::.`\
       
       |||::/  \::;
       ||;::\__/::;
       \ \.::::::/
        `":-..-"`
        
""")

H1 = input (R+'❯'+Y+'❯'+G+'❯ '+C)
time.sleep(1)
print (R+' R '+Y+'u '+G+'n '+B+'n '+N+'i '+C+'n '+G+'g .'+R+'.'+Y+'.')
time.sleep(3)
if H1 == "HX-WE code S":
        os.system ("python HX-WE.py")
