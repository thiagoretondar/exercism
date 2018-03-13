def to_rna(dna_strand):
    rna_set = { 'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U' }
    rna_transcription = ''
    for char in dna_strand:
        rna_transcription = rna_transcription + rna_set[char]
    return rna_transcription
