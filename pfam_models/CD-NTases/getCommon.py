from Bio import SearchIO;
from Bio import SeqIO;
import pandas as pd;
import os;
import sys;
import copy;
import requests;
import csv;

def parse_hmmer(path):
    hit_list = [];
    for item in SearchIO.parse(path, "hmmer3-tab"):
        for hit in item:
            split_file_name: list = hit.id.split("_");
            species: str = "_".join(split_file_name[:-1]);
            protein_name: str = split_file_name[-1];
            hit_list.append(hit.description.split(" ")[0]);
    return hit_list;

# eSMODS = set(parse_hmmer("./eSMODS/eSMODS_hmm_search.txt"));
# OAS = set(parse_hmmer("./OAS/OAS_hmm_search.txt"));
# Mab21 = set(parse_hmmer("./Mab21/Mab21_hmm_search.txt"))
# CD_NTases = set(parse_hmmer("./CD-NTases_hmm_search.txt"));

# print(len(CD_NTases));
# print(len(parse_hmmer("./CD-NTases_hmm_search.txt")))
# CD_NTase_map = {};

# def checkMatches(domain_set):
#     matches = [];
#     for element in domain_set:
#         if element in CD_NTases:
#             matches.append(element);
#     return matches;

# eSMODS_matches = checkMatches(eSMODS);
# OAS_matches = checkMatches(OAS);
# Mab21_matches = checkMatches(Mab21);            

# print(eSMODS_matches);
# print(OAS_matches);
# print(Mab21_matches);
