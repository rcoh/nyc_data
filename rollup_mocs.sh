cat ~/Downloads/MOCS_Sell.csv | csvtojson | jq -rc ' .[]' > mocs.json
cat mocs.json | python3 unroll_mocs.py| agrind '* | json | sum(ct) by product' > mocs_rollup
