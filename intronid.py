import os
import re


class Gene:
    def __init__(self, chromosome_id, gene_id):
        self.chromosome_id = chromosome_id
        self.gene_id = gene_id
        self.transcripts = []

    def addTranscript(self, transcript):
        self.transcripts.append(transcript)

    def FindLongestTranscript(self):
        maxlength = 0
        longestTx = None
        for t in self.transcripts:
            length = t.GetLength()
            if length > maxlength:
                longestTx = t
                maxlength = length
        return longestTx
        
        
    def outputIntronsFromLongestTranscript(self):
        t = self.FindLongestTranscript()
        output = open('intronlist2.txt', 'a')
        for i in range(len(t.exons) - 1):
            place=t.list_index()
            intronTupple = (self.chromosome_id, t.transcript_id, int(t.exons[i].end)+1, int(t.exons[i+1].start)-1, place)
            intronTuppleStr=intronTupple[0]+'\t'+intronTupple[1][16:-1]+'_intron'+'intronTupple[4]'+'\t'+intronTupple[1][16:-1]+'\t'+str(intronTupple[2])+'\t'+str(intronTupple[3])+'\n'
            output.write(intronTuppleStr)



class Transcript:
    def __init__(self, transcript_id):
        self.exons = []
        self.transcript_id = transcript_id


    def addExon(self, exon):
        self.exons.append(exon)

    def GetLength(self):
        length = 0
        for exon in self.exons:
            length = length + exon.length
        return length
        
    def list_index (self):
        for i, e in enumerate (self.exons):
            place=i+1
        return place


class Exon:
    def __init__(self, start, end):

        if int(start) > int(end):
            self.start = end
            self.end = start

        else:
            self.start = start
            self.end = end

        self.length = int(self.end) - int(self.start) + 1

def main():
    # genes = {}

    with open('Equus_caballus_protein_coding_gene_tx_exon.gtf') as f:

        gene = None
        transcript = None
        for line in f:
            tokens = line.split('\t')
            chromosome_id = tokens[0]
            ids = tokens[8].split(';')
            gene_id = ids[0]
            transcript_id = ids[2]
            if tokens[2] == 'gene':
                if gene != None:
                    gene.outputIntronsFromLongestTranscript()
                # TODO need geneId in Gene class....
                gene = Gene(chromosome_id, gene_id)
            if tokens[2] == 'transcript':
                transcript = Transcript(transcript_id)
                gene.addTranscript(transcript)
            if tokens[2] == 'exon':
                exon = Exon(tokens[3], tokens[4])
                transcript.addExon(exon)
        gene.outputIntronsFromLongestTranscript()

if __name__ == '__main__':
    main()
