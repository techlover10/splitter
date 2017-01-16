#!/usr/bin/python3

# Set the directories here
import sys, os
INPUT_DIR = 'data/'
OUT_DIR = 'split_data/'

# Set the source data files here
in_file_name = 'example.txt'
users_file = 'example_users.txt'

data = open(INPUT_DIR + in_file_name).readlines()
names = open(INPUT_DIR + users_file).readlines()

# Starting user value - if there is no username as the first message, it will save
# the messages into "start_null".txt until it finds a known user
curr_user = "start_null" 
for line in data:
    if line in names:
        curr_user = line
    else:
        open(OUT_DIR + curr_user.strip('\n') + '.txt', 'a').write(line)
