import os
import re

class Gene:

	def __init__(self, chromosome_id, gene_id):
		self.chromosome_id = chromosome_id
		self.gene_id = gene_id
		self.transcripts = []
		
	def addTranscript (self, transcript):
	    self.transcripts.append(transcript)

		
	#def addExonToTranscript(self, transcript_id, exon):
	#	self.transcripts.extend([transcript_id, exon])
	
	def FindLongestTranscript(self):
	    maxlength=0
	    longestTx=None
	    for t in self.transcripts:
	        length=t.GetLength()
	        if length > maxlength:
	            longestTx=t
	            maxlength=length
	    return longestTx
	
	def outputIntronsFromLongestTranscript(self):
	    t=self.FindLongestTranscript()
	    for i in range (len(t.exons)-1):
	        intron=(self.chromosome_id, t.transcript_id, int(t.exons[i].end)+1, int(t.exons[i+1].start)-1)
	        print (intron)

	
class Transcript:

	def __init__(self, transcript_id):
		self.exons = []
		self.transcript_id=transcript_id
		#self.numexons=0

	def addExon(self, exon):
		self.exons.append(exon)
		
	def GetLength(self):
	    length=0
	    for exon in self.exons:
	        length=length+exon.length
	    return length

		
class Exon:
	def __init__(self, start, end):
	
		if int(start) > int(end) :
			self.start=end
			self.end=start
			
		else:
			self.start=start
			self.end=end
			
		self.length=int(self.end) - int(self.start) + 1
		


def main():
	#genes = {}
	
	with open('/Equus_caballus_protein_coding_gene_tx_exon.gtf') as f:
	    gene = None
	    transcript = None
	    for line in f:
	        tokens = line.split('\t')
	        chromosome_id = tokens[0]
	        ids = tokens[8].split(';')
	        gene_id = ids[0]
	        transcript_id = ids[2]
	        if tokens[2] == 'gene':
	            if gene!=None:
	                gene.outputIntronsFromLongestTranscript()
	            #TODO need geneId in Gene class....
	            gene = Gene(chromosome_id, gene_id)        	
	        if tokens[2] == 'transcript':
	            transcript = Transcript(transcript_id)
	            gene.addTranscript(transcript)
	        if tokens[2]=='exon':
	            exon = Exon(tokens[3], tokens[4])
	            transcript.addExon(exon)
	    gene.outputIntronsFromLongestTranscript()   
	            #FindLongestTranscipt()
	        #if gene!=None:
	            #processGene(gene)
		    	    
#def processGene(gene):
    #for (t_id, transcript) in gene.transcripts:
        #max_key=max(gene.transcripts, key= lambda x: len(gene.transcripts[x]))
        #for exon in transcript.exons():
            #for i in range(len(transcript.exons)-1):
                #intron = (gene.chromosome_id, t_id, transcript.exons[i].end+1, transcript.exons[i+1].start-1)
                #print (intron)

if __name__ == '__main__':
	main()