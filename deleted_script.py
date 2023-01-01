#!/usr/bin/python3

import os
import time
from slack_sdk.webhook import WebhookClient
import argparse

def getArgs(): # get input argoman
    parser = argparse.ArgumentParser()
    parser.add_argument('-u' , '--url' , dest = 'slack_url' , action="store", type=str , help="add your slack token")
    parser.add_argument('-d' , '--days' , dest = 'n_days' , action="store", type=int , help="number of days you want store files")
    parser.add_argument('-l','--list', nargs='+', dest = 'directories' , help="your directories")
    return parser

args = getArgs().parse_args() 

if args.slack_url and args.n_days and args.directories: # set default input argoman.
    url = args.slack_url
    number_of_days = args.n_days
    list_directory = args.directories
else:
    url = ""
    number_of_days = 30
    list_directory = []

def create_path(list_directory): # create list from all files in input directory.
    list_of_files = []
    for i in list_directory:
        os.chdir(i)
        x = os.listdir()
        for j in x:
            list_of_files.append(f"{i}/{j}")
    return list_of_files

def deleted_files(day_in_sec , number_of_days ): # remove every files by input argoman in directories.
    deleted_list = []
    current_time = int(time.time())
    list_of_files = create_path(list_directory)
    for i in list_of_files:
        file_time = int(os.stat(i).st_mtime)
        if (file_time < current_time - (day_in_sec*number_of_days)):
            os.remove(i)
            deleted_list.append(i)
    return deleted_list

def send_result(url): # send result to slack channel
    webhook = WebhookClient(url)
    result = deleted_files(day_in_sec=86400 , number_of_days=number_of_days )
    result_lentgh = len(result)
    if result_lentgh <= 10:
        response = webhook.send(text=f"{str(result)} , {result_lentgh}")
    elif result_lentgh > 10:
        response = webhook.send(text=str(result[:-(result_lentgh/2)]))
        response = webhook.send(text=str(result[-(result_lentgh/2):]))

send_result(url)

