print("Franceca_Asuncion")
print("francescaasuncion")
gunzip -c ~/code/MCB185/data/dictionary.gz | grep "a" | grep -v "[^auotfcm]" | grep -E ".{4,}" | wc
