# -*- coding: utf-8 -*-
'''
Author: moxi
Date: 2022-03-03 13:12:54
LastEditTime: 2022-03-03 15:02:13
Description: 由官方的ModMaker修改而成

Copyright (c) 2022 by moxi/ICEJADE, All Rights Reserved. 
'''

import sys
import uuid
import os
import logging
import shutil
import stat

OUTPUT_FOLDER = "output"
TEMPLATE_FOLDER = "data"
NEW_UUID_1 = str(uuid.uuid1())
NEW_UUID_2 = str(uuid.uuid1())
NEW_UUID_3 = str(uuid.uuid1())
NEW_UUID_4 = str(uuid.uuid1())

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def MakeMod(teamName, modName):
    logging.info("Make Mod TeamName:%s ModName:%s " % (teamName, modName))
    logging.info("uuid1:[%s] uuid2:[%s] uuid3:[%s] uuid4:[%s]" % (NEW_UUID_1, NEW_UUID_2, NEW_UUID_3, NEW_UUID_4))
    folder = os.path.exists(OUTPUT_FOLDER)
    if not folder:
        os.makedirs(OUTPUT_FOLDER)
        logging.warn("OUTPUT_FOLDER is not exists")
        logging.info("create output folder:%s" % OUTPUT_FOLDER)

    teamName = teamName[0] + teamName[1:]
    destMod = teamName + modName
    logging.info(destMod)

    def remove_readonly(func, path, _):
        os.chmod(path, stat.S_IWRITE)
        func(path)

    logging.info("copy folder from %s to %s" % (TEMPLATE_FOLDER, os.path.join(OUTPUT_FOLDER,destMod)))
    destFolder = os.path.join(OUTPUT_FOLDER, destMod)
    if os.path.exists(destFolder):
        logging.info("remove %s" % destFolder)
        shutil.rmtree(destFolder, onerror=remove_readonly)
    shutil.copytree(TEMPLATE_FOLDER, destFolder)

    # 遍历替换文件内容
    for path, dirList, fileList in os.walk(destFolder, topdown=False):

        for file in fileList:
            filePath = os.path.join(path, file)
            # 替换文本内容
            if filePath.find("pack_icon") == -1:
                with open(filePath) as f:
                    contents = f.read()
                    f.close()
                newContents = contents

                if filePath.find(".py") != -1:
                    newContents = replaceContents(newContents,filePath, teamName, modName)


                if file == ("pack_manifest.json"):
                    newContents = replaceUUID(newContents)
                    logging.info("replace uuid %s" % filePath)
    
                with open(filePath, 'w') as f:
                    f.write(newContents)
                    f.close()

                newFilePath = replaceContents(file,filePath, teamName, modName)
                newFilePath = os.path.join(path, newFilePath)
                if newFilePath != filePath:
                    logging.info("File rename from %s to %s" % (filePath, newFilePath))
                    os.rename(filePath, newFilePath)

        for dir in dirList:
            dirPath = os.path.join(path, dir)
            newDirPath = replaceContents(dir, dirPath,teamName, modName)
            newDirPath = os.path.join(path, newDirPath)
            if newDirPath != dirPath:
                logging.info("Dir rename from %s to %s" % (dirPath, newDirPath))
                os.rename(dirPath, newDirPath)
        logging.info("Done.")
                
def replaceContents(origin,filePath, teamName, modName):
    ret = origin.replace("NeteaseMod_Temp", "%s_%s" % (teamName,modName))
    ret = ret.replace("template", modName[0].lower() + modName[1:])
    ret = ret.replace("Template",teamName + modName[0].upper() + modName[1:])
    logging.info("replace %s" % filePath)
    return ret

def replaceUUID(contents):
    ret = contents.replace("BEHAVIOR_HEADER_UIID", NEW_UUID_1)
    ret = ret.replace("BEHAVIOR_MODULE_UUID", NEW_UUID_2)
    ret = ret.replace("RESOURCE_HEADER_UUID", NEW_UUID_3)
    ret = ret.replace("RESOURCE_MODULE_UUID", NEW_UUID_4)
    return ret

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        logging.info("format error!")
    else:
        MakeMod(sys.argv[1], sys.argv[2])
