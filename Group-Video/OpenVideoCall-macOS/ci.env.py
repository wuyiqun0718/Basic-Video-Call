#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os

def main():
    #if need reset
    SDK_URL = "https://download.agora.io/sdk/release/Agora_Native_SDK_for_Mac_v2_9_1_FULL.zip?_ga=2.144511669.1414964891.1571043871-5559409.1503304822"
    TARGET_LIBS_ZIP = "agora_sdk.zip"
    TARGET_INTERNAL_FOLDER = "agora_sdk"
    
    #if need reset
    ZIP_STRUCTURE_FOLDER = "Agora_Native_SDK_for_Mac_FULL/libs"
    FRAMEWORK_NAME = "AgoraRtcEngineKit.framework"
    APP_NAME = "OpenVideoCall"

    wget = "wget -q " + SDK_URL + " -O " + TARGET_LIBS_ZIP
    os.system(wget)
    
    unzip = "unzip -q " + TARGET_LIBS_ZIP + " -d " + TARGET_INTERNAL_FOLDER
    os.system(unzip)
    
    mv = "mv -f " + TARGET_INTERNAL_FOLDER + "/" + ZIP_STRUCTURE_FOLDER + "/" + FRAMEWORK_NAME + " \"" + APP_NAME +"\""
    os.system(mv)

    appId = ""
    if "AGORA_APP_ID" in os.environ:
        appId = os.environ["AGORA_APP_ID"]
    token = ""

    #if need reset
    f = open("./OpenVideoCall/KeyCenter.swift", 'r+')
    content = f.read()

    #if need reset
    appString = "\"" + appId + "\""
    tokenString = "\"" + token + "\""
    contentNew = re.sub(r'<#Your App Id#>', appString, content)
    contentNew = re.sub(r'<#Temp Access Token#>', tokenString, contentNew)
    f.seek(0)
    f.write(contentNew)
    f.truncate()


if __name__ == "__main__":
    main()
