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
            # hit_list.append(hit);
    return hit_list;



pore = set(parse_hmmer("./gasdermin-pore/gasdermin-pore_FULL_hmm_search.txt"));
print(f'pore length = {len(pore)}')
# print(pore)
pub = set(parse_hmmer("./gasdermin-pub/gasdermin-pub_FULL_hmm_search.txt"));
print(f'pub length = {len(pub)}')
# combined = set(parse_hmmer("./gasdermin_combined_FULL_hmmsearch.txt"));
# print(f'set combined length = {len(combined)}');
# print(f'combined length = {len(parse_hmmer("./gasdermin_combined_hmmsearch.txt"))}');

match = [];
for pore_element in pore:
    for pub_element in pub:
        if pore_element == pub_element:
            # print(f'{pore_element} = {pub_element}')
            match.append(pore_element);
print(f'match length = {len(match)}');
# print(match)

