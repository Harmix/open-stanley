// Open Stanley hero: the lines the plugin reads, drifting through a lens.
// Characters come and go with a noise field, the whole surface ripples, a light band moves across it.
(function(){
  var c=document.getElementById("field"); if(!c) return;
  var g=c.getContext("2d");
  var src=["slack #founders","meeting · customer call","gmail · sent","calendar","voice note","notion · spec","pam · memory","story · fresh","ledger","audit","scout","recap","soapbox","drive · deck"];
  var txt=["the deal went to the vendor who replied first","we don't need memory, we need to stop asking one person","hour 2 of 4: the agent sent a real email to a lead named test","coffee chat with a YC partner, 30 min","3 co-founders picked the top 5 facts from the same meeting: 2.0/5 overlap","he had never heard of racing separate ideas to $10K MRR","the summary said one thing; the transcript says another","the thing I'd tell founders who are just starting","receipt: pam:meeting/3a1f","lane: founder-operating-lessons · shape: event → claim → question","landing: first-person=yes named-entity=yes question=yes image=yes","impressions 10,312 · reactions 41 · comments 6 · reposts 2","two of the commenters are founders you met last week","experiment ending: open-question n=9 · flat n=31","raise money when you don't need it","the knowledge was already in the agent; the team still asked a person","who kept showing up this month: 7 people, 3 new","post scheduled tue 09:00 · series link in first comment","what did you do by hand before you built it?","rules promoted 2 · retired 1 · diffs stored 14"];
  var stream="";for(var i=0;i<400;i++){stream+=src[(i*5+3)%src.length]+"  "+String(8+(i*5)%14).padStart(2,"0")+":"+String((i*17)%60).padStart(2,"0")+"  "+txt[(i*11)%txt.length]+"      ";}
  // small value-noise
  var P=new Uint8Array(512);for(var i=0;i<256;i++)P[i]=i;for(var i=255;i>0;i--){var j=(Math.random()*(i+1))|0;var t=P[i];P[i]=P[j];P[j]=t;}for(var i=0;i<256;i++)P[256+i]=P[i];
  function fade(t){return t*t*t*(t*(t*6-15)+10);}function lerp(a,b,t){return a+t*(b-a);}
  function grad(h,x,y){switch(h&3){case 0:return x+y;case 1:return -x+y;case 2:return x-y;default:return -x-y;}}
  function noise(x,y){var X=Math.floor(x)&255,Y=Math.floor(y)&255;x-=Math.floor(x);y-=Math.floor(y);var u=fade(x),v=fade(y);var A=P[X]+Y,B=P[X+1]+Y;return lerp(lerp(grad(P[A],x,y),grad(P[B],x-1,y),u),lerp(grad(P[A+1],x,y-1),grad(P[B+1],x-1,y-1),u),v);}
  var W,H,dpr,cols,rows,cw=9.2,ch=19,t0=performance.now(),reduce=matchMedia("(prefers-reduced-motion: reduce)").matches,fonts,curF=-1,mx=-1,my=-1;
  function size(){dpr=Math.min(2,devicePixelRatio||1);W=c.clientWidth;H=c.clientHeight;c.width=W*dpr;c.height=H*dpr;g.setTransform(dpr,0,0,dpr,0,0);cols=Math.ceil(W/cw)+6;rows=Math.ceil(H/ch)+6;fonts=["12px JetBrains Mono, ui-monospace, Menlo, monospace","13.5px JetBrains Mono, ui-monospace, Menlo, monospace","15.5px JetBrains Mono, ui-monospace, Menlo, monospace","18px JetBrains Mono, ui-monospace, Menlo, monospace"];g.textBaseline="top";}
  size();addEventListener("resize",size);
  c.parentElement.addEventListener("mousemove",function(e){var r=c.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top;});
  c.parentElement.addEventListener("mouseleave",function(){mx=my=-1;});
  var last=0;
  function frame(now){
    if(now-last<33){requestAnimationFrame(frame);return;} last=now;
    var t=(now-t0)/1000;
    g.fillStyle="#0a1335";g.fillRect(0,0,W,H);curF=-1;
    var cx=W/2,cy=H/2,R=Math.min(W,H)*0.62,lens=W<720?0.25:0.5;
    var scroll=reduce?0:t*0.7,rowOff=Math.floor(scroll),frac=scroll-rowOff;
    var bandX=((t*0.09)%1.4-0.2)*W;          // a light band crossing left to right
    for(var j=-3;j<rows;j++){
      var y0=(j-frac)*ch;
      for(var i=-3;i<cols;i++){
        var x0=i*cw;
        // visibility: noise field drifting, thresholded, so words surface and sink
        var n=noise(i*0.09+t*0.05,(j+rowOff)*0.13-t*0.03);
        if(n<-0.12) continue;
        var dx=x0-cx,dy=y0-cy,d=Math.sqrt(dx*dx+dy*dy)/R;
        var k=Math.exp(-d*d*2.2);
        var sc=1+lens*k;
        var ripple=Math.sin(t*0.8+x0*0.012)*4+Math.sin(t*0.5+y0*0.02)*3;
        var x=cx+dx*sc, y=cy+dy*sc+ripple*(0.4+k);
        if(x<-20||x>W+20||y<-20||y>H+20) continue;
        var idx=((j+rowOff)*cols+i+((j+rowOff)*37))%stream.length; if(idx<0) idx+=stream.length;
        var chr=stream.charAt(idx); if(chr===" ") continue;
        var a=0.16+0.45*k+0.25*Math.max(0,n);
        a+=0.28*Math.exp(-((x-bandX)*(x-bandX))/(W*W*0.012));     // the band
        if(mx>=0){var mdx=x-mx,mdy=y-my;a+=0.35*Math.exp(-(mdx*mdx+mdy*mdy)/14000);}   // cursor light
        a*=1-0.7*Math.exp(-(d*d)/0.06);                              // thin behind the wordmark, smoothly
        if(a<0.05) continue;
        var fz=k>0.66?3:(k>0.33?2:(k>0.12?1:0)); if(fz!==curF){curF=fz;g.font=fonts[fz];}
        var num=chr>="0"&&chr<="9";
        g.fillStyle=num?"rgba(175,232,205,"+Math.min(1,a)+")":"rgba(160,188,255,"+Math.min(1,a)+")";
        g.fillText(chr,x,y);
      }
    }
    g.fillStyle="rgba(0,0,0,0.16)";for(var sy=0;sy<H;sy+=3){g.fillRect(0,sy,W,1);}
    if(!reduce) requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();
