const {Resvg}=require('@resvg/resvg-js');const fs=require('fs');
const fontFiles=['fonts/Inter.ttf','fonts/JetBrainsMono.ttf'];
for(const name of ['01-now-playing-dark','02-library-albums','06-equalizer-dsp','14-classic-compact','16-mobile-screens','28-components-actions','32-foundations-tokens','43-skin-comparison']){
 const svg=fs.readFileSync(`svg/${name}.svg`,'utf8');const r=new Resvg(svg,{fitTo:{mode:'width',value:1440},font:{fontFiles,defaultFontFamily:'Inter',defaultFontSize:14}});fs.writeFileSync(`docs/${name}.png`,r.render().asPng());
}
console.log('Rendered 8 check images');
