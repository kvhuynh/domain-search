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
            # hit_list.append(hit.description.split(" ")[0]);
            hit_list.append(hit);
    return hit_list;

def get_similar_proteins(domain, LRR):
    similar_proteins = [];
    for LRR_item in LRR:
        for domain_item in domain:
            if LRR_item == domain_item:
                similar_proteins.append(domain[domain_item]);
                # print(LRR_item)
    # print(len(similar_proteins));
    return similar_proteins;

def protein_name_hit_dict(hit_list):
    result = {};
    for element in hit_list:
        split_file_name: list = element.id.split("_");
        species: str = "_".join(split_file_name[:-1]);
        protein_name: str = split_file_name[-1];
        if element.id not in result:
            result[element.id] = element;
    return result;

# NACHT = set(parse_hmmer("../NACHT/NACHT_FULL_hmm_search.txt"));
# TIR = set(parse_hmmer("../TIR/TIR_FULL_hmm_search.txt"));
NB_ARC = set(parse_hmmer("../NB-ARC/NB-ARC_FULL_hmm_search.txt"));
LRR = set(parse_hmmer("../leucine-rich-repeat/leucine-rich-repeat_FULL_hmm_search.txt"));

NB_ARC_dict = protein_name_hit_dict(NB_ARC);
LRR_dict = protein_name_hit_dict(LRR);
# NACHT_dict = protein_name_hit_dict(NACHT);
# TIR_dict = protein_name_hit_dict(TIR);

# print(TIR_dict);
# GET ALL PROTEIN HITS THAT ARE SIMILAR
with open("./LRR-NB-ARC_FULL_test_hmm_search.txt", "w") as f:
    for hit in get_similar_proteins(NB_ARC_dict, LRR_dict):
        f.write(f'{hit.id}\n')
        # print(hit.qresult.id)

# print(len(get_similar_proteins(NACHT_dict, LRR_dict)))


# TRANSFER ALL HITS FROM ORIGINAL LRR FILE TO NACHT
with open("./LRR-NB-ARC_FULL_test_hmm_search.txt", "r") as infile, open("../leucine-rich-repeat/leucine-rich-repeat_FULL_hmm_search.txt", "r") as leucine_rich_repeat, open("./LRR-NB-ARC_FULL_hmm_search.txt", "w") as outfile:
    # for line in infile:
    #     for 
    protein_names = []
    for line in infile:
        protein_names.append(line[:-1]);
    for line in leucine_rich_repeat:
        for protein in protein_names:
            if protein in line:
                outfile.write(line);
                # print(line);




# copy_matching_lines('input.txt', 'output.txt', 'search_string')


# print(len(TIR))
# print(len(LRR))


