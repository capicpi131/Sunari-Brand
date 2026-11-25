const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
for(let i=1;i<=10;i++){const n=String(i).padStart(2,'0');await p.goto('file://'+process.cwd()+`/story-${n}.html`);await p.evaluate(()=>document.fonts.ready);await p.screenshot({path:`out/story-${n}.png`});}
await b.close()})();
