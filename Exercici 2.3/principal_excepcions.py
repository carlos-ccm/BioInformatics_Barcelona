import excepcions

sequencia = "ATGCATGCÑATGCATGC"
try:
    print(excepcions.comprovar_fasta(sequencia))
except excepcions.ErrorFastaExcepcion:
    print(excepcions.ErrorFastaExcepcion.missatge)