import colorama
from colorama import Fore,Style
import sys
user=input("Enter the DNA sequence: ").upper()
trip = []
def transcription():
    lst = []
    base = 'ATGC'
    for i in user:
        if i in base:

            if i=='A':
                lst.append('U')
            if i == 'T':
                lst.append('A')
            if i == 'C':
                lst.append('G')
            if i == 'G':
                lst.append('C')
        else:
            del(lst)
            break
    if len(lst)>0:
        rna_seq = ''
        for j in lst:
            rna_seq = rna_seq + j
        k, f = 0, 3
        while k < len(rna_seq):
            trip.append(rna_seq[k:f])
            k = k + 3
            f = f + 3
        if len(trip) > 0:
            print('The RNA sequence is:', rna_seq)
        h = 0
        sh = ''
        print('The triplet codon are:', end=' ')
        while h < len(rna_seq):
            sh = rna_seq[h:h + 3]
            print(sh, end=' ')
            h = h + 3
    else:
        print(f"{Fore.RED}Empty sequence")
def translation():
    print(' ')
    amino,amino1 = [],[]
    for l in trip:
        if l == 'UAA' or l == 'UAG' or l == 'UGA':
            break
        elif l == 'AUG':
            amino=f"{Fore.GREEN}Met"
            amino1.append(amino)
            nxt = trip[1:]
            for f in nxt:
                if f == 'UAA' or f == 'UAG' or f == 'UGA':
                    break
                if f == 'UUU' or f == 'UUC':
                    amino = f"{Fore.GREEN}Phe"
                    amino1.append(amino)
                if f == 'AUG':
                    amino = f"{Fore.GREEN}Met"
                    amino1.append(amino)
                if f == 'UUA' or f == 'UUG' or f == 'CUU' or f == 'CUC' or f == "CUA" or f == 'CUG':
                    amino = f"{Fore.GREEN}Leu"
                    amino1.append(amino)
                if f == 'AUU' or f == 'AUC':
                    amino = f"{Fore.GREEN}Ile"
                    amino1.append(amino)
                if f == 'GUU' or f == 'GUC' or f == 'GUA' or f == 'GUG':
                    amino = f"{Fore.GREEN}Val"
                    amino1.append(amino)
                if f == 'UCU' or f == 'UCC' or f == 'UCA' or f == 'UCG':
                    amino = f"{Fore.LIGHTRED_EX}Ser"
                    amino1.append(amino)
                if f == 'CCU' or f == 'CCC' or f == 'CCA' or f == 'CCG':
                    amino = f"{Fore.LIGHTYELLOW_EX}Pro"
                    amino1.append(amino)
                if f == 'ACU' or f == 'ACC' or f == 'ACA' or f == 'ACG':
                    amino =f"{Fore.YELLOW}Thr"
                    amino1.append(amino)
                if f == 'GCU' or f == 'GCC' or f == 'GCA' or f == 'GCG':
                    amino = f"{Fore.LIGHTGREEN_EX}Ala"
                    amino1.append(amino)
                if f == 'UAU' or f == 'UAC' or f == 'UGU' or f == 'UGC':
                    amino = f"{Fore.CYAN}Tyr"
                    amino1.append(amino)
                if f == 'CAU' or f == 'CAC':
                    amino = f"{Fore.LIGHTBLUE_EX}His"
                    amino1.append(amino)
                if f == 'CAA' or f == 'CAG':
                    amino = f"{Fore.YELLOW}Gln"
                    amino1.append(amino)
                if f == 'AAU' or f == 'AAC':
                    amino = f"{Fore.MAGENTA}Asn"
                    amino1.append(amino)
                if f == 'AAA' or f == 'AAG':
                    amino = f"{Fore.LIGHTMAGENTA_EX}Lys"
                    amino1.append(amino)
                if f == 'GAU' or f == 'GAC':
                    amino = f"{Fore.RED}Asp"
                    amino1.append(amino)
                if f == 'GAA' or f == 'GAG':
                    amino = f"{Fore.LIGHTRED_EX}Glu"
                    amino1.append(amino)
                if f == 'UGG':
                    amino = f"{Fore.CYAN}Trp"
                    amino1.append(amino)
                if f == 'CGU' or f == 'CGC' or f == 'CGA' or f == 'CGG' or f == 'AGA' or f == 'AGG':
                    amino = f"{Fore.BLUE}Arg"
                    amino1.append(amino)
                if f == 'AGU' or f == 'AGC':
                    amino = f"{Fore.YELLOW}Ser"
                    amino1.append(amino)
                if f == 'GGU' or f == 'GGC' or f == 'GGG' or f == 'GGA':
                    amino = f"{Fore.YELLOW+Fore.RED}Gly"
                    amino1.append(amino)
    if len(amino1) > 0:
        amin=' '
        t=0
        print("The protein sequence is : ",end='')
        for n in amino1:
            amin=amin+'-'+n
        print(amin,end='-')
try:
    transcription()
    translation()
except UnboundLocalError:
    print(f"{Fore.RED}Invalid nucleotide base")














