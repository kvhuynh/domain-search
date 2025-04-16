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

alpha_beta = set(parse_hmmer("./IFN-alpha-beta/IFN-alpha-beta_FULL_hmm_search.txt"));
gamma = set(parse_hmmer("./IFN-gamma/IFN-gamma_FULL_hmm_search.txt"));

# print(f'alpha beta = {alpha_beta}');
# print(f'gamma = {gamma}');
print(len(alpha_beta))
print(len(gamma))

for gamma_element in gamma:
    for alpha_beta_element in alpha_beta:
        if gamma_element == alpha_beta_element:
            print(f'{gamma_element} = {alpha_beta_element}')



# eSMODS = set(parse_hmmer("./eSMODS/eSMODS_hmm_search.txt"));
# OAS = set(parse_hmmer("./OAS/OAS_hmm_search.txt"));
# Mab21 = set(parse_hmmer("./Mab21/Mab21_hmm_search.txt"))
# CD_NTases = set(parse_hmmer("./CD-NTases_hmm_search.txt"));

