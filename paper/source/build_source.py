# Copyright 2026 Yusuf Kaya and Jan Moser
# SPDX-License-Identifier: Apache-2.0
"""Regenerate the editable LaTeX source from publication.md using Pandoc."""
from pathlib import Path
import subprocess
args=['pandoc','publication.md','-f','markdown+tex_math_single_backslash+raw_tex','-s','--top-level-division=section','--toc-depth=1','--pdf-engine=xelatex','-V','documentclass=article','-V','fontsize=10pt','-V','papersize=a4','-V','geometry=margin=23mm','-V','mainfont=Latin Modern Roman','-V','sansfont=Latin Modern Sans','-V','monofont=DejaVu Sans Mono','-V','colorlinks=false','-V','linestretch=1.08','-H','preamble.tex','-o','Compact_Post_Quantum_KEM_Tradeoff.tex']
subprocess.run(args,cwd=Path(__file__).resolve().parent,check=True)
p=Path(__file__).resolve().parent/'Compact_Post_Quantum_KEM_Tradeoff.tex'
t=p.read_text().replace('≥',r'\ensuremath{\ge}').replace('≤',r'\ensuremath{\le}')
p.write_text(t)
