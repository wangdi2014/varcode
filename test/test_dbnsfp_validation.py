# Copyright (c) 2014. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pandas as pd
from varcode import VariantAnnotator

annot = VariantAnnotator(75)

def validate_transcript_mutation(
        chrom, dna_position,
        dna_ref, dna_alt,
        aa_pos, aa_alt):
    print annot.describe_variant(chrom, dna_position, dna_ref, dna_alt)


def test_dbnsfp_validation_set():
    """
    test_dbnsfp_validation_set : check that amino acid substitution gives
    same answer as subset of dbNSFP entries (using Ensembl 75)
    """
    # columns for validation dataset:
    # - aa_pos : base-1 position within protein
    # - dna_alt : non-reference DNA nucleotide
    # - chrom : choromosome
    # - ensembl_transcript : transcript ID
    # - dna_position : base-1 position within chromosome
    # - dna_ref : reference DNA nucleotide
    validation_set = pd.read_csv('dbnsfp_validation_set.csv')
    for _, row in validation_set.iterrows():
        print row
        validate_transcript_mutation(
            row['chrom'],
            row['dna_position'],
            row['dna_ref'],
            row['dna_alt'],
            row['aa_pos'],
            row['aa_alt'])

if __name__ == '__main__':
  test_dbnsfp_validation_set()