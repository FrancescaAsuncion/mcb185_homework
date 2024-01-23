print("Franceca_Asuncion")
print("francescaasuncion")
gunzip -c ~/code/MCB185/data/dictionary.gz | grep "a" | grep -v "[^auotfcm]" | grep -E ".{4,}" | wc
gunzip -c ~/code/MCB185/data/dictionary.gz | grep "b" | grep -v "[^bailnrt]" | grep -E ".{4,}" | wc
gunzip -c ~/code/MCB185/data/dictionary.gz | grep "c" | grep -v "[^caonidm]" | grep -E ".{4,}" | wc
gunzip -c ~/code/MCB185/data/dictionary.gz | grep "z" | grep -v "[^znorgia]" | grep -E ".{4,}" | wc
gunzip -c ~/code/MCB185/data/jaspar2024_core.transfac.gz | grep tax | cut -d ":" -f 2 | sort | uniq -c | sort -nr
print("Co-authors: Anisha Patel and Varsha Thalladi")

