with open ("Intron_list.txt") as infile, open ("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.replace("transcript_id", "").replace(",","").replace("'","").replace("(", "").replace(")","").replace('"',""))
