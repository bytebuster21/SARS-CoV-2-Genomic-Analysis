from Bio import SeqIO
import matplotlib.pyplot as plt

def get_stats(fasta_file):
    # This reads the FASTA and calculates length and GC%
    record = SeqIO.read(fasta_file, "fasta")
    seq = record.seq
    gc = (seq.count("G") + seq.count("C")) / len(seq) * 100
    return len(seq), round(gc, 4)

# Update these with your actual filename
len20, gc20 = get_stats("sequence_2020.fasta")
len26, gc26 = get_stats("sequence_2026.fasta")

print(f"2020: {len20}bp, GC: {gc20}%")
print(f"2026: {len26}bp, GC: {gc26}%")

# Create the visual 'Proof'
plt.figure(figsize=(8, 6))
plt.bar(['2020 Ref', '2026 Var'], [gc20, gc26], color=['#3498db', '#e67e22'])
plt.ylabel('GC Content (%)')
plt.title('Evolution of Viral Stability (GC Content Shift)')
plt.savefig('results_chart.png') # This saves the image for your LinkedIn post!
plt.show()