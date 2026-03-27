#!/usr/bin/env nextflow


params.sam = "input.sam"

process ANALYZE_SAM {
	publishDir "sam_statistics/", mode: 'copy'
	
	input:
		path sam_input  

	output:
		file "SAM_statistics_results.txt"

	script:
		"""
		uv run $HOME/sam_project/main.py ${sam_input} > SAM_statistics_results.txt
		"""
}


workflow {

	sam_file = channel.fromPath(params.sam)
	
	ANALYZE_SAM(sam_file)
}
