# from Bio import SearchIO;
# from Bio import SeqIO;
# import pandas as pd;
# import os;
# import sys;
# import copy;
# import requests;
# import csv;


# def create_json(domains: dict):
#     result_map = {};
#     for file in os.listdir("./TCS_FULL"):
#         result_map[file.split(".fasta")[0]] = {"domains": copy.deepcopy(domains)};
#     return result_map;

# def traverse_files_for_json():
#     domains: dict = {};
#     files_names = [];
#     file_paths = []
#     for root, dirs, files in os.walk("./domains_TCS_FULL", topdown=False):
#         for name in files:
#             path_name = os.path.join(root, name);
#             if path_name.endswith(".txt"):
#                 domains[root.split("/")[-1]] = [];
#                 file_paths.append(path_name);
#     print(domains);
#     output_json: dict = create_json(domains)
#     return {"file_paths": file_paths, "domains_list": domains, "output": output_json};
                
# def parse_hmm_search(output):
#     map_of_aliases = {};
#     for path in output["file_paths"]:
#         # set current domain
#         curr_domain: str = path.split("/")[-1].split("_")[0];
#         print(path)
#         for item in SearchIO.parse(path, "hmmer3-tab"):
#             for hit in item:
#                 split_file_name: list = hit.id.split("_");
#                 species: str = "_".join(split_file_name[:-1]);
#                 protein_name: str = split_file_name[-1];
#                 output["output"][species]["domains"][curr_domain].append(hit.description.split(' ')[0]);

#     print(output)
#     with open("TCS_FULL_json_04102025.txt", "w") as f:
#         f.write(str(output));

#     return output

# def write_to_excel(data):
#     domain_columns = list(data["domains_list"].keys())
#     row_protein_names = [];
#     rows_count = []

#     for species, info in data["output"].items():
#         row_protein_name = [species]
#         row_count = [species]
#         domains = info["domains"]
#         for domain in domain_columns:
#             values = domains.get(domain, [])
#             value_str = ",".join(values)
#             row_protein_name.append(value_str)
#             row_count.append(len(values))

#         row_protein_names.append(row_protein_name)
#         rows_count.append(row_count);

#     protein_hit_names_df = pd.DataFrame(row_protein_names, columns=["Species"] + domain_columns)
#     protein_hit_count_df = pd.DataFrame(rows_count, columns=["Species"] + domain_columns)

#     with pd.ExcelWriter("TCS_FULL_04152025.xlsx") as writer:

#         workbook = writer.book;
#         protein_hit_names_df.to_excel(writer, sheet_name="Protein hit names", index=False);
#         protein_hit_count_df.to_excel(writer, sheet_name="Protein hit count", index=False);

# write_to_excel(parse_hmm_search(traverse_files_for_json()));




