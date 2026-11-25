"""Original, dependency-free SVG design artwork for the FUSE white-label player study.
All album art, icons, waveforms and UI are vector geometry. No reference-product assets.
"""
from pathlib import Path
from xml.sax.saxutils import escape
import math, random, json, base64
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'svg'; OUT.mkdir(exist_ok=True)
DARK=dict(bg='#101519',shell='#151C21',panel='#1B242B',raised='#243139',line='#35454E',text='#F3F7F6',muted='#ADBDC5',dim='#84969F',accent='#79E3C2',accent2='#F3C580',blue='#91BFFF',purple='#C5AEF4',danger='#FF9B9B',ink='#10251F',focus='#FFFFFF')
LIGHT=dict(bg='#E9EFEE',shell='#F7FAF9',panel='#FFFFFF',raised='#E7EFED',line='#B6C6C2',text='#172B27',muted='#4E655F',dim='#60756F',accent='#116B53',accent2='#8B530D',blue='#285EA0',purple='#70509B',danger='#A32D38',ink='#FFFFFF',focus='#172B27')
MONO=dict(bg='#F0F3F2',shell='#FFFFFF',panel='#FFFFFF',raised='#E8EEEC',line='#A8B8B2',text='#233B33',muted='#526A61',dim='#63796F',accent='#245C49',accent2='#765522',blue='#385F7D',purple='#66567D',danger='#8B343D',ink='#FFFFFF',focus='#233B33')
TRACKS=[('Slow satellites','Northbound','Afterglow','4:26'),('Glass houses','Northbound','Afterglow','3:51'),('A little further','Northbound','Afterglow','5:08'),('Coastline','Northbound','Afterglow','3:42'),('Blue hour','Northbound','Afterglow','4:17'),('Still / moving','Northbound','Afterglow','3:36'),('Northern lights','Northbound','Afterglow','5:24'),('Last light','Northbound','Afterglow','4:02')]
ICONS={
'play':'M9 5 L19 12 L9 19 Z', 'pause':'M8 5 V19 M16 5 V19',
'prev':'M6 5 V19 M18 5 L8 12 L18 19 Z','next':'M18 5 V19 M6 5 L16 12 L6 19 Z',
'stop':'M7 7 H17 V17 H7 Z','shuffle':'M3 6 H6 C10 6 13 18 17 18 H21 M17 14 L21 18 L17 22 M3 18 H6 C8 18 9 15 10 13 M13 9 C14 7 15 6 17 6 H21 M17 2 L21 6 L17 10',
'repeat':'M5 7 H18 L21 10 M19 3 L22 7 L19 11 M19 17 H6 L3 14 M5 13 L2 17 L5 21',
'heart':'M12 20 L4 12 C-1 5 8 1 12 7 C16 1 25 5 20 12 Z',
'music':'M9 18 V5 L20 3 V16 M9 9 L20 7 M9 18 C9 22 2 22 3 18 C3 15 7 15 9 18 M20 16 C20 20 13 20 14 16 C14 13 18 13 20 16',
'library':'M4 4 V20 M9 4 V20 M14 5 L19 4 L22 19 L17 20 Z',
'grid':'M4 4 H10 V10 H4 Z M14 4 H20 V10 H14 Z M4 14 H10 V20 H4 Z M14 14 H20 V20 H14 Z',
'list':'M8 6 H21 M8 12 H21 M8 18 H21 M3 6 H4 M3 12 H4 M3 18 H4',
'queue':'M4 6 H15 M4 12 H12 M4 18 H10 M17 12 V21 L22 17 Z',
'wave':'M2 12 H5 L8 4 L12 20 L16 7 L19 15 L22 12',
'eq':'M5 3 V21 M12 3 V21 M19 3 V21 M2 8 H8 M9 16 H15 M16 7 H22',
'search':'M10 3 A7 7 0 1 0 10 17 A7 7 0 1 0 10 3 M15 15 L21 21',
'settings':'M12 8 A4 4 0 1 0 12 16 A4 4 0 1 0 12 8 M12 2 V5 M12 19 V22 M2 12 H5 M19 12 H22 M5 5 L7 7 M17 17 L19 19 M5 19 L7 17 M17 7 L19 5',
'plus':'M12 5 V19 M5 12 H19','close':'M6 6 L18 18 M18 6 L6 18',
'check':'M5 12 L10 17 L20 6','chevron':'M9 5 L16 12 L9 19',
'down':'M5 9 L12 16 L19 9','up':'M5 15 L12 8 L19 15',
'more':'M5 12 H5.1 M12 12 H12.1 M19 12 H19.1',
'folder':'M3 7 V5 H10 L12 8 H21 V19 H3 Z',
'volume':'M3 9 H7 L12 5 V19 L7 15 H3 Z M16 8 C20 10 20 14 16 16 M19 5 C25 9 25 15 19 19',
'mute':'M3 9 H7 L12 5 V19 L7 15 H3 Z M16 9 L22 15 M22 9 L16 15',
'expand':'M9 4 H4 V9 M15 4 H20 V9 M4 15 V20 H9 M20 15 V20 H15',
'minimize':'M4 9 H9 V4 M15 4 V9 H20 M4 15 H9 V20 M15 20 V15 H20',
'monitor':'M3 4 H21 V16 H3 Z M8 21 H16 M12 16 V21',
'info':'M12 3 A9 9 0 1 0 12 21 A9 9 0 1 0 12 3 M12 11 V17 M12 7 V7.1',
'warning':'M12 3 L22 21 H2 Z M12 9 V14 M12 17 V17.1',
'clock':'M12 3 A9 9 0 1 0 12 21 A9 9 0 1 0 12 3 M12 7 V12 L16 14',
'moon':'M20 15 A9 9 0 0 1 9 3 A9 9 0 1 0 20 15 Z',
'radio':'M3 8 H21 V21 H3 Z M6 8 L18 3 M6 12 H13 M6 16 H13 M17 13 A3 3 0 1 0 17 19 A3 3 0 1 0 17 13',
'palette':'M12 3 A9 9 0 1 0 12 21 H14 C17 21 16 17 18 17 H20 C25 10 19 3 12 3 Z M7 9 H7.1 M11 6 H11.1 M16 7 H16.1 M6 14 H6.1',
'lock':'M6 10 V7 A6 6 0 0 1 18 7 V10 M4 10 H20 V21 H4 Z M12 14 V17',
'link':'M9 15 L15 9 M8 17 L6 19 C2 22 -1 16 3 13 L7 9 C10 6 14 8 13 11 M16 7 L18 5 C22 2 25 8 21 11 L17 15 C14 18 10 16 11 13',
'download':'M12 3 V15 M7 10 L12 15 L17 10 M4 17 V21 H20 V17',
'upload':'M12 16 V4 M7 9 L12 4 L17 9 M4 17 V21 H20 V17',
'trash':'M4 6 H20 M9 6 V3 H15 V6 M6 6 L7 21 H17 L18 6 M10 10 V17 M14 10 V17',
'edit':'M4 16 L16 4 L20 8 L8 20 H4 Z M13 7 L17 11',
'grip':'M8 5 H8.1 M16 5 H16.1 M8 12 H8.1 M16 12 H16.1 M8 19 H8.1 M16 19 H16.1',
'star':'M12 3 L15 9 L22 10 L17 15 L18 22 L12 18 L6 22 L7 15 L2 10 L9 9 Z',
'headphones':'M4 14 V11 A8 8 0 0 1 20 11 V14 M4 12 H7 V21 H4 Z M17 12 H20 V21 H17 Z',
'sun':'M12 7 A5 5 0 1 0 12 17 A5 5 0 1 0 12 7 M12 1 V3 M12 21 V23 M1 12 H3 M21 12 H23 M4 4 L6 6 M18 18 L20 20 M4 20 L6 18 M18 6 L20 4',
'keyboard':'M2 5 H22 V19 H2 Z M5 9 H6 M9 9 H10 M13 9 H14 M17 9 H18 M5 13 H6 M9 13 H10 M13 13 H14 M17 13 H18 M7 16 H17',
'back':'M19 12 H4 M10 6 L4 12 L10 18',
'filter':'M3 5 H21 L14 13 V20 L10 18 V13 Z',
'pin':'M9 3 H15 L14 9 L19 13 H5 L10 9 Z M12 13 V22',
}
def esc(s): return escape(str(s))
def rect(x,y,w,h,fill,r=0,stroke=None,sw=1,extra=''):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+f' {extra}/>'
def line(x1,y1,x2,y2,c,sw=1,extra=''):
 return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}" {extra}/>'
def txt(x,y,s,size=14,c=None,weight=400,anchor='start',mono=False,extra=''):
 fam="'JetBrains Mono','SFMono-Regular',Consolas,monospace" if mono else "Inter,'SF Pro Display','Segoe UI',Arial,sans-serif"
 return f'<text x="{x}" y="{y}" font-family="{fam}" font-size="{size}" font-weight="{weight}" fill="{c or T["text"]}" text-anchor="{anchor}" {extra}>{esc(s)}</text>'
def circle(x,y,r,c,stroke=None,sw=1,extra=''):
 return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}"'+(f' stroke="{stroke}" stroke-width="{sw}"' if stroke else '')+f' {extra}/>'
def path(d,fill='none',stroke=None,sw=1,extra=''):
 return f'<path d="{d}" fill="{fill}"'+(f' stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"' if stroke else '')+f' {extra}/>'
def icon(name,x,y,size=20,c=None,sw=1.8):
 return f'<g transform="translate({x} {y}) scale({size/24})">{path(ICONS.get(name,ICONS["music"]),stroke=c or T["muted"],sw=sw)}</g>'
def label(x,y,s,c=None,size=11): return txt(x,y,s,size,c or T['dim'],650,extra='letter-spacing="1.6"')
def pill(x,y,w,s,kind='neutral',h=28,ic=None):
 bg=T['raised']; fg=T['muted']
 if kind=='accent': bg=T['accent']; fg=T['ink']
 if kind=='soft': bg='#254239' if T is DARK else '#DDEFE7'; fg=T['accent']
 if kind=='warn': bg='#44382A' if T is DARK else '#F5E8D5'; fg=T['accent2']
 out=rect(x,y,w,h,bg,h/2)
 if ic: out+=icon(ic,x+10,y+(h-16)/2,16,fg)
 out+=txt(x+(32 if ic else w/2),y+h/2+4,s,11,fg,600,'start' if ic else 'middle')
 return out
def button(x,y,w,s,kind='secondary',ic=None,h=40,disabled=False):
 bg=T['raised']; fg=T['text']; stroke=T['line']
 if kind=='primary': bg=T['accent']; fg=T['ink']; stroke=None
 if kind=='ghost': bg='none'; stroke=None; fg=T['muted']
 if kind=='danger': bg=T['danger']; fg='#241316' if T is DARK else '#FFFFFF'; stroke=None
 if disabled: fg=T['dim']; bg=T['panel']
 out=rect(x,y,w,h,bg,9,stroke)
 if ic: out+=icon(ic,x+14,y+(h-18)/2,18,fg)
 out+=txt(x+(42 if ic else w/2),y+h/2+5,s,13,fg,600,'start' if ic else 'middle')
 return out
def ib(name,x,y,size=40,active=False,kind='ghost',c=None):
 out=rect(x,y,size,size,T['accent'] if active else (T['raised'] if kind=='solid' else 'none'),10,T['line'] if kind=='solid' else None)
 return out+icon(name,x+(size-20)/2,y+(size-20)/2,20,c or (T['ink'] if active else T['muted']))
def rule(x,y,w): return line(x,y,x+w,y,T['line'])
T=DARK
def defs():
 return '''<defs>
 <linearGradient id="art-bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#163D42"/><stop offset=".52" stop-color="#327775"/><stop offset="1" stop-color="#102B38"/></linearGradient>
 <linearGradient id="art-sun" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#FFE2A3"/><stop offset=".55" stop-color="#F3B786"/><stop offset="1" stop-color="#DC897D"/></linearGradient>
 <linearGradient id="wave-fill" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#79E3C2" stop-opacity=".38"/><stop offset="1" stop-color="#79E3C2" stop-opacity=".02"/></linearGradient>
 <linearGradient id="spectrum" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#79E3C2"/><stop offset=".6" stop-color="#91BFFF"/><stop offset="1" stop-color="#F3C580"/></linearGradient>
 <radialGradient id="ambient"><stop stop-color="#4D9C8C" stop-opacity=".24"/><stop offset="1" stop-color="#4D9C8C" stop-opacity="0"/></radialGradient>
 <linearGradient id="metal" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#53616A"/><stop offset=".48" stop-color="#303D47"/><stop offset=".52" stop-color="#26323B"/><stop offset="1" stop-color="#414F58"/></linearGradient>
 <linearGradient id="classic-wave" x1="0" y1="0" x2="1" y2="0"><stop stop-color="#75E6BB"/><stop offset=".5" stop-color="#E6E997"/><stop offset="1" stop-color="#F3B47B"/></linearGradient>
 <pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r=".7" fill="#8CA8A0" opacity=".22"/></pattern>
 </defs>'''
def art(x,y,s,variant=0,show_title=True):
 # Original fictional album sleeve. All geometry, no external images.
 hue=[('#163D42','#327775','#102B38'),('#353452','#777299','#222D48'),('#4C3935','#A27760','#263C40'),('#183C4B','#497C93','#172B37')][variant%4]
 gid=f'ag{variant}'
 out=f'<g transform="translate({x} {y}) scale({s/400})"><defs><linearGradient id="{gid}" x2="1" y2="1"><stop stop-color="{hue[0]}"/><stop offset=".55" stop-color="{hue[1]}"/><stop offset="1" stop-color="{hue[2]}"/></linearGradient><clipPath id="{gid}-clip"><rect width="400" height="400" rx="8"/></clipPath></defs><g clip-path="url(#{gid}-clip)">'+rect(0,0,400,400,f'url(#{gid})',8)
 out+=circle(245,148,92,'url(#art-sun)')
 for i in range(9):
  yy=224+i*21
  out+=path(f'M-20 {yy} C70 {yy-65} 130 {yy+42} 225 {yy-12} S355 {yy-40} 430 {yy-8}',stroke='#A4DBCB' if i%2 else '#122F39',sw=12 if i%2 else 17,extra=f'opacity="{.55+i*.04}"')
 out+=path('M0 325 L105 236 L157 284 L225 213 L400 345 V400 H0 Z','#102C34',extra='opacity=".78"')
 out+=rect(0,0,400,400,'url(#dots)',8)
 if show_title:
  out+=txt(25,42,'N O R T H B O U N D',13,'#E9F5E9',600)
  out+=txt(24,365,['AFTERGLOW','OPEN WATER','SLOW SIGNALS','BLUE HOUR'][variant%4],28,'#F6F3E7',650,extra='letter-spacing="3"')
 return out+'</g></g>'
def wave_points(w=600,h=80,n=160,seed=5):
 r=random.Random(seed); pts=[]
 for i in range(n):
  envelope=.2+.8*math.sin(math.pi*i/(n-1))**.35
  a=(.25+.75*abs(math.sin(i*.47))*abs(math.cos(i*.13)))*envelope
  a=max(.07,min(1,a*(.65+r.random()*.5)))
  pts.append((i*w/(n-1),a))
 return pts
def wave(x,y,w,h,progress=.38,bars=True,seed=5,c=None):
 c=c or T['accent']; pts=wave_points(w,h,seed=seed)
 out=line(x,y+h/2,x+w,y+h/2,T['line'])
 if bars:
  for i,(px,a) in enumerate(pts):
   hh=max(3,a*h*.88); out+=line(x+px,y+(h-hh)/2,x+px,y+(h+hh)/2,c if i/len(pts)<progress else (T['dim'] if T is DARK else '#7C9690'),max(2,w/len(pts)*.48),f'opacity="{1 if i/len(pts)<progress else .65}"')
 else:
  d='M'+ ' L'.join(f'{x+px:.1f} {y+h/2-a*h*.44:.1f}' for px,a in pts)
  out+=path(d,stroke=c,sw=2)
 out+=line(x+w*progress,y-5,x+w*progress,y+h+5,T['text'],1.5)
 out+=circle(x+w*progress,y-5,4,T['text'])
 return out
def spectrum(x,y,w,h,n=48,seed=3,classic=False):
 r=random.Random(seed); out=''
 for i in range(n):
  a=(.18+.75*math.exp(-i/(n*.48)))*(.45+r.random()*.55)
  bw=w/n; hh=a*h
  out+=rect(x+i*bw,y+h-hh,bw*.65,hh,'url(#classic-wave)' if classic else 'url(#spectrum)',1)
  out+=rect(x+i*bw,y+h-hh-5,bw*.65,2,T['accent2'])
 return out
def logo(x,y,size=28,word=True,c=None):
 c=c or T['accent']; s=size/32
 out=f'<g transform="translate({x} {y}) scale({s})">'
 for i,h in enumerate([12,23,32,20,10]): out+=rect(i*6,(32-h)/2,3.5,h,c,1.7)
 out+='</g>'
 if word: out+=txt(x+size+12,y+size*.73,'FUSE',size*.73,T['text'],750,extra='letter-spacing="2"')
 return out
def avatar(x,y,s=32): return circle(x+s/2,y+s/2,s/2,T['raised'],T['line'])+txt(x+s/2,y+s/2+4,'AL',11,T['muted'],650,'middle')
def transport(x,y,scale=1,playing=True,compact=False):
 out=f'<g transform="translate({x} {y}) scale({scale})">'
 out+=ib('shuffle',0,4,36)+ib('prev',48,0,44)+ib('pause' if playing else 'play',104,-4,56,active=True)+ib('next',172,0,44)+ib('repeat',228,4,36)
 return out+'</g>'
def volume(x,y,w=130,val=.68):
 return icon('volume',x,y-10,20)+rect(x+32,y-2,w,4,T['line'],2)+rect(x+32,y-2,w*val,4,T['accent'],2)+circle(x+32+w*val,y,6,T['text'])+txt(x+w+46,y+4,f'{round(val*100)}%',11,T['muted'],mono=True)
def nav_item(x,y,w,name,ic,active=False,count=None):
 out=rect(x,y,w,42,T['raised'] if active else 'none',9)
 if active: out+=rect(x,y+11,3,20,T['accent'],2)
 out+=icon(ic,x+14,y+11,20,T['accent'] if active else T['muted'])+txt(x+46,y+26,name,13,T['text'] if active else T['muted'],600 if active else 450)
 if count: out+=txt(x+w-14,y+26,count,11,T['dim'],anchor='end',mono=True)
 return out
def shell(title='Now playing',active='Now playing',w=1440,h=960,sidebar=True,search='Search your music',status='Local library · 2,418 tracks',queue_count='3',theme=None):
 global CW,CH,T
 T=theme or DARK
 CW,CH=w,h
 out=rect(0,0,w,h,T['bg'])
 # Native-window chrome is deliberately neutral; host platform supplies real controls.
 out+=rect(0,0,w,36,T['shell'])+circle(20,18,5,T['danger'])+circle(39,18,5,T['accent2'])+circle(58,18,5,T['accent'])
 out+=txt(w/2,23,'FUSE  /  WHITE-LABEL PLAYER',10,T['dim'],600,'middle',extra='letter-spacing="1.8"')
 out+=pill(w-174,6,154,'LOCAL MODE','neutral',24,'lock')
 out+=rect(0,36,w,h-36,T['shell'])
 if sidebar:
  out+=rect(0,36,224,h-136,T['shell'])+line(224,36,224,h-100,T['line'])
  out+=logo(24,62,28)+label(25,135,'WORKSPACE')
  for i,(n,ic) in enumerate([('Now playing','play'),('Library','library'),('Playlists','list'),('Favorites','heart'),('History','clock')]): out+=nav_item(14,151+i*46,196,n,ic,n==active)
  out+=label(25,417,'YOUR COLLECTION')
  for i,(n,ic) in enumerate([('Albums','grid'),('Artists','music'),('Folders','folder'),('Radio','radio')]): out+=nav_item(14,433+i*44,196,n,ic,n==active)
  out+=label(25,643,'PLAYLISTS')+ib('plus',177,624,28)
  for i,n in enumerate(['Late night drive','Deep focus','Sunday morning']): out+=nav_item(14,657+i*40,196,n,'list')
  out+=button(18,h-164,188,'Import music','ghost','plus',36)
 # Header
 hx=248 if sidebar else 32
 out+=txt(hx,88,title,26,T['text'],650)
 out+=rect(w-474,57,300,42,T['bg'],10,T['line'])+icon('search',w-460,68,18,T['dim'])+txt(w-432,83,search,13,T['dim'])+pill(w-218,66,34,'/ K',h=24)
 out+=ib('settings',w-154,58,40)+ib('palette',w-108,58,40)+avatar(w-58,62,32)
 return out
def player_bar(y=None,w=1440,playing=True,empty=False):
 y=y or CH-100
 if empty:
  out=rect(0,y,w,100,T['panel'])+line(0,y,w,y,T['line'])+rect(20,y+18,64,64,T['bg'],8,T['line'])+icon('music',38,y+36,28,T['dim'])+txt(100,y+39,'Nothing playing',14,T['muted'],600)+txt(100,y+60,'Choose a track or import your music',11,T['dim'])
  out+=transport(470,y+12,.86,False)+txt(803,y+45,'No audio source',12,T['dim'])+volume(1130,y+48,130)+ib('expand',1360,y+27,40)
  return out
 out=rect(0,y,w,100,T['panel'])+line(0,y,w,y,T['line'])
 out+=art(20,y+18,64)+txt(100,y+39,'Slow satellites',14,T['text'],600)+txt(100,y+60,'Northbound · Afterglow',11,T['muted'])+ib('heart',306,y+30,36)
 out+=transport(470,y+12,.86,playing)
 out+=txt(466,y+82,'1:42',10,T['muted'],mono=True)+rect(508,y+77,190,3,T['line'],2)+rect(508,y+77,64,3,T['accent'],2)+txt(710,y+82,'4:26',10,T['muted'],mono=True)
 out+=pill(803,y+21,104,'FLAC · 24/96','soft',28)+txt(803,y+70,'Source quality',10,T['dim'])
 out+=ib('queue',937,y+26,40)+txt(980,y+51,'3',11,T['accent'],650)+ib('eq',1011,y+26,40)+ib('wave',1060,y+26,40)
 out+=volume(1130,y+48,130)+ib('expand',1360,y+27,40)
 return out
def track_row(x,y,w,i=0,selected=False,current=False,queue=False,checkbox=False):
 title,artist,album,dur=TRACKS[i%8]
 out=rect(x,y,w,56,T['raised'] if selected else (T['panel'] if current else 'none'),8,T['accent'] if selected else None)
 if checkbox: out+=rect(x+12,y+19,18,18,T['accent'] if selected else T['bg'],4,T['accent'] if selected else T['line'])+(icon('check',x+14,y+21,14,T['ink']) if selected else '')
 xx=x+(44 if checkbox else 16)
 if current: out+=icon('wave',xx,y+18,20,T['accent'])
 else: out+=txt(xx+10,y+33,f'{i+1:02}',12,T['dim'],mono=True,anchor='middle')
 out+=txt(xx+40,y+24,title,13,T['accent'] if current else T['text'],600 if current else 500)+txt(xx+40,y+43,artist+' · '+album,11,T['muted'])
 out+=txt(x+w-150,y+33,'FLAC',10,T['dim'],mono=True)+txt(x+w-82,y+33,dur,12,T['muted'],mono=True)
 out+=ib('heart' if i%3 else 'more',x+w-46,y+10,36)
 return out
def card(x,y,w=200,variant=0,title='Afterglow',subtitle='Northbound · 2024'):
 out=art(x,y,w,variant)+txt(x,y+w+25,title,15,T['text'],600)+txt(x,y+w+46,subtitle,12,T['muted'])
 return out
def panel(x,y,w,h,title=None,subtitle=None):
 out=rect(x,y,w,h,T['panel'],14,T['line'])
 if title: out+=txt(x+24,y+34,title,16,T['text'],600)
 if subtitle: out+=txt(x+24,y+57,subtitle,12,T['muted'])
 return out
def board(title,subtitle,w=1200,h=800,theme=None):
 global T
 T=theme or DARK
 out=rect(0,0,w,h,T['bg'])+rect(0,0,w,h,'url(#dots)')
 out+=logo(40,30,26)+label(180,50,'DESIGN SYSTEM / 1.0')
 out+=txt(40,112,title,32,T['text'],650)+txt(40,143,subtitle,14,T['muted'])
 return out
ASSETS=[]
def save(name,body,w,h,title,desc,category):
 global T
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="{name}-title {name}-desc"><title id="{name}-title">{esc(title)}</title><desc id="{name}-desc">{esc(desc)}</desc>'+defs()+body+'</svg>'
 (OUT/(name+'.svg')).write_text(svg)
 ASSETS.append(dict(id=name,title=title,desc=desc,category=category,w=w,h=h,svg=svg))
 return svg
