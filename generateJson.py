import os, sys
import json

#Make sure PCBench and PCART are located at the same directory level
#|
#|---PCART
#|---PCBench
#    |---Benchmark
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))
from PCART.Path.getPath import Path
 
print("Generating json files for PCART...")
pathObj=Path('D') #First level subdirectories
pathObj.getPath(f"/home/nuaa/Projects/PCBench/Benchmark") #PCBench's path
libPath=pathObj.path
for it in libPath: #Traverse each lib
    pathObj2=Path('D')
    pathObj2.getPath(it)
    apiPath=pathObj2.path
    libName=it.split('/')[-1]
    for p in apiPath: #Traverse each API in the lib
        s=p.split('/')[-1]
        apiName=s.split('@')[0].split('.')[-1]
        currentVersion=s.split('@')[-1].split('-')[0] 
        targetVersion=s.split('@')[-1].split('-')[-1] 
        pathObj3=Path('D')
        pathObj3.getPath(p)
        examplePath=pathObj3.path
        configDict={}
        for exp in examplePath:
            label=exp[-2:]
            jsonPath=f"{exp}/{apiName}{label}.json"
            configDict['projPath']=exp
            configDict['runCommand']=f"python {apiName}{label}.py"
            configDict['runFilePath']=""
            configDict['libName']=libName
            configDict['currentVersion']=currentVersion
            configDict['targetVersion']=targetVersion
            configDict['currentEnv']=f"/dataset/zhang/anaconda3/envs/{libName}{currentVersion}" #Change to your local Conda environment
            configDict['targetEnv']=f"/dataset/zhang/anaconda3/envs/{libName}{targetVersion}" #Change to your local Conda environment
            with open(jsonPath,'w') as fw:
                json.dump(configDict,fw,indent=4,ensure_ascii=False) 
    
    print(libName)
print("Done")
