#!/usr/bin/env node
'use strict';
// Convert only the audited local SMPTeX reference formulas; never unsanitized HTML.
const fs=require('node:fs');
let mathjax,TeX,SVG,liteAdaptor,RegisterHTMLHandler,AllPackages;
try{
 ({mathjax}=require('mathjax-full/js/mathjax.js'));
 ({TeX}=require('mathjax-full/js/input/tex.js'));
 ({SVG}=require('mathjax-full/js/output/svg.js'));
 ({liteAdaptor}=require('mathjax-full/js/adaptors/liteAdaptor.js'));
 ({RegisterHTMLHandler}=require('mathjax-full/js/handlers/html.js'));
 ({AllPackages}=require('mathjax-full/js/input/tex/AllPackages.js'));
}catch(e){process.stderr.write('Install optional mathjax-full@3.2.1\n');process.exit(2)}
const adaptor=liteAdaptor();RegisterHTMLHandler(adaptor);
const document=mathjax.document('',{InputJax:new TeX({packages:AllPackages}),
                                    OutputJax:new SVG({fontCache:'local'})});
const input=JSON.parse(fs.readFileSync(0,'utf8'));
if(!Array.isArray(input.tex)||input.tex.some(s=>typeof s!=='string'))
 throw Error('Unexpected JSON input schema');
const result=[];
for(const tex of input.tex){
 const html=adaptor.outerHTML(document.convert(tex,{display:true,em:16,ex:8,containerWidth:1600}));
 const match=html.match(/<svg\b[^>]*>[\s\S]*<\/svg>/);
 if(!match||html.includes('merror'))throw Error('MathJax could not render: '+tex);
 result.push(match[0]);
}
process.stdout.write(JSON.stringify({svg:result}));
