"""Basic dependency-free checks. Run: python tests/smoke_test.py"""
from pathlib import Path
import re, subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
checks=[]
def check(label, cond):
 print(('PASS' if cond else 'FAIL')+' '+label)
 checks.append(bool(cond))
index=(ROOT/'index.html').read_text()
main=(ROOT/'main.js').read_text()
products=(ROOT/'products.js').read_text()
check('HTML entry exists', '<div id="app"></div>' in index)
check('Responsive viewport', 'width=device-width' in index)
check('Three numbered photo controls implemented', 'data-photo="${i}"' in main)
check('Product popup and WhatsApp enquiry', all(x in main for x in ('function openProduct(', 'function drawModal(', 'https://wa.me/918668586372')))
check('Favorites and category filters', all(x in main for x in ('hitech_favorites','data-category','function updateGrid(')))
check('Local photo picker and room preview', all(x in main for x in ('id="design-photo"','id="room-input"','function renderRoomPreview(')))
check('3 supplied sofa gallery paths', all(x in products for x in ('sofa-001-1.jpg','sofa-001-2.jpg','sofa-001-3.jpg')))
for f in ['sofa-001-1.jpg','sofa-001-2.jpg','sofa-001-3.jpg','real-bed.jpg','real-sofa.jpg']:
 check('File '+f,(ROOT/'images'/f).is_file())
for file in ['main.js','products.js']:
 r=subprocess.run(['node','--check',str(ROOT/file)],capture_output=True,text=True)
 check('JavaScript syntax '+file,r.returncode==0)
check('GitHub Pages workflow', (ROOT/'.github/workflows/deploy.yml').exists())
check('README localhost instructions','python -m http.server' in (ROOT/'README.md').read_text())
print(f'\n{sum(checks)}/{len(checks)} passed')
sys.exit(0 if all(checks) else 1)
