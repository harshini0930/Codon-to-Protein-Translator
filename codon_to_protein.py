from Bio.Seq import Seq
import os

if not os.path.exists("outputs"):
    os.makedirs("outputs")


def translate_dna(dna_input):
    dna_seq = Seq(dna_input.upper())
    protein_seq = dna_seq.translate()
    codons = [dna_seq[i:i+3] for i in range(0, len(dna_seq), 3)]
    return dna_seq, codons, protein_seq

def amino_acid_properties(protein_seq):
    aa_properties = {
        'A':'hydrophobic','R':'basic','N':'polar','D':'acidic','C':'polar',
        'E':'acidic','Q':'polar','G':'hydrophobic','H':'basic','I':'hydrophobic',
        'L':'hydrophobic','K':'basic','M':'hydrophobic','F':'hydrophobic',
        'P':'hydrophobic','S':'polar','T':'polar','W':'hydrophobic','Y':'polar','V':'hydrophobic'
    }
    return {aa: aa_properties.get(aa,'unknown') for aa in protein_seq}


def main():
    user_input = input("Enter your DNA sequence (A, T, G, C only): ")
    dna_seq, codons, protein_seq = translate_dna(user_input)
    aa_props = amino_acid_properties(protein_seq)

    print("\n=== Results ===")
    print("DNA sequence: ", dna_seq)
    print("Codons: ", codons)
    print("Protein sequence: ", protein_seq)
    print("\nAmino acid properties:")
    for aa, prop in aa_props.items():
        print(f"{aa}: {prop}")

    # Save results to outputs folder
    output_file = os.path.join("outputs", "protein_output.txt")
    with open(output_file, "w") as f:
        f.write(f"DNA: {dna_seq}\n")
        f.write(f"Codons: {codons}\n")
        f.write(f"Protein: {protein_seq}\n")
        f.write("Amino acid properties:\n")
        for aa, prop in aa_props.items():
            f.write(f"{aa}: {prop}\n")

    print(f"\nResults saved to {output_file}")

if __name__ == "__main__":
    main()


