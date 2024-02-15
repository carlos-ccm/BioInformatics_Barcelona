class ErrorFastaExcepcion(Exception):
    def __init__(self,missatge = "Nucleotid no valid"):
        self.missatge = missatge
        super().__init__(self.missatge)
        
def comprovar_fasta(fasta):
    valid = ['A','T','C','G']
    for nucleotid in fasta:
        if nucleotid not in valid:
            raise ErrorFastaExcepcion (f"Nucleotid {nucleotid} no es vàlid")
    return "Sequencia correcta"

sequencia = "ATGCATGCÑATGCATGC"
try:
    print(comprovar_fasta(sequencia))
except ErrorFastaExcepcion as e:
    print(e.missatge)