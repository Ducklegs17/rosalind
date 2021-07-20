import os

def open_file(filename):
    """
    Reads a file
    """
    return (open(filename,"r"))

def validate_content_of_rna_string(seq):
    """
    Checks that the rna string is comprised of only A, U, G and Cs
    """
    rna = seq.upper()
    sum = rna.count("A") + rna.count("U") + rna.count("G") + rna.count("C")
    return sum == len(rna)

def split_into_codons(string):
    """
    splits the rna string into codons (blocks of three letters)
    """
    assert validate_content_of_rna_string(string), "argument contains invalid characters"
    seq = string.upper()
    return [seq[i:i+3] for i in range(0, len(seq), 3)]

def make_dictionary(dict_file):
    """
    Converts the codon -> aminoacid file into a dictionary object 
    """
    aminoacid_dict = {}
    for line in dict_file:
        key, value = line.split()
        aminoacid_dict[key] = value
    return aminoacid_dict

def translate_codons_to_aminoacids(codons,dictionary):
    """
    Translates each codon into the appropriate amino acid using the dictionary and joings into a single string
    """
    acid = "".join([dictionary.get(i) for i in codons])
    return acid

def remove_stop(string):
    """
    Remove the last 4 characters from a string
    """
    return string[:-4]

def main():
    code = open_file("code.txt")
    aminoacid_dict = make_dictionary(code)
    rna = open_file("input.txt").read().strip()
    codons = split_into_codons(rna)
    acids = translate_codons_to_aminoacids(codons,aminoacid_dict)
    print(remove_stop(acids))

if __name__ == '__main__':
    main()
