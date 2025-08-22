from Bio import Entrez, SeqIO
from Bio.Seq import Seq
from collections import Counter
import sympy as sp
import math
import random

# Set email for Entrez (required for NCBI access; use a placeholder or your own)
Entrez.email = "your.email@example.com"  # Replace with a real email to avoid NCBI blocks

# Function to fetch a gene sequence from NCBI
def fetch_gene_sequence(accession, start=1, end=None):
    handle = Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text", seq_start=start, seq_stop=end)
    record = SeqIO.read(handle, "fasta")
    handle.close()
    return record.seq

# Expanded PWT-inspired DNA prime analyzer
def analyze_dna_primes(dna_seq):
    # Translate to protein for context
    protein = dna_seq.translate()
    print(f"Protein sequence (first 50 aa): {str(protein)[:50]}...")

    # Extract codons (handle if not multiple of 3)
    codons = [str(dna_seq[i:i+3]) for i in range(0, len(dna_seq), 3) if len(dna_seq[i:i+3]) == 3]

    # Count codons
    codon_count = Counter(codons)

    # Analyze counts for prime signatures
    prime_data = []
    for codon, count in codon_count.items():
        factors = sp.factorint(count)
        is_prime_count = sp.isprime(count)
        prime_data.append((codon, count, is_prime_count, factors))

    # Totals
    total_codons = len(codons)
    total_length = len(dna_seq)
    total_factors = sp.factorint(total_codons)
    length_factors = sp.factorint(total_length)

    return prime_data, total_codons, total_factors, total_length, length_factors

# Simulate evolutionary drifts (simple SNP mutations over generations)
def simulate_evo_drifts(dna_seq, generations=5, mutation_rate=0.01):
    results = []
    current_seq = dna_seq
    for gen in range(generations):
        # Mutate: Random SNP at rate
        seq_list = list(current_seq)
        for i in range(len(seq_list)):
            if random.random() < mutation_rate:
                bases = ['A', 'C', 'G', 'T']
                seq_list[i] = random.choice([b for b in bases if b != seq_list[i]])
        current_seq = Seq(''.join(seq_list))
        
        # Analyze
        prime_data, total_codons, total_factors, _, _ = analyze_dna_primes(current_seq)
        
        # Summarize drift (e.g., number of prime counts)
        num_prime_counts = sum(1 for _, _, is_prime, _ in prime_data if is_prime)
        results.append((gen + 1, num_prime_counts, total_factors))
    
    return results

# Main execution
if __name__ == "__main__":
    # Fetch full HBB gene segment (NG_028289.1, positions 5001-7000 for ~2kb)
    print("Fetching HBB gene segment from NCBI...")
    hbb_seq = fetch_gene_sequence("NG_028289.1", start=5001, end=7000)
    print(f"Fetched sequence length: {len(hbb_seq)} bp")

    # Analyze original
    print("\nOriginal HBB Gene Segment Analysis:")
    prime_data, total_codons, total_factors, total_length, length_factors = analyze_dna_primes(hbb_seq)
    print("Sample Prime Data (first 5 codons):")
    for data in prime_data[:5]:
        print(data)
    print(f"Total Codons: {total_codons}, Factors: {total_factors}")
    print(f"DNA Length: {total_length}, Factors: {length_factors}")

    # Simulate drifts
    print("\nSimulating Evolutionary Prime Drifts (5 generations):")
    evo_results = simulate_evo_drifts(hbb_seq, generations=5, mutation_rate=0.01)
    for gen, prime_counts, factors in evo_results:
        print(f"Generation {gen}: Prime Counts = {prime_counts}, Total Codon Factors = {factors}")
