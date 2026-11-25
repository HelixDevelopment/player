const {Resvg}=require('@resvg/resvg-js');const sharp=require('sharp');const fs=require('fs');
(async()=>{const files=fs.readdirSync('svg').filter(f=>f.endsWith('.svg')).sort();
for(let p=0;p<Math.ceil(files.length/6);p++){
 const comps=[];const batch=files.slice(p*6,p*6+6);
 for(let i=0;i<batch.length;i++){const name=batch[i];const svg=fs.readFileSync('svg/'+name,'utf8');const png=new Resvg(svg,{fitTo:{mode:'width',value:700},font:{fontFiles:['fonts/Inter.ttf','fonts/JetBrainsMono.ttf'],defaultFontFamily:'Inter'}}).render().asPng();const im=sharp(png);const m=await im.metadata();const h=Math.ceil(700*m.height/m.width);const buf=await sharp(png).resize(700,h).png().toBuffer();comps.push({input:buf,left:0,top:i*500});
 fs.writeFileSync('docs/'+name.replace('.svg','.png'),png);
 }
 // separate pages avoids clipping tall boards
 for(let i=0;i<batch.length;i++){const name=batch[i];const svg=fs.readFileSync('svg/'+name,'utf8');const png=new Resvg(svg,{fitTo:{mode:'width',value:1000},font:{fontFiles:['fonts/Inter.ttf','fonts/JetBrainsMono.ttf'],defaultFontFamily:'Inter'}}).render().asPng();fs.writeFileSync('docs/'+name.replace('.svg','.png'),png);}
}
console.log('Rendered all SVGs');})();
