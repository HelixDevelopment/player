from design_core import *

def finish(name,body,w,h,title,desc,cat='Full screens'):
 return save(name,body,w,h,title,desc,cat)
T=DARK
# 01 — Flagship performance / now-playing workspace
b=shell('Now playing','Now playing')
b+=txt(248,119,'Your music. Nothing in the way.',13,T['muted'])
b+=pill(1190,112,220,'STUDIO / DARK','neutral',28,'palette')
b+=art(248,153,328)
b+=label(608,181,'FROM YOUR LIBRARY')
b+=txt(608,231,'Slow satellites',38,T['text'],650)
b+=txt(608,264,'Northbound',18,T['muted'],500)
b+=txt(608,291,'Afterglow  ·  2024  ·  Track 01',13,T['dim'])
b+=pill(608,315,76,'FLAC', 'soft')+pill(694,315,108,'24-bit / 96 kHz')+pill(812,315,78,'Stereo')
b+=button(608,366,142,'Track details','secondary','info',38)+ib('heart',764,365,40)+ib('more',814,365,40)
b+=panel(930,153,480,330,'Up next', 'Explicit queue · 3 tracks')
b+=pill(1314,171,72,'Clear all','ghost',26)
for i in range(3):
 b+=rect(950,226+i*73,440,64,T['bg'] if i==0 else 'none',8)
 b+=art(960,234+i*73,48,(i+1)%4,False)+txt(1022,253+i*73,TRACKS[i+1][0],13,T['text'],550)+txt(1022,273+i*73,'Northbound',11,T['muted'])+txt(1336,263+i*73,TRACKS[i+1][3],11,T['muted'],mono=True)+icon('grip',1362,248+i*73,18)
b+=button(951,444,438,'Open full queue','ghost','queue',30)
b+=panel(248,510,1162,276)
b+=label(272,541,'LIVE WAVEFORM')+pill(433,523,82,'Audio reactive','soft',24)
b+=txt(1386,541,'01:42 / 04:26',12,T['muted'],mono=True,anchor='end')
b+=wave(278,582,1100,112,.38,True)
b+=txt(278,739,'−48 dB',10,T['dim'],mono=True)+txt(1378,739,'Peak −1.2 dBFS · analysis only',10,T['dim'],mono=True,anchor='end')
b+=ib('wave',1298,721,32)+ib('expand',1344,721,32)
b+=txt(248,818,'PLAYING FROM  AFTERGLOW',11,T['dim'],600,extra='letter-spacing="1.2"')+txt(1408,818,'8 tracks · 34 min',12,T['muted'],anchor='end')
b+=player_bar()
finish('01-now-playing-dark',b,1440,960,'Now playing — Studio Dark','Album-led desktop workspace with persistent transport, explicit queue, source-quality metadata and reactive waveform. Fictional music and original vector sleeve.')

# 02 — Album library
b=shell('Library','Library',search='Search albums, artists, tracks')
b+=txt(248,119,'2,418 tracks  ·  186 albums  ·  42 artists',13,T['muted'])
b+=button(1224,111,184,'Import music','primary','plus',38)
b+=pill(248,149,92,'Albums','soft',34)+pill(350,149,80,'Tracks','ghost',34)+pill(440,149,82,'Artists','ghost',34)
b+=button(1110,149,144,'Recently added','ghost','down',34)+ib('grid',1268,146,40,active=True)+ib('list',1318,146,40)+ib('filter',1368,146,40)
for i,(name,sub) in enumerate([('Afterglow','Northbound'),('Open water','Harbor Assembly'),('Slow signals','Mira Sol'),('Blue hour','The Low Tide'),('Soft focus','Ellis North'),('Parallel lines','Kite Theory')]):
 x=248+(i%3)*398; y=216+(i//3)*294
 b+=card(x,y,236,i,name,sub+' · 2024')
 b+=ib('play',x+184,y+184,40,active=True)
b+=txt(248,826,'Showing 6 of 186 albums',12,T['muted'])+button(1250,802,158,'Load more','secondary','down',36)
b+=player_bar()
finish('02-library-albums',b,1440,960,'Library — album grid','Original vector album covers; persistent navigation, search, import, view switches and sorting. Grid is a library view, not a music recommendation service.')

# 03 — Track library + bulk selection
b=shell('Library','Library')
b+=pill(248,114,90,'Albums','ghost',32)+pill(348,114,84,'Tracks','soft',32)+pill(442,114,84,'Artists','ghost',32)
b+=txt(1408,137,'2,418 tracks · 164 hours',12,T['muted'],anchor='end')
b+=rect(248,173,1160,58,T['raised'],10,T['accent'])
b+=txt(268,208,'4 tracks selected',14,T['text'],600)+button(535,182,136,'Add to queue','ghost','queue',38)+button(680,182,145,'Add to playlist','ghost','plus',38)+button(835,182,115,'Edit tags','ghost','edit',38)+button(1230,182,158,'Clear selection','ghost','close',38)
b+=label(266,268,'')
b+=rect(260,253,18,18,T['accent'],4)+icon('check',262,255,14,T['ink'])+txt(306,268,'TITLE / ARTIST',11,T['dim'],600)+txt(954,268,'ALBUM',11,T['dim'],600)+txt(1216,268,'FORMAT',11,T['dim'],600)+txt(1320,268,'TIME',11,T['dim'],600)
for i in range(9): b+=track_row(248,286+i*57,1160,i,selected=i in [0,2,4,5],current=i==0,checkbox=True)
b+=txt(248,833,'Selection is independent of the currently playing track.',12,T['muted'])+pill(1220,809,188,'Shift-click for a range','neutral',28)
b+=player_bar()
finish('03-library-tracks-selection',b,1440,960,'Library — tracks and bulk selection','Selection toolbar exposes queue, playlist and tag actions. Current playback, selection and explicit queue are separate concepts.')

# 04 — Queue and playlist context
b=shell('Playlists','Playlists')
b+=txt(248,120,'Late night drive',22,T['text'],600)+pill(500,99,94,'12 tracks','neutral',28)
b+=button(1080,106,154,'Play playlist','primary','play',40)+ib('more',1246,106,40)+ib('edit',1298,106,40)+ib('download',1350,106,40)
b+=panel(248,164,744,652,'Playlist context','Original order · playing track 01')
b+=pill(842,183,126,'Save as M3U8','ghost',28,'download')
for i in range(8):
 b+=track_row(266,238+i*66,708,i,current=i==0)
 if i==2: b+=pill(796,238+i*66+13,72,'QUEUED','soft',24)
b+=panel(1012,164,396,652,'Play next','Explicit queue overrides context')
b+=txt(1036,246,'These tracks play before the list resumes.',12,T['muted'])
for i in range(3):
 b+=rect(1032,272+i*91,356,80,T['bg'],9,T['line'])+icon('grip',1044,300+i*91,18)+art(1072,286+i*91,52,i+1,False)+txt(1136,307+i*91,TRACKS[i+1][0],12,T['text'],600)+txt(1136,327+i*91,'Northbound',11,T['muted'])+ib('close',1344,291+i*91,32)
b+=txt(1036,568,'Then resumes at',11,T['dim'],600)+txt(1036,597,'04  Coastline',14,T['text'],600)+txt(1036,621,'Northbound · Afterglow',12,T['muted'])
b+=button(1032,662,356,'Clear queue','secondary','close',40)+button(1032,716,356,'Add selected tracks','ghost','plus',40)
b+=txt(1036,789,'Removing a queued item never deletes a file.',10,T['muted'])
b+=player_bar()
finish('04-queue-and-context',b,1440,960,'Queue — explicit next versus playlist context','Queue panel shows consumed order and resume point. Grip handles support keyboard reorder; removal is non-destructive.')

# 05 — Immersive visualizer
T=DARK
b=rect(0,0,1440,960,T['bg'])+circle(760,370,570,'url(#ambient)')
b+=logo(40,32,28)+pill(226,34,112,'FOCUS VIEW','neutral',28)+txt(1150,52,'Esc  Back to workspace',12,T['muted'],anchor='end')+ib('settings',1260,26,40)+ib('minimize',1310,26,40)+ib('close',1360,26,40)
b+=art(72,145,246)+label(350,174,'NORTHBOUND / AFTERGLOW')
b+=txt(348,235,'Slow satellites',46,T['text'],650)+txt(350,274,'Northbound',20,T['muted'])+pill(350,302,162,'FLAC · 24-bit / 96 kHz','soft',30)
b+=pill(1124,156,116,'Waveform','soft',34)+pill(1250,156,116,'Spectrum','ghost',34)
b+=txt(72,411,'LIVE SIGNAL',11,T['dim'],650,extra='letter-spacing="2"')+pill(1180,389,186,'Pause visualization','neutral',34,'pause')
b+=wave(80,478,1280,200,.38,True,11)
b+=line(72,716,1368,716,T['line'])
b+=txt(72,752,'01:42',14,T['muted'],mono=True)+txt(1368,752,'−02:44',14,T['muted'],mono=True,anchor='end')
b+=transport(578,787,1.1)+volume(1100,817,140)
b+=txt(72,815,'OUTPUT  ·  MacBook speakers',11,T['dim'],600)+txt(72,842,'Source format shown; output route may resample.',11,T['muted'])
b+=pill(536,891,164,'Motion: full','ghost',30,'wave')+pill(718,891,166,'Skin: Studio Dark','ghost',30,'palette')
finish('05-immersive-visualizer',b,1440,960,'Immersive visualizer — waveform focus','Large live signal with visible pause control, stable metadata and exit route. Static SVG is an illustrative frame; companion demo drives paths from audio analysis.')

# 06 — EQ / DSP
b=shell('Sound studio','Now playing')
b+=txt(248,120,'Shape the sound. Keep the original safe.',13,T['muted'])
b+=pill(1166,108,116,'EQ enabled','soft',32)+pill(1292,108,116,'Safe gain','neutral',32,'lock')
b+=panel(248,162,1160,440,'Equalizer','10 bands · ±12 dB · double-click a band to reset')
b+=button(272,239,180,'Flat / reference','secondary','down',38)+button(466,239,150,'Save preset','ghost','plus',38)+button(1240,239,142,'Reset all','ghost','repeat',38)
b+=txt(290,321,'+12',11,T['dim'],mono=True)+txt(290,408,'0',11,T['dim'],mono=True)+txt(290,510,'−12',11,T['dim'],mono=True)
for yy in [316,403,505]: b+=line(332,yy,1366,yy,T['line'],1,'stroke-dasharray="4 6"')
gains=[0,2,3,1,-1,-2,0,2,1,0]; freqs=['31','62','125','250','500','1k','2k','4k','8k','16k']
for i,g in enumerate(gains):
 x=376+i*106; y=403-g*7
 b+=rect(x-3,310,6,202,T['bg'],3,T['line'])+rect(x-3,y,6,403-y,T['accent'],3)
 b+=rect(x-13,y-8,26,16,T['text'],4)+line(x-7,y,x+7,y,T['dim'])
 b+=txt(x,548,freqs[i],12,T['muted'],mono=True,anchor='middle')+txt(x,574,f'{g:+d} dB',11,T['accent'],mono=True,anchor='middle')
b+=txt(290,574,'Hz',10,T['dim'])
b+=panel(248,622,566,192,'Processing chain','Non-destructive · applies to output only')
for i,(s,v) in enumerate([('Preamp','−3.0 dB'),('Loudness','Track gain'),('Crossfeed','Off')]):
 b+=txt(274,701+i*34,s,13,T['muted'])+txt(780,701+i*34,v,13,T['text'],mono=True,anchor='end')
b+=panel(834,622,574,192,'Output protection','Never label processing as “bit-perfect”')
b+=icon('check',858,689,20,T['accent'])+txt(890,705,'True-peak limiter available',13,T['text'])+txt(858,738,'EQ, gain and crossfeed disable bit-perfect claims.',12,T['muted'])+txt(858,766,'Clipping warnings appear before unsafe presets apply.',12,T['muted'])
b+=player_bar()
finish('06-equalizer-dsp',b,1440,960,'Sound studio — equalizer and DSP','Numeric band values, reference preset, reset, preamp and explicit processing status. Advanced effects are capability-gated.')

# 07 — Skin studio
b=shell('Skin studio','Now playing')
b+=txt(248,120,'One player. Your signature. Layout and behavior stay predictable.',13,T['muted'])
b+=button(1218,108,190,'Import skin','primary','upload',38)
b+=panel(248,162,754,480,'Preview','Studio Dark · editable design tokens')
b+=rect(272,242,706,290,T['bg'],12,T['line'])+art(294,264,172)+txt(490,285,'NOW PLAYING',10,T['dim'],600)+txt(490,325,'Slow satellites',25,T['text'],650)+txt(490,353,'Northbound · Afterglow',13,T['muted'])+wave(490,383,454,62,.4)+transport(490,464,.65)
b+=pill(272,561,112,'Desktop','soft',30)+pill(394,561,100,'Compact','ghost',30)+pill(504,561,90,'Mobile','ghost',30)+txt(976,581,'Preview only',11,T['dim'],anchor='end')
b+=panel(1022,162,386,480,'Skin properties')
for i,(n,v) in enumerate([('Name','Studio Dark'),('Accent','Mint / #79E3C2'),('Surface','Graphite'),('Corner radius','12 px'),('Waveform','Mirrored bars'),('Motion','Full')]):
 b+=txt(1046,244+i*57,n,11,T['dim'])+txt(1046,267+i*57,v,14,T['text'],550)
b+=panel(248,664,1160,150,'Installed skins','Imported skins cannot run scripts or change control meanings')
for i,(n,c,sub) in enumerate([('Studio Dark','#79E3C2','Balanced / default'),('Daylight','#116B53','Light / high legibility'),('Classic Metal','#F3C580','Compact / tactile'),('High Contrast','#FFFFFF','Maximum clarity')]):
 x=270+i*285;b+=rect(x,725,266,66,T['bg'],9,T['accent'] if i==0 else T['line'])+circle(x+24,758,10,c,T['line'])+txt(x+46,752,n,13,T['text'],600)+txt(x+46,774,sub,10,T['muted'])
b+=player_bar()
finish('07-skin-studio',b,1440,960,'Skin studio — safe white-label theming','Token-based skins, live preview and explicit apply semantics. Classic styling changes presentation, not queue or playback behavior.')

# 08 — Audio settings
b=shell('Settings','Now playing')
b+=pill(248,113,90,'Audio','soft',32)+pill(348,113,104,'Library','ghost',32)+pill(462,113,124,'Appearance','ghost',32)+pill(596,113,120,'Shortcuts','ghost',32)+pill(726,113,102,'Privacy','ghost',32)
b+=panel(248,171,1160,224,'Output device','Changes apply on confirmation; playback pauses briefly if the route restarts')
b+=rect(272,252,650,46,T['bg'],8,T['line'])+icon('monitor',288,265,20)+txt(324,281,'MacBook Pro speakers',14,T['text'])+icon('down',886,265,20)
b+=pill(950,258,176,'System default','soft',32)+txt(272,335,'Exclusive / bit-perfect modes are separate capabilities, not assumptions.',12,T['muted'])+txt(272,361,'Supported format: negotiated with the selected device.',12,T['muted'])
b+=panel(248,415,566,397,'Playback')
for i,(n,sub,on) in enumerate([('Gapless playback','For compatible formats and transitions',True),('Restore position on launch','Resume the last local track',True),('Remember explicit queue','Keep pending items across sessions',True),('Prevent sleep during playback','Release the lock when paused',False)]):
 y=490+i*76;b+=txt(272,y,n,14,T['text'],550)+txt(272,y+23,sub,11,T['muted'])+rect(738,y-15,48,26,T['accent'] if on else T['line'],13)+circle(773 if on else 751,y-2,9,T['ink'] if on else T['text'])
b+=panel(834,415,574,397,'Volume & loudness')
b+=txt(858,490,'Normalization',14,T['text'],550)+button(1110,465,272,'ReplayGain / track','secondary','down',40)
b+=txt(858,548,'Fallback for untagged audio',13,T['muted'])+txt(1380,548,'−18 LUFS',13,T['text'],anchor='end',mono=True)
b+=txt(858,607,'Prevent clipping',13,T['muted'])+pill(1250,586,132,'Enabled','soft',30)
b+=txt(858,674,'Advanced routing, exclusive mode and DSD handling',13,T['text'],550)+txt(858,701,'Only shown when the audio backend advertises support.',12,T['muted'])+button(858,739,220,'View capabilities','ghost','info',36)
b+=player_bar()
finish('08-settings-audio',b,1440,960,'Settings — audio and playback','Output selection, gapless, resume, queue persistence and normalization. Unsupported engine capabilities are not presented as working toggles.')

# 09 — Tag editor
b=shell('Edit metadata','Library')
b+=txt(248,120,'4 files selected · changes are written only when you save',13,T['muted'])
b+=button(1098,106,144,'Cancel','secondary',h=40)+button(1256,106,152,'Save changes','primary','check',h=40)
b+=panel(248,164,344,648,'Selected files','Mixed values remain visibly mixed')
for i in range(4): b+=rect(268,244+i*92,304,80,T['bg'],8)+art(280,256+i*92,56,i,False)+txt(350,276+i*92,TRACKS[i][0],12,T['text'],600)+txt(350,298+i*92,'Northbound',11,T['muted'])
b+=txt(268,662,'Original files stay untouched until save.',11,T['muted'])+txt(268,686,'Unsupported fields are read-only.',11,T['muted'])+button(268,730,304,'Review file permissions','ghost','lock',36)
b+=panel(612,164,796,648,'Common tags','Fields with different values show “Multiple values”')
for i,(n,v) in enumerate([('Title','Multiple values'),('Artist','Northbound'),('Album','Afterglow'),('Album artist','Northbound'),('Year','2024'),('Genre','Ambient / electronic')]):
 x=640+(i%2)*374;y=252+(i//2)*100;b+=txt(x,y,n,12,T['muted'],600)+rect(x,y+14,350,46,T['bg'],8,T['line'])+txt(x+14,y+43,v,13,T['dim'] if i==0 else T['text'])
b+=txt(640,584,'Track numbering',12,T['muted'],600)+button(640,602,224,'Keep existing numbers','secondary','down',40)
b+=txt(900,584,'Artwork',12,T['muted'],600)+art(900,606,82,0,False)+button(998,611,154,'Replace art','ghost','upload',36)+button(1160,611,150,'Keep mixed','ghost','lock',36)
b+=rect(636,723,748,58,T['bg'],8)+icon('info',650,741,20,T['accent2'])+txt(684,747,'Saving updates embedded tags, not filenames.',12,T['text'])+txt(684,767,'File renaming is a separate, previewed operation.',11,T['muted'])
b+=player_bar()
finish('09-metadata-editor',b,1440,960,'Metadata editor — safe batch editing','Mixed values, explicit save, artwork replacement and file-permission checks. Tag writes and file renaming are separate operations.')

# 10 — Command / search overlay
b=shell('Library','Library')
for i in range(6): b+=card(248+(i%3)*398,210+(i//3)*294,236,i,['Afterglow','Open water','Slow signals'][i%3])
b+=rect(0,36,1440,924,'#07100F',extra='opacity=".78"')
b+=panel(370,154,700,566)
b+=rect(394,178,652,58,T['bg'],10,T['accent'])+icon('search',410,196,22,T['accent'])+txt(448,214,'north',18,T['text'])+pill(984,193,44,'Esc',h=26)
b+=label(398,270,'BEST MATCH')
b+=rect(394,286,652,76,T['raised'],10)+art(408,298,52,0,False)+txt(476,318,'Northbound',15,T['text'],600)+txt(476,341,'Artist · 4 albums · 32 tracks',12,T['muted'])+pill(960,309,64,'Enter',h=26)
b+=label(398,397,'ALBUMS & TRACKS')
for i,(n,s) in enumerate([('Northern lights','Track · Northbound'),('Afterglow','Album · Northbound'),('Northbound radio','Radio · saved station')]):
 b+=icon('music',408,420+i*57,20)+txt(444,435+i*57,n,14,T['text'])+txt(444,453+i*57,s,11,T['muted'])
b+=rule(394,612,652)+txt(398,650,'↑ ↓ Navigate    Enter Open    Esc Close',12,T['muted'])+txt(1046,691,'Local results only',11,T['dim'],anchor='end')
b+=player_bar()
finish('10-search-command',b,1440,960,'Search — keyboard-first local results','Modal search preserves the player, distinguishes result types and exposes keyboard navigation. No implicit remote search or playback.')

# 11 — First run / empty library
b=shell('Welcome','Library')
b+=rect(248,154,1160,650,T['panel'],16,T['line'])
b+=circle(830,365,225,'url(#ambient)')+art(724,224,212)
b+=label(300,220,'MAKE YOURSELF AT HOME')
b+=txt(300,281,'Your music.',36,T['text'],650)+txt(300,326,'Your space.',36,T['accent'],650)
b+=txt(300,375,'Bring your local collection into one calm workspace.',14,T['muted'])+txt(300,401,'No account. No upload. No automatic playback.',14,T['muted'])
b+=button(300,448,222,'Choose a music folder','primary','folder',46)+button(538,448,144,'Open files','secondary','plus',46)
b+=txt(300,536,'You can add more folders or remove them later.',12,T['dim'])
b+=rule(300,575,1056)
for i,(n,s,ic) in enumerate([('01  Import','Index files without changing them','folder'),('02  Make it yours','Pick a skin and playback defaults','palette'),('03  Press play','Start only when you are ready','play')]):
 x=300+i*354;b+=icon(ic,x,611,24,T['accent'])+txt(x,663,n,15,T['text'],600)+txt(x,690,s,12,T['muted'])
b+=txt(248,837,'Nothing is imported until you choose a location.',12,T['muted'])+button(1180,811,228,'Skip and explore empty player','ghost','chevron',34)
b+=player_bar(empty=True)
finish('11-onboarding-empty',b,1440,960,'First run — consent-led import','No automatic folder scanning or playback. Empty transport is disabled in implementation; this SVG is a layout illustration.')

# 12 — Recovery / error screen
b=shell('Library','Library')
b+=pill(248,117,194,'3 files need attention','warn',32,'warning')
b+=panel(248,176,1160,310,'We could not open this file','Playback paused safely. Your library and playlists are unchanged.')
b+=rect(272,263,66,66,T['raised'],12)+icon('warning',288,279,34,T['accent2'])
b+=txt(358,286,'Missing file: Coastline.flac',18,T['text'],600)+txt(358,315,'/Music/Northbound/Afterglow/04 Coastline.flac',12,T['muted'],mono=True)
b+=txt(358,343,'The drive may be disconnected or the file may have moved.',13,T['muted'])
b+=button(272,385,168,'Locate file','primary','folder',42)+button(454,385,164,'Skip track','secondary','next',42)+button(632,385,178,'Copy diagnostics','ghost','info',42)
b+=txt(272,459,'No files were deleted. The explicit queue is preserved.',12,T['muted'])
b+=panel(248,508,1160,304,'Import issues','Partial success is still success: 2,415 files are ready to play')
for i,(n,s) in enumerate([('02 Blue hour.wav','Unsupported codec · review format support'),('03 A little further.flac','Read permission denied · check folder access'),('05 Notes.txt','Not an audio file · ignored without changing it')]):
 b+=txt(272,603+i*65,n,14,T['text'],550)+txt(272,626+i*65,s,12,T['muted'])+button(1210,583+i*65,172,'Review','ghost','chevron',36)
b+=player_bar(playing=False)
finish('12-errors-recovery',b,1440,960,'Recovery — missing files and partial import','Actionable errors preserve the library and queue. Diagnostics are copied only on request; no silent destructive cleanup.')

# 13 — Light skin
T=LIGHT
b=shell('Now playing','Now playing',theme=LIGHT)
b+=txt(248,120,'A quieter interface for bright spaces.',13,T['muted'])+pill(1210,108,198,'DAYLIGHT / LIGHT','neutral',30,'sun')
b+=art(248,160,320)+label(600,185,'FROM YOUR LIBRARY')+txt(600,235,'Slow satellites',36,T['text'],650)+txt(600,270,'Northbound',18,T['muted'])+txt(600,299,'Afterglow · 2024',13,T['muted'])
b+=pill(600,326,164,'FLAC · 24-bit / 96 kHz','soft',30)+button(600,378,144,'Track details','secondary','info',38)+ib('heart',760,377,40)
b+=panel(920,160,488,326,'Up next','Explicit queue · 3 tracks')
for i in range(3): b+=art(944,235+i*72,52,i+1,False)+txt(1012,255+i*72,TRACKS[i+1][0],13,T['text'],600)+txt(1012,276+i*72,'Northbound',11,T['muted'])+txt(1368,266+i*72,TRACKS[i+1][3],11,T['muted'],anchor='end',mono=True)
b+=panel(248,514,1160,274,'Live waveform','Audio reactive · pause available in focus view')
b+=wave(276,600,1100,110,.38,True)
b+=txt(276,756,'01:42 / 04:26',12,T['muted'],mono=True)+txt(1378,756,'Analysis only · not an output-level guarantee',11,T['muted'],anchor='end')
b+=player_bar()
finish('13-now-playing-light',b,1440,960,'Now playing — Daylight skin','Light theme uses darker semantic colors rather than inverting dark-theme accents. Same layout, hierarchy and control semantics.')
T=DARK

# 14 — Classic metal compact stack
b=board('Classic / compact performance', 'Winamp-inspired modularity, modern targets and explicit labels. Original metal styling; no copied sprites.',1200,860)
x=160;y=205;w=880
b+=rect(x-8,y-8,w+16,590,'#0B1116',14,'#61717A',2)
for k,(name,h) in enumerate([('PLAYER',182),('EQUALIZER',184),('PLAYLIST',174)]):
 yy=y+sum([182,184,174][:k])+k*12
 b+=rect(x,yy,w,h,'url(#metal)',7,'#75848B',1)+line(x+8,yy+2,x+w-8,yy+2,'#93A0A6',1)
 b+=rect(x+12,yy+10,w-24,25,'#1B2831',4)+txt(x+w/2,yy+28,'FUSE  /  '+name,12,'#D8E5E7',650,'middle',extra='letter-spacing="3"')
 if k==0:
  b+=rect(x+18,yy+47,180,78,'#0D191C',5,'#63777A')+txt(x+32,yy+84,'01:42',30,'#A5F0C9',500,mono=True)+spectrum(x+30,yy+94,156,22,24,3,True)
  b+=txt(x+220,yy+68,'01  NORTHBOUND',12,'#F3C580',600,mono=True)+txt(x+220,yy+94,'SLOW SATELLITES',20,'#E8F3E8',600,mono=True)+txt(x+220,yy+118,'FLAC  /  24-96  /  STEREO',11,'#AFC5C9',mono=True)
  b+=pill(x+674,yy+52,178,'SOURCE QUALITY','soft',26)
  b+=rect(x+20,yy+141,w-40,5,'#13212A',3)+rect(x+20,yy+141,290,5,'#79E3C2',3)+circle(x+310,yy+143,7,'#E9F2E8')
  b+=transport(x+20,yy+151,.64)+volume(x+290,yy+169,150)+button(x+570,yy+151,116,'Queue · 3','secondary','queue',28)+button(x+698,yy+151,154,'Classic skin','ghost','palette',28)
 if k==1:
  b+=pill(x+20,yy+48,94,'EQ ON','soft',26)+button(x+126,yy+47,124,'Flat','secondary','down',28)+button(x+264,yy+47,114,'Reset','ghost','repeat',28)+txt(x+w-24,yy+65,'PRE  −3 dB',11,'#D8E5E7',anchor='end',mono=True)
  for i,g in enumerate([0,2,3,1,-1,-2,0,2,1,0]):
   xx=x+48+i*83;cy=yy+123-g*2
   b+=line(xx,yy+92,xx,yy+153,'#14232A',6)+line(xx,yy+92,xx,yy+153,'#79918D',1)+rect(xx-9,cy-6,18,12,'#D3DFDB',3,'#172D32')+txt(xx,yy+174,['31','62','125','250','500','1K','2K','4K','8K','16K'][i],10,'#D8E5E7',mono=True,anchor='middle')
 if k==2:
  b+=txt(x+22,yy+60,'LATE NIGHT DRIVE',12,'#F3C580',600,mono=True)+txt(x+w-22,yy+60,'12 TRACKS / 48:32',11,'#D8E5E7',mono=True,anchor='end')
  for i in range(3):
   yy2=yy+73+i*29
   b+=rect(x+16,yy2,w-32,27,'#152A2B' if i==0 else '#1B2831',3)+txt(x+28,yy2+19,f'{i+1:02}  {TRACKS[i][0].upper()}  —  NORTHBOUND',12,'#A5F0C9' if i==0 else '#D8E5E7',mono=True)+txt(x+w-30,yy2+19,TRACKS[i][3],12,'#D8E5E7',mono=True,anchor='end')
b+=txt(160,821,'STACK ORDER: PLAYER → EQ → PLAYLIST   ·   Minimum logical width: 560 px   ·   No 275 px hit-target constraint',11,T['muted'])
finish('14-classic-compact',b,1200,860,'Classic Metal — compact modular stack','Original beveled surfaces, spectral display, transport, EQ and playlist modules. Modern target sizes and readable labels replace tiny legacy controls.')

# 15 — Mini and shade modes
b=board('Small modes, complete control','Mini player and window-shade strip share the same state and queue. Dimensions are logical pixels.',1200,800)
b+=label(60,211,'MINI / 420 × 248')
b+=rect(60,235,420,248,T['panel'],16,T['line'])+art(80,255,92)+txt(190,278,'Slow satellites',17,T['text'],650)+txt(190,303,'Northbound',13,T['muted'])+ib('more',430,254,32)
b+=wave(82,365,374,34,.38)+transport(116,415,.68)+ib('expand',424,423,32)
b+=label(560,211,'SHADE / 560 × 72')
b+=rect(560,235,560,72,T['panel'],12,T['line'])+logo(576,257,24,False)+txt(618,264,'Slow satellites',13,T['text'],600)+txt(618,286,'Northbound · 01:42',10,T['muted'])+transport(808,249,.64)+ib('expand',1070,251,40)
b+=txt(560,338,'Shade keeps play, previous, next and expand reachable.',12,T['muted'])+txt(560,361,'Shuffle/repeat remain in the overflow menu, not hidden toggles.',12,T['muted'])
b+=panel(60,540,1060,190,'Mode contract')
for i,(n,s) in enumerate([('One playback state','All modes reflect the same track and position'),('No lost queue','Changing size never clears pending items'),('Accessible exit','Expand is labeled and keyboard reachable'),('Minimum dimensions','Do not shrink below readable target limits')]):
 x=84+i*260;b+=txt(x,623,n,13,T['text'],600)+txt(x,650,s[:31],11,T['muted'])+txt(x,669,s[31:],11,T['muted'])
finish('15-mini-and-shade',b,1200,800,'Mini player and shade mode','Compact layouts preserve transport, identity and expansion. Shared state, no hidden queue destruction, no legacy tiny-target requirement.')

# 16 — Mobile trio
b=board('Pocket studio','390 × 844 logical px · touch-first targets · safe-area insets are host responsibilities',1290,1030)
for j,(name,kind) in enumerate([('NOW PLAYING','now'),('LIBRARY','library'),('UP NEXT','queue')]):
 x=40+j*420;y=185
 b+=rect(x,y,390,790,T['shell'],26,T['line'])+txt(x+24,y+35,'9:41',12,T['text'],600)+txt(x+350,y+35,'100%',11,T['muted'],anchor='end')
 b+=logo(x+22,y+60,22,False)+txt(x+58,y+80,name,12,T['text'],650,extra='letter-spacing="1"')+ib('search' if kind!='queue' else 'more',x+326,y+53,44)
 if kind=='now':
  b+=art(x+35,y+119,320)+txt(x+28,y+485,'Slow satellites',26,T['text'],650)+txt(x+28,y+514,'Northbound · Afterglow',14,T['muted'])+ib('heart',x+324,y+464,44)
  b+=wave(x+28,y+550,334,48,.38)+txt(x+28,y+625,'01:42',11,T['muted'],mono=True)+txt(x+362,y+625,'−02:44',11,T['muted'],mono=True,anchor='end')
  b+=transport(x+63,y+650,1.0)+pill(x+28,y+721,128,'FLAC · 24/96','soft',28)+ib('queue',x+232,y+714,44)+ib('eq',x+282,y+714,44)+ib('volume',x+332,y+714,44)
 elif kind=='library':
  b+=txt(x+24,y+133,'Your library',27,T['text'],650)+pill(x+24,y+157,82,'Albums','soft',30)+pill(x+116,y+157,76,'Tracks','ghost',30)+pill(x+202,y+157,76,'Artists','ghost',30)
  for i in range(4):
   xx=x+24+(i%2)*180;yy=y+213+(i//2)*242;b+=art(xx,yy,162,i)+txt(xx,yy+187,['Afterglow','Open water','Slow signals','Blue hour'][i],14,T['text'],600)+txt(xx,yy+208,['Northbound','Harbor Assembly','Mira Sol','The Low Tide'][i],11,T['muted'])
  b+=rect(x+12,y+704,366,68,T['panel'],14,T['line'])+art(x+22,y+714,48)+txt(x+82,y+734,'Slow satellites',12,T['text'],600)+txt(x+82,y+753,'Northbound',10,T['muted'])+ib('pause',x+276,y+716,44,active=True)+ib('next',x+326,y+716,44)
 else:
  b+=txt(x+24,y+133,'Up next',28,T['text'],650)+txt(x+24,y+161,'3 explicit tracks · then Afterglow',12,T['muted'])
  for i in range(3):
   yy=y+195+i*104;b+=rect(x+20,yy,350,90,T['panel'],12,T['line'])+icon('grip',x+30,yy+31,20)+art(x+60,yy+17,56,i+1,False)+txt(x+130,yy+36,TRACKS[i+1][0],13,T['text'],600)+txt(x+130,yy+58,'Northbound',11,T['muted'])+ib('close',x+318,yy+23,44)
  b+=txt(x+24,y+548,'THEN RESUMES AT',10,T['dim'],600)+txt(x+24,y+580,'04  Coastline',16,T['text'],600)+txt(x+24,y+605,'Northbound · Afterglow',12,T['muted'])
  b+=button(x+24,y+650,342,'Clear queue','secondary','close',44)+button(x+24,y+708,342,'Back to player','ghost','back',44)
 b+=rect(x+142,y+773,106,4,T['dim'],2)
finish('16-mobile-screens',b,1290,1030,'Mobile — player, library and queue','Touch-first 44 px targets, readable hierarchy and explicit queue semantics. Conceptual mobile layouts; native safe areas and gestures require platform implementation.')

# 17 — Tablet / medium workspace
b=shell('Now playing','Now playing',w=1100,h=820,sidebar=False)
b+=pill(32,111,124,'Now playing','soft',30)+pill(168,111,94,'Library','ghost',30)+pill(274,111,94,'Queue','ghost',30)
b+=art(32,174,280)+txt(340,211,'Slow satellites',30,T['text'],650)+txt(340,246,'Northbound · Afterglow',15,T['muted'])+pill(340,272,164,'FLAC · 24-bit / 96 kHz','soft',30)
b+=button(340,332,156,'Track details','secondary','info',40)+ib('heart',510,332,40)
b+=panel(720,174,348,330,'Up next','3 explicit tracks')
for i in range(3): b+=art(740,246+i*73,48,i+1,False)+txt(802,265+i*73,TRACKS[i+1][0],12,T['text'],600)+txt(802,286+i*73,'Northbound',11,T['muted'])
b+=panel(32,530,1036,162,'Live waveform')+wave(56,596,988,56,.38)
b+=player_bar(720,1100)
finish('17-tablet-workspace',b,1100,820,'Medium workspace — 1100 px','Navigation becomes labeled horizontal tabs; artwork, metadata, queue and waveform remain visible without horizontal scrolling.')

# 18 — Sleep timer / output dialog
b=shell('Now playing','Now playing')
b+=rect(0,36,1440,924,'#07100F',extra='opacity=".72"')
b+=panel(426,174,588,568,'Sleep timer','Stop gently without changing your files')
b+=pill(450,260,112,'15 minutes','ghost',34)+pill(574,260,112,'30 minutes','soft',34)+pill(698,260,112,'45 minutes','ghost',34)+pill(822,260,166,'End of track','ghost',34)
b+=txt(450,345,'Custom duration',12,T['muted'],600)+rect(450,361,190,46,T['bg'],8,T['line'])+txt(466,390,'30',16,T['text'],mono=True)+txt(654,390,'minutes',13,T['muted'])
b+=txt(450,451,'At the end',12,T['muted'],600)+button(450,468,540,'Fade out, then pause','secondary','down',44)
b+=rect(450,544,540,62,T['bg'],8)+icon('info',466,563,20,T['accent2'])+txt(500,568,'Pauses playback; does not shut down the computer.',12,T['text'])+txt(500,590,'System shutdown is a separate, permission-gated action.',11,T['muted'])
b+=button(450,650,254,'Cancel','secondary',h=44)+button(720,650,270,'Start timer','primary','clock',h=44)
b+=player_bar()
finish('18-sleep-timer-dialog',b,1440,960,'Sleep timer — explicit action and outcome','Modal dialog distinguishes pause from system shutdown, exposes duration and fade behavior, and preserves playback state on cancel.')

# 19 — Radio / podcasts capability screen
b=shell('Radio','Radio')
b+=txt(248,120,'Saved stations and subscriptions · provider availability varies',13,T['muted'])+button(1210,108,198,'Add station URL','primary','plus',38)
b+=pill(248,151,94,'Radio','soft',32)+pill(352,151,116,'Podcasts','ghost',32)
b+=panel(248,208,1160,236,'Your saved stations','Local entries work without a directory subscription')
for i,(n,s) in enumerate([('Northbound FM','Ambient / electronic · saved URL'),('Open frequency','Community radio · saved URL'),('Night service','Downtempo · saved URL')]):
 x=270+i*380;b+=rect(x,282,356,132,T['bg'],10,T['line'])+icon('radio',x+18,302,28,T['accent'])+txt(x+62,320,n,15,T['text'],600)+txt(x+18,351,s,11,T['muted'])+button(x+18,368,120,'Play station','ghost','play',32)+ib('more',x+302,366,36)
b+=panel(248,466,1160,344,'Connection state','A stream is not a seekable local file')
b+=icon('warning',276,550,28,T['accent2'])+txt(324,570,'Northbound FM is reconnecting',18,T['text'],600)+txt(324,601,'Buffering · attempt 2 of 3 · your local queue is unchanged',13,T['muted'])
b+=button(324,638,150,'Retry now','primary','repeat',40)+button(490,638,180,'Return to library','secondary','library',40)
b+=txt(276,744,'No seeking, duration or offline claims for live radio. Recording appears only when supported and permitted.',12,T['muted'])
b+=player_bar(playing=False)
finish('19-radio-stream-state',b,1440,960,'Radio — saved stations and reconnect state','Provider-independent saved URLs, explicit buffering and retry. Live streams do not inherit local-file seeking or duration assumptions.')

# 20 — Lyrics / track information
b=shell('Track details','Now playing')
b+=art(248,164,286)+txt(566,205,'Slow satellites',32,T['text'],650)+txt(566,241,'Northbound · Afterglow',16,T['muted'])+pill(566,268,164,'FLAC · 24-bit / 96 kHz','soft',30)
b+=panel(860,164,548,314,'Audio facts','Source metadata, not a guarantee of output fidelity')
for i,(n,v) in enumerate([('Codec','FLAC / lossless container'),('Sample rate','96,000 Hz'),('Bit depth','24-bit'),('Channels','Stereo'),('File size','86.4 MB'),('ReplayGain','Track −7.2 dB')]):
 b+=txt(884,252+i*34,n,12,T['muted'])+txt(1384,252+i*34,v,12,T['text'],mono=True,anchor='end')
b+=panel(248,510,1160,302,'Lyrics','No lyrics are bundled with this fictional demo track')
b+=icon('music',760,588,40,T['dim'])+txt(828,650,'No embedded lyrics found',18,T['text'],600,'middle')+txt(828,680,'Add your own plain text or timed LRC file. Nothing is fetched automatically.',12,T['muted'],anchor='middle')
b+=button(710,722,236,'Add lyrics file','secondary','plus',40)
b+=player_bar()
finish('20-track-details-lyrics',b,1440,960,'Track details — facts and lyrics empty state','Separates source facts from output claims; lyrics are local and user-supplied unless a separately consented provider is configured.')

# 21 — History / favorites
b=shell('History','History')
b+=txt(248,120,'Recently played · stored on this device',13,T['muted'])+button(1208,108,200,'Clear history','secondary','trash',38)
b+=pill(248,153,116,'Today','soft',32)+pill(374,153,132,'This week','ghost',32)+pill(516,153,116,'Favorites','ghost',32)
for i in range(8):
 b+=track_row(248,212+i*67,1160,i,current=False)
 b+=txt(1040,245+i*67,['09:41','09:36','09:31','Yesterday'][min(i,3)],11,T['dim'],mono=True)
b+=txt(248,807,'History is not the explicit queue. Clearing it does not remove files or favorites.',12,T['muted'])
b+=player_bar()
finish('21-history-favorites',b,1440,960,'History — local listening record','Local history with explicit clearing and separate favorites. No automatic scrobbling or cloud account implied.')

# 22 — Import progress
b=shell('Import music','Library')
b+=panel(248,168,1160,470,'Building your library','You can keep using the player while indexing runs')
b+=icon('folder',276,260,32,T['accent'])+txt(326,284,'/Music/Local collection',18,T['text'],600)+pill(1220,260,160,'Indexing','soft',30)
b+=rect(276,338,1104,10,T['bg'],5,T['line'])+rect(276,338,762,10,T['accent'],5)
b+=txt(276,382,'1,668 of 2,418 files indexed',16,T['text'],600)+txt(1380,382,'69%',16,T['accent'],650,anchor='end',mono=True)
for i,(n,v) in enumerate([('Audio ready','1,660 tracks'),('Needs review','8 files'),('Current folder','Northbound / Afterglow')]):
 b+=txt(276,447+i*43,n,13,T['muted'])+txt(1380,447+i*43,v,13,T['text'],mono=True,anchor='end')
b+=button(276,566,174,'Pause import','secondary','pause',40)+button(466,566,170,'Cancel import','ghost','close',40)+txt(1380,592,'No files are modified',12,T['muted'],anchor='end')
b+=panel(248,660,1160,150,'What happens next','Indexed tracks appear in Library; nothing plays automatically')
b+=txt(276,752,'Cancel stops indexing and keeps already indexed tracks. Remove a source folder later in Settings → Library.',12,T['muted'])
b+=player_bar()
finish('22-import-progress',b,1440,960,'Import — incremental progress and cancellation','Partial results remain usable, indexing is non-destructive, and cancel does not silently delete indexed tracks.')

# 23 — Desktop wireframe
T=MONO
b=shell('Now playing / structural wireframe','Now playing',status='Structural annotation',theme=MONO)
b+=rect(248,150,330,330,T['raised'],12,T['line'])+path('M248 150 L578 480 M578 150 L248 480',stroke=T['line'])+txt(413,325,'ALBUM ART',14,T['muted'],600,'middle')
b+=label(610,180,'TRACK IDENTITY')+rect(610,205,280,34,T['raised'],4)+rect(610,255,190,20,T['raised'],4)+rect(610,302,250,28,T['raised'],4)+rect(610,365,180,40,T['raised'],8)
b+=panel(930,150,478,330,'QUEUE REGION','Fixed meaning: explicit next + resume context')
for i in range(3): b+=rect(950,235+i*72,438,58,T['raised'],6)+txt(970,270+i*72,f'NEXT ITEM {i+1}',12,T['muted'],600)
b+=panel(248,510,1160,276,'SIGNAL REGION','Waveform / spectrum / static artwork; one active mode')
b+=rect(274,590,1108,110,T['raised'],6)+txt(828,651,'REACTIVE SVG LAYER',14,T['muted'],600,'middle')
b+=txt(248,818,'CONTENT SCROLLS INDEPENDENTLY; TRANSPORT DOES NOT',11,T['muted'],600)
b+=player_bar()
for n,x,y,tx,ty in [('1',110,165,20,115),('2',390,170,330,135),('3',1160,170,1090,135),('4',800,530,730,495),('5',600,885,530,845)]:
 b+=circle(x,y,12,T['accent'])+txt(x,y+4,n,11,T['ink'],700,'middle')+txt(tx,ty,{'1':'Persistent navigation','2':'Content adapts','3':'Queue stays explicit','4':'Visualization is pausable','5':'Transport is persistent'}[n],11,T['muted'])
finish('23-wireframe-desktop',b,1440,960,'Desktop structural wireframe','Regions and behavior before decoration: persistent navigation, adaptive content, explicit queue, pausable signal and persistent transport.', 'Wireframes & maps')
T=DARK

# 24 — Information architecture
b=board('Information architecture','One navigation model across skins. Advanced tools are reachable, never required for basic playback.',1400,940,MONO)
def node(x,y,w,h,title,sub='',accent=False):
 return rect(x,y,w,h,T['accent'] if accent else T['panel'],10,T['accent'] if accent else T['line'])+txt(x+w/2,y+29,title,15,T['ink'] if accent else T['text'],650,'middle')+txt(x+w/2,y+52,sub,11,T['ink'] if accent else T['muted'],anchor='middle')
b+=node(550,190,300,74,'PLAYER SHELL','Persistent transport + global search',True)
branches=[('LISTEN','Now playing\nQueue / Lyrics'),('ORGANIZE','Library / Playlists\nFavorites / History'),('SOUND','EQ / DSP / Output\nSleep timer'),('PERSONALIZE','Skins / Shortcuts\nAccessibility'),('MANAGE','Import / Tags\nPrivacy / Recovery')]
for i,(n,s) in enumerate(branches):
 x=40+i*274;b+=path(f'M700 264 V298 H{x+117} V326',stroke=T['line'],sw=2)+node(x,326,234,74,n,s.split('\n')[0],False)+txt(x+117,426,s.split('\n')[1],12,T['muted'],anchor='middle')
 for j in range(3):
  labels=[['Performance view','Mini / shade','Track details'],['Albums / tracks','Folders / artists','Radio / podcasts'],['Presets','Capabilities','Timer outcomes'],['Token editor','Skin import','Focus / motion'],['Source folders','Batch operations','Diagnostics']][i]
  b+=rect(x+10,465+j*62,214,46,T['panel'],8,T['line'])+txt(x+117,494+j*62,labels[j],12,T['text'],anchor='middle')
b+=panel(40,692,1320,184,'Cross-cutting rules')
for i,s in enumerate(['Queue, playlist context, selection and history are different data structures.','Search and shortcuts work from every primary view; Esc closes the top layer only.','Unsupported capabilities are hidden or explained, never shown as functional toggles.','Skin changes preserve labels, focus order, target sizes and state semantics.']): b+=txt(66,773+i*25,s,13,T['muted'])
finish('24-information-architecture',b,1400,940,'Information architecture and navigation contract','Five task groups with cross-cutting queue, search, accessibility and capability rules.', 'Wireframes & maps')

# 25 — Responsive wireframes
b=board('Responsive behavior','Breakpoints are content-driven; these are reference layouts, not device-specific assumptions.',1400,900,MONO)
for j,(x,w,name,desc) in enumerate([(40,650,'DESKTOP / ≥1200','Sidebar + content + queue'),(730,330,'MEDIUM / 900–1199','Labeled tabs + stacked regions'),(1100,260,'COMPACT / <900','Single column + bottom transport')]):
 b+=label(x,205,name)+txt(x,231,desc,12,T['muted'])
 b+=rect(x,255,w,510,T['shell'],12,T['line'])+rect(x+10,265,w-20,38,T['raised'],6)+txt(x+22,290,'HEADER / SEARCH',11,T['muted'],600)
 if j==0:
  b+=rect(x+10,315,120,380,T['raised'],6)+txt(x+70,500,'NAV',12,T['muted'],anchor='middle')+rect(x+145,315,230,170,T['raised'],6)+rect(x+390,315,248,170,T['raised'],6)+rect(x+145,500,493,195,T['raised'],6)+txt(x+390,603,'SIGNAL',12,T['muted'],anchor='middle')
 elif j==1:
  b+=rect(x+10,315,w-20,36,T['raised'],6)+txt(x+w/2,338,'LABELED TABS',11,T['muted'],anchor='middle')+rect(x+10,365,w-20,155,T['raised'],6)+rect(x+10,535,w-20,160,T['raised'],6)+txt(x+w/2,449,'TRACK + ART',12,T['muted'],anchor='middle')+txt(x+w/2,620,'SIGNAL / QUEUE TAB',12,T['muted'],anchor='middle')
 else:
  b+=rect(x+10,315,w-20,230,T['raised'],6)+txt(x+w/2,435,'ART / IDENTITY',12,T['muted'],anchor='middle')+rect(x+10,560,w-20,135,T['raised'],6)+txt(x+w/2,633,'SIGNAL + CONTROLS',11,T['muted'],anchor='middle')
 b+=rect(x+10,710,w-20,44,T['accent'],6)+txt(x+w/2,738,'PERSISTENT TRANSPORT',11,T['ink'],650,'middle')
b+=txt(40,824,'At 200% text size: allow vertical scrolling; never clip actions or require horizontal scrolling for core playback.',13,T['muted'])
finish('25-wireframe-responsive',b,1400,900,'Responsive structural wireframes','Desktop, medium and compact region behavior with persistent transport and content-driven reflow.', 'Wireframes & maps')

# 26 — User flow map
b=board('Critical task flows','Every flow has a start, a visible state change, a recovery path and a non-destructive exit.',1400,980,MONO)
flows=[('IMPORT','Choose folder','Index locally','Review issues','Library ready'),('PLAY','Choose track','Load / buffer','Play','Update all modes'),('QUEUE','Add next','Show position','Reorder / remove','Resume context'),('TAG EDIT','Select files','Show mixed values','Save explicitly','Confirm / recover'),('SKIN','Preview tokens','Validate contrast','Apply','Restore default')]
for i,row in enumerate(flows):
 y=205+i*137;b+=label(40,y+35,row[0])
 for j,s in enumerate(row[1:]):
  x=190+j*292;b+=rect(x,y,242,66,T['panel'],9,T['line'])+txt(x+121,y+39,s,13,T['text'],600,'middle')
  if j<3:b+=icon('chevron',x+251,y+23,20,T['accent'])
 b+=txt(190,y+94,['Permission denied → explain access; retry without rescanning everything.','Decode failure → preserve queue; locate / skip / copy diagnostics.','Empty queue → resume visible context; undo removal.','Write failure → keep edits in form; show file-specific reason.','Invalid skin → reject safely; keep current skin and focus order.'][i],12,T['muted'])
finish('26-user-flows',b,1400,980,'Critical flows and recovery exits','Import, playback, queue, metadata and skin flows with explicit failure recovery.', 'Wireframes & maps')

# 27 — State matrix
b=board('Playback and data states','The UI must distinguish loading, paused, stopped, buffering, unavailable and error.',1400,940,MONO)
cols=['STATE','TRANSPORT','SIGNAL','QUEUE / CONTEXT','RECOVERY']
widths=[190,245,245,330,310];x0=40
x=x0
for w,c in zip(widths,cols): b+=rect(x,194,w,44,T['raised'],0)+txt(x+14,222,c,11,T['muted'],650);x+=w
rows=[('Empty','Play disabled','Static placeholder','No context','Import / open files'),('Loading','Cancel / back','Static + progress','Target visible','Timeout → retry'),('Playing','Pause enabled','Live / pausable','Current marked','Pause / next'),('Paused','Play enabled','Frozen frame','Position retained','Resume'),('Buffering','Pause / skip','Last frame + label','Stream position honest','Retry / local track'),('Stopped','Play from start','Static artwork','Context retained','Choose track'),('Error','Play disabled*','No fake signal','Queue preserved','Locate / skip'),('Offline','Local enabled','Local only','Remote marked offline','Retry remote later')]
for i,row in enumerate(rows):
 x=x0;y=238+i*72
 for w,s in zip(widths,row):b+=rect(x,y,w,72,T['panel'] if i%2==0 else T['shell'],0,T['line'])+txt(x+14,y+31,s[:27],12,T['text'],550 if w==190 else 400)+(txt(x+14,y+51,s[27:],11,T['muted']) if len(s)>27 else '');x+=w
b+=txt(40,858,'* Error-state play may become “Retry” only when the same target can be reopened safely. Never animate a live signal without fresh audio data.',12,T['muted'])
finish('27-state-matrix',b,1400,940,'Playback state matrix','Visible behavior for empty, loading, playing, paused, buffering, stopped, error and offline states.', 'Wireframes & maps')

# 28 — Component buttons / controls
T=DARK
b=board('01 / Actions and selection','Reusable vector components. Hit areas are separate from visible pills; disabled actions explain why in implementation.',1400,1000)
b+=label(40,200,'BUTTONS / 40 PX HIGH')
for i,(n,k) in enumerate([('Primary','primary'),('Secondary','secondary'),('Quiet','ghost'),('Destructive','danger')]):b+=button(40+i*180,225,160,n,k,'plus' if i==0 else None)
b+=label(760,200,'ICON BUTTONS / 40–44 PX')
for i,n in enumerate(['play','heart','queue','more','expand']):b+=ib(n,760+i*64,218,44,active=i==0)
b+=label(1120,200,'STATES')
b+=button(1120,225,230,'Unavailable','secondary',disabled=True)
b+=label(40,320,'SEGMENTED CONTROL / TABS')
b+=rect(40,345,540,52,T['panel'],12,T['line'])
for i,n in enumerate(['Albums','Tracks','Artists']):b+=pill(50+i*174,353,164,n,'soft' if i==0 else 'ghost',36)
b+=label(620,320,'TOGGLE / SWITCH')
for i,(n,on) in enumerate([('Enabled',True),('Disabled',False),('Focus',True)]):
 x=620+i*220;b+=rect(x,353,48,26,T['accent'] if on else T['line'],13)+circle(x+35 if on else x+13,366,9,T['ink'] if on else T['text'])+txt(x+62,371,n,12,T['muted'])+(rect(x-5,348,58,36,'none',18,T['focus'],2) if i==2 else '')
b+=label(40,440,'CHECKBOX / RADIO / RATING')
for i,(n,on) in enumerate([('Unchecked',False),('Checked',True),('Mixed',True)]):
 x=40+i*190;b+=rect(x,470,22,22,T['accent'] if on else T['bg'],5,T['accent'] if on else T['line'])+(icon('check',x+3,473,16,T['ink']) if on and i==1 else line(x+5,481,x+17,481,T['ink'],2) if on else '')+txt(x+34,487,n,12,T['muted'])
for i in range(2):b+=circle(650+i*150,481,10,T['bg'],T['accent'],2)+(circle(650+i*150,481,5,T['accent']) if i else '')+txt(670+i*150,487,['Unselected','Selected'][i],12,T['muted'])
for i in range(5):b+=icon('star',1000+i*38,466,26,T['accent2'] if i<3 else T['dim'])
b+=label(40,560,'TEXT FIELDS / 46 PX HIGH')
for i,(n,s) in enumerate([('Default','Search your music'),('Focused','Northbound'),('Error','Enter a valid duration')]):
 x=40+i*440;b+=txt(x,594,n,12,T['muted'],600)+rect(x,610,400,46,T['panel'],9,T['danger'] if i==2 else T['focus'] if i==1 else T['line'],2 if i else 1)+txt(x+14,639,s,14,T['text'] if i else T['dim'])+txt(x,681,['Helper text stays outside the field.','2 px focus ring + caret; not color alone.','Message identifies the correction.'][i],11,T['danger'] if i==2 else T['muted'])
b+=label(40,740,'BADGES / STATUS')
for i,(n,k) in enumerate([('FLAC · 24/96','soft'),('Buffering','warn'),('Offline','neutral'),('Explicit','neutral'),('Queued · 2','soft')]):b+=pill(40+i*250,765,220,n,k,32)
b+=panel(40,844,1320,112,'Component rules')
b+=txt(64,901,'Minimum pointer target 24 px; design default 40 px desktop / 44 px touch. Focus ring is never removed.',13,T['muted'])+txt(64,929,'Labels remain visible for unfamiliar actions. Color is reinforced by text, icon, shape or position.',13,T['muted'])
finish('28-components-actions',b,1400,1000,'Component sheet — actions and selection','Buttons, icon buttons, segmented controls, switches, checkboxes, radios, ratings, fields and badges with state guidance.', 'Component sheets')

# 29 — Sliders / transport / waveform anatomy
b=board('02 / Continuous controls','Sliders expose values and keyboard steps. Waveform seeking is a separate action from visualization pause.',1400,1020)
b+=label(40,200,'TRANSPORT / SHARED ACROSS MODES')
b+=transport(40,235,1.2)+txt(430,270,'Shuffle · Previous · Play/Pause · Next · Repeat',13,T['muted'])+txt(430,296,'Repeat states: Off → All → One. Never use color alone.',12,T['muted'])
b+=label(40,365,'SEEK / 01:42 OF 04:26')
b+=wave(40,402,1320,100,.38)
b+=txt(40,535,'Drag to preview time; commit on release. Arrow = 5 s; Shift = 30 s. Live streams disable seeking.',12,T['muted'])
b+=label(40,600,'VOLUME / OUTPUT LEVEL')
b+=volume(40,641,360,.68)+txt(570,646,'Arrow = 1%; Page = 5%; Home/End = min/max. Mute is a separate toggle.',12,T['muted'])
b+=label(40,715,'EQ BAND / NUMERIC VALUE ALWAYS AVAILABLE')
b+=rect(40,745,640,180,T['panel'],12,T['line'])+line(90,835,630,835,T['line'],6)+line(90,835,360,835,T['accent'],6)+circle(360,835,12,T['text'])+txt(90,785,'−12 dB',12,T['muted'])+txt(630,785,'+12 dB',12,T['muted'],anchor='end')+txt(360,884,'+1.5 dB',16,T['accent'],600,'middle',mono=True)
b+=panel(720,745,640,180,'Signal controls')
b+=pill(744,812,130,'Waveform','soft',34)+pill(886,812,126,'Spectrum','ghost',34)+pill(1024,812,132,'Static art','ghost',34)+button(1170,810,166,'Pause visuals','secondary','pause',38)
b+=txt(40,974,'SVG is the presentation layer. Audio analysis supplies data; pausing visuals does not pause audio.',13,T['muted'])
finish('29-components-sliders',b,1400,1020,'Component sheet — transport and continuous controls','Seek, volume, EQ, repeat and visualization controls with keyboard steps and explicit semantics.', 'Component sheets')

# 30 — Rows / cards / queue items
b=board('03 / Music objects','Current playback, selected rows and queued items use different visual treatments.',1400,1000)
b+=label(40,200,'TRACK ROW / DEFAULT · CURRENT · SELECTED · DRAG TARGET')
for i,kind in enumerate(['default','current','selected','drop']):
 y=225+i*76;b+=track_row(40,y,850,i,current=kind=='current',selected=kind=='selected',checkbox=kind=='selected')
 if kind=='drop':b+=line(40,y-3,900,y-3,T['accent'],3)+pill(920,y+12,180,'Insert before track','soft',30)
 b+=pill(1120,y+12,220,kind.upper(),'neutral',30)
b+=label(40,570,'ALBUM CARD / HOVER REVEALS PLAY, NOT NAVIGATION')
b+=card(40,600,200,0)+ib('play',188,748,40,active=True)
b+=label(420,570,'QUEUE ITEM / HANDLE + REMOVE')
for i in range(2):b+=rect(420,600+i*100,480,84,T['panel'],10,T['line'])+icon('grip',436,630+i*100,20)+art(468,616+i*100,52,i,False)+txt(536,637+i*100,TRACKS[i+1][0],14,T['text'],600)+txt(536,660+i*100,'Northbound · explicit queue',11,T['muted'])+ib('close',848,622+i*100,40)
b+=panel(940,600,420,284,'Object semantics')
for i,s in enumerate(['Current: audio actually playing.','Selected: target for batch actions.','Queued: explicit future playback.','Context: playlist/folder after queue.','Favorite: independent metadata.','Drag: insertion line + live announcement.']):b+=txt(964,674+i*32,s,12,T['muted'])
b+=txt(40,954,'Long titles truncate visually but remain available in full via tooltip, details and accessible name. Never truncate the primary action label.',12,T['muted'])
finish('30-components-music-objects',b,1400,1000,'Component sheet — tracks, albums and queue items','Distinct current, selected, queued and drag-target states with non-destructive object semantics.', 'Component sheets')

# 31 — Menus / dialogs / feedback
b=board('04 / Overlays and feedback','One top layer at a time. Focus is trapped in modal dialogs; non-modal menus close predictably.',1400,1040)
b+=label(40,200,'CONTEXT MENU')
b+=rect(40,225,340,330,T['panel'],12,T['line'])
for i,(n,ic) in enumerate([('Play next','queue'),('Add to playlist','plus'),('Show album','grid'),('Edit metadata','edit'),('Remove from playlist','close')]):
 b+=rect(50,237+i*54,320,48,T['raised'] if i==0 else 'none',7)+icon(ic,64,251+i*54,20)+txt(98,267+i*54,n,13,T['text'])+txt(350,267+i*54,['Q','P','','E',''][i],11,T['dim'],anchor='end',mono=True)
b+=label(430,200,'INLINE ALERT / NON-DESTRUCTIVE')
b+=rect(430,225,930,94,T['panel'],10,T['line'])+icon('info',450,249,24,T['accent'])+txt(492,253,'3 tracks added to “Play next”',15,T['text'],600)+txt(492,280,'They will play before the current playlist resumes.',12,T['muted'])+button(1190,246,146,'Undo','secondary','repeat',38)
b+=rect(430,338,930,94,T['panel'],10,T['danger'])+icon('warning',450,362,24,T['danger'])+txt(492,366,'Could not save tags to 2 files',15,T['text'],600)+txt(492,393,'Your edits are still here. Review permissions and try again.',12,T['muted'])+button(1190,359,146,'Review','secondary','chevron',38)
b+=label(430,480,'TOAST / SHORT, DISMISSIBLE, NEVER THE ONLY ERROR RECORD')
b+=rect(430,505,930,58,T['raised'],10,T['line'])+icon('check',450,523,22,T['accent'])+txt(488,540,'Skin applied: Studio Dark',13,T['text'])+button(1190,515,146,'Undo skin','ghost','repeat',38)
b+=label(40,610,'MODAL / DESTRUCTIVE ACTION')
b+=rect(40,635,650,330,T['panel'],14,T['line'])+txt(66,678,'Remove 4 tracks from this playlist?',19,T['text'],600)+txt(66,715,'The audio files stay in your library and on disk.',13,T['muted'])+txt(66,742,'This changes the playlist, not the explicit queue.',13,T['muted'])+button(66,874,280,'Keep tracks','secondary',h=44)+button(362,874,300,'Remove from playlist','danger',h=44)
b+=panel(730,635,630,330,'Feedback timing')
for i,s in enumerate(['Success toast: 4 s; hover/focus pauses dismissal.','Undo queue removal: 8 s; persistent alternative in History.','Errors: remain until resolved or explicitly dismissed.','Progress: labeled, cancellable when cancellation is supported.','Screen reader: announce completion once, not every frame.','Reduced motion: no slide, bounce or pulsing notification.']):b+=txt(754,711+i*37,s,12,T['muted'])
finish('31-components-overlays',b,1400,1040,'Component sheet — menus, alerts, toasts and dialogs','Overlay hierarchy, destructive confirmation, undo and persistent error guidance.', 'Component sheets')

# 32 — Tokens / typography / spacing
b=board('Foundations / tokens and type','White-label values are semantic. Skin authors change tokens, not component anatomy or behavior.',1400,1020)
b+=label(40,200,'STUDIO DARK / SEMANTIC PALETTE')
keys=['bg','shell','panel','raised','line','text','muted','accent','accent2','danger']
for i,k in enumerate(keys):
 x=40+(i%5)*270;y=225+(i//5)*112;b+=rect(x,y,244,88,T['panel'],10,T['line'])+rect(x+12,y+12,42,42,DARK[k],8,T['line'])+txt(x+68,y+32,k,13,T['text'],600)+txt(x+68,y+56,DARK[k],11,T['muted'],mono=True)
b+=label(40,490,'TYPE SCALE / SYSTEM SANS + TABULAR NUMERALS')
for i,(n,s,sz) in enumerate([('Display',40,40),('Screen title',28,28),('Section',18,18),('Body',14,14),('Metadata',12,12),('Overline',11,11)]):
 x=40+(i%3)*450;y=535+(i//3)*105;b+=txt(x,y+30,n,sz,T['text'],650 if sz>18 else 500)+txt(x,y+58,f'{sz} px / {round(sz*1.35)} px line height',11,T['muted'],mono=True)
b+=label(40,760,'SPACING / 4 PX BASE')
for i,n in enumerate([4,8,12,16,24,32,48,64]):
 x=40+i*166;b+=rect(x,790,n,28,T['accent'],3)+txt(x,846,str(n),13,T['text'],mono=True)+txt(x,869,['Icon gap','Compact','Control','Panel','Section','Layout','Region','Hero'][i],11,T['muted'])
b+=panel(40,906,1320,80,'Contrast policy')
b+=txt(64,954,'Body text ≥4.5:1; meaningful controls and focus indicators ≥3:1. Validate every skin against its actual adjacent surfaces.',13,T['muted'])
finish('32-foundations-tokens',b,1400,1020,'Foundations — color, typography and spacing','Semantic dark tokens, readable type scale and 4 px spacing system. Light and high-contrast mappings are specified in the Markdown.', 'Foundations')

# 33 — Icon library
b=board('Icon system / editable SVG paths','24 px grid · 1.8 px stroke · round joins · 40/44 px interactive wrapper · no icon-only navigation',1400,1100)
for i,(n,d) in enumerate(ICONS.items()):
 x=40+(i%8)*170;y=205+(i//8)*116;b+=rect(x,y,146,96,T['panel'],10,T['line'])+icon(n,x+61,y+14,24,T['text'])+txt(x+73,y+70,n,11,T['muted'],anchor='middle')
b+=txt(40,1064,'All icons in this sheet are original path geometry. Names map to the reusable symbol contract in the implementation appendix.',12,T['muted'])
finish('33-icon-library',b,1400,1100,'Reusable icon library','Original 24 px stroke icons for playback, navigation, editing, status and skin controls.', 'Foundations')

# 34 — Waveform modes / signal design
b=board('Signal language / four visual modes','One signal source, multiple presentations. Decorative motion never masquerades as audio analysis.',1400,1080)
b+=panel(40,190,1320,206,'01  Mirrored waveform','Primary mode · time-domain envelope · played/unplayed distinction')
b+=wave(66,278,1268,76,.38,True)
b+=panel(40,416,640,252,'02  Spectrum','Log-spaced bands · peak caps · no fake stereo')
b+=spectrum(66,510,588,112,52)
b+=panel(700,416,660,252,'03  Oscilloscope','Time-domain trace · stable centerline · clipped samples flagged')
pts=[]
for i in range(240):
 x=728+i*2.5;y=562+math.sin(i*.16)*35*math.sin(i*.023)**2;pts.append(f'{x:.1f},{y:.1f}')
b+=line(728,562,1332,562,T['line'])+path('M'+' L'.join(pts),stroke=T['accent'],sw=2)
b+=panel(40,688,1320,220,'04  Static / reduced motion','Album art remains visible; signal updates can be paused or hidden without affecting audio')
b+=art(66,766,112,0,False)+txt(204,797,'Slow satellites',20,T['text'],600)+txt(204,826,'Northbound · static presentation',13,T['muted'])+pill(1110,780,220,'Visualization paused','neutral',34,'pause')
b+=txt(40,956,'Color + shape + labels distinguish modes. Peak meters are analysis measurements, not a promise about device output.',13,T['muted'])+txt(40,987,'Default: no flashing, no camera-like zoom, no continuous rotation. Full motion is an explicit preference.',13,T['muted'])
finish('34-waveform-modes',b,1400,1080,'Waveform and visualization modes','Mirrored bars, spectrum, oscilloscope and static reduced-motion presentation with honest signal semantics.', 'Signal & skins')

# 35 — Accessibility / focus and zoom
b=board('Accessibility / designed into every skin','Targets, focus, contrast and motion are skin invariants. Accessibility is not a separate “ugly mode”.',1400,1000)
b+=label(40,200,'FOCUS RING / 2 PX + 2 PX OFFSET')
for i,n in enumerate(['play','heart','queue','settings']):b+=rect(40+i*100,230,48,48,'none',12,T['focus'],2)+ib(n,44+i*100,234,40,active=i==0)
b+=label(500,200,'STATE IS NOT COLOR ALONE')
b+=pill(500,235,146,'Playing','soft',36,'wave')+pill(658,235,146,'Paused','neutral',36,'pause')+pill(816,235,166,'Buffering','warn',36,'clock')+pill(994,235,170,'Unavailable','neutral',36,'lock')
b+=panel(40,330,650,280,'Keyboard contract')
for i,s in enumerate(['Space: play/pause when not typing or on a button.','Left/Right: seek 5 s; Shift: 30 s.','Up/Down: volume 1% when transport has focus.','Tab: next control; Shift+Tab: previous.','Esc: close top overlay or leave focus view.','Alt+Up/Down: reorder focused queue item.']):b+=txt(64,405+i*32,s,12,T['muted'])
b+=panel(710,330,650,280,'Zoom and reflow')
for i,s in enumerate(['200% text: no clipped actions or overlapping labels.','320 CSS px equivalent: core playback remains usable.','400% browser zoom: verify equivalent reflow behavior.','Minimum target: 24 px; default: 40/44 px.','No horizontal scroll for core playback at compact width.','Respect OS reduced motion; offer an in-app override.']):b+=txt(734,405+i*32,s,12,T['muted'])
b+=label(40,660,'HIGH CONTRAST / SAME COMPONENTS')
hc=dict(DARK);hc.update(bg='#000000',shell='#000000',panel='#101010',raised='#202020',line='#BDBDBD',text='#FFFFFF',muted='#E0E0E0',dim='#C8C8C8',accent='#A8FFDA',accent2='#FFE0A3',ink='#000000')
old=T;T=hc
b+=rect(40,685,1320,230,T['bg'],12,T['line'])+art(64,709,132)+txt(220,742,'Slow satellites',26,T['text'],650)+txt(220,775,'Northbound · Afterglow',14,T['muted'])+transport(220,817,.8)+pill(600,730,166,'FLAC · 24/96','soft',32)+button(600,790,190,'Track details','secondary','info',40)+button(810,790,190,'Open queue','secondary','queue',40)+wave(1050,740,270,100,.38)
T=old
b+=txt(40,962,'SVG artwork is a design artifact. Production exposes native/HTML semantics, names, roles, values and live announcements.',12,T['muted'])
finish('35-accessibility-states',b,1400,1000,'Accessibility — focus, keyboard and high contrast','Focus rings, non-color state cues, keyboard behavior, zoom requirements and a high-contrast skin using the same components.', 'Foundations')

# 36 — Skin architecture / slot map
b=board('Skin contract / anatomy','Skins may change tokens, artwork and permitted layout variants. They may not change meanings or run code.',1400,960,MONO)
b+=rect(40,195,1320,600,T['shell'],14,T['line'])
slots=[('APP CHROME',60,215,1280,54),('NAVIGATION',60,285,200,420),('CONTENT',280,285,720,420),('QUEUE',1020,285,320,420),('TRANSPORT',60,725,1280,50)]
for n,x,y,w,h in slots:
 b+=rect(x,y,w,h,T['raised'],8,T['accent'],2)+txt(x+w/2,y+h/2+5,n,14,T['text'],650,'middle')
b+=label(40,840,'ALLOWED')
b+=txt(160,840,'Color · type scale · radius · texture · vector art · approved layout variant',13,T['muted'])
b+=label(40,884,'LOCKED')
b+=txt(160,884,'Control meaning · focus order · minimum targets · queue semantics · error honesty',13,T['muted'])
finish('36-skin-slot-map',b,1400,960,'Skin slot architecture','Tokenized chrome, navigation, content, queue and transport slots with locked behavioral and accessibility invariants.', 'Signal & skins')

# 37 — Component anatomy / measurements
b=board('Component anatomy / implementation dimensions','Visible geometry and interaction geometry are separate. All values are logical pixels at 100% scale.',1400,940,MONO)
b+=panel(40,195,650,310,'Primary button / 40 px')
b+=rect(100,285,260,40,T['accent'],9)+icon('plus',114,296,18,T['ink'])+txt(146,311,'Import music',13,T['ink'],600)
b+=line(100,346,360,346,T['muted'])+line(100,340,100,352,T['muted'])+line(360,340,360,352,T['muted'])+txt(230,372,'260 × 40 / radius 9',12,T['muted'],anchor='middle')
b+=line(385,285,385,325,T['muted'])+txt(405,311,'40',12,T['muted'])+txt(100,433,'Padding 14 · icon 18 · gap 10 · label 13/600',12,T['muted'])
b+=panel(710,195,650,310,'Track row / 56 px')
b+=track_row(740,282,590,0,current=True)
b+=txt(740,382,'Index 24 · gap 16 · title 13/600 · subtitle 11',12,T['muted'])+txt(740,414,'Duration right-aligned · overflow target 36–40',12,T['muted'])+txt(740,446,'Compact mode may use 48 px, never below 40 for touch.',12,T['muted'])
b+=panel(40,535,1320,320,'State layers / order from bottom to top')
for i,(n,s) in enumerate([('Surface','Panel / raised / shell token'),('State tint','Hover or selected fill; never obscures text'),('Content','Icon + label + value; stable geometry'),('Focus','2 px ring + 2 px offset; visible above tint'),('Drag / error','Insertion line or inline message; not color alone')]):
 y=617+i*43;b+=txt(66,y,n,13,T['text'],650)+txt(250,y,s,13,T['muted'])
finish('37-component-anatomy',b,1400,940,'Component measurements and state layers','Button and track-row dimensions plus surface, state, content, focus and error layer order.', 'Component sheets')

# 38 — Desktop compact breakpoint
T=DARK
b=board('Compact desktop / 720 px','Single-column content with a persistent transport. Queue becomes a labeled sheet, not an invisible sidebar.',820,1000)
b+=rect(50,180,720,760,T['shell'],16,T['line'])+logo(72,202,26)+pill(230,200,114,'Now playing','soft',32)+pill(356,200,92,'Library','ghost',32)+pill(460,200,86,'Queue','ghost',32)+ib('search',654,196,44)+ib('settings',704,196,44)
b+=art(74,266,228)+txt(330,300,'Slow satellites',27,T['text'],650)+txt(330,334,'Northbound · Afterglow',14,T['muted'])+pill(330,361,164,'FLAC · 24-bit / 96 kHz','soft',30)+button(330,414,154,'Track details','secondary','info',40)+ib('heart',500,414,40)
b+=panel(74,526,672,226,'Live waveform','Tap or click the signal to seek; pause is separate')+wave(98,614,624,78,.38)
b+=txt(74,790,'UP NEXT  ·  3 TRACKS',11,T['dim'],600)+button(590,766,156,'Open queue','ghost','queue',36)
b+=art(74,813,48,1,False)+txt(138,833,'Glass houses',13,T['text'],600)+txt(138,853,'Northbound',11,T['muted'])+txt(744,842,'3:51',12,T['muted'],anchor='end',mono=True)
b+=rect(50,874,720,66,T['panel'],0)+transport(220,884,.8)+ib('queue',480,887,40)+volume(548,908,100)
finish('38-compact-desktop',b,820,1000,'Compact desktop — 720 px','Single-column player with labeled navigation, waveform, queue preview and persistent transport.')

# 39 — Playlist manager / smart playlist
b=shell('Playlist builder','Playlists')
b+=txt(248,120,'Smart playlist · rules match against your local library',13,T['muted'])+button(1210,108,198,'Save playlist','primary','check',38)
b+=panel(248,168,1160,290,'Match rules','All conditions must be true')
for i,(a,op,v) in enumerate([('Genre','is any of','Ambient, electronic'),('Year','is between','2018–2024'),('Play count','is greater than','0')]):
 y=254+i*58;b+=button(272,y,210,a,'secondary','down',40)+button(498,y,220,op,'secondary','down',40)+rect(734,y,574,40,T['bg'],8,T['line'])+txt(750,y+25,v,13,T['text'])+ib('close',1330,y,40)
b+=button(272,414,166,'Add condition','ghost','plus',32)
b+=panel(248,480,1160,334,'Preview','18 tracks match · updates as rules change')
for i in range(4):b+=track_row(266,560+i*57,1124,i)
b+=player_bar()
finish('39-smart-playlist',b,1440,960,'Smart playlist builder','Readable condition rows, explicit all/any logic and live local-library preview. No remote recommendation dependency.')

# 40 — Privacy / library settings
b=shell('Settings','Library')
b+=pill(248,113,90,'Audio','ghost',32)+pill(348,113,104,'Library','soft',32)+pill(462,113,124,'Appearance','ghost',32)+pill(596,113,120,'Shortcuts','ghost',32)+pill(726,113,102,'Privacy','ghost',32)
b+=panel(248,170,1160,306,'Music sources','Only these folders are indexed')
for i,(n,s) in enumerate([('/Music/Local collection','2,418 tracks · available'),('/Volumes/Archive/Audio','Offline · drive disconnected')]):
 b+=icon('folder',274,258+i*94,26,T['accent'] if i==0 else T['accent2'])+txt(316,278+i*94,n,15,T['text'],600)+txt(316,302+i*94,s,12,T['muted'])+button(1200,252+i*94,180,'Remove source','ghost','close',38)
b+=button(272,420,184,'Add folder','secondary','plus',38)
b+=panel(248,498,566,314,'Local-first defaults')
for i,s in enumerate(['No account required for local playback.','No automatic cloud upload or remote metadata lookup.','History and favorites stay on this device by default.','Scrobbling and artwork providers are opt-in.','Diagnostics exclude file contents and private paths by default.']):b+=txt(272,580+i*43,s,12,T['muted'])
b+=panel(834,498,574,314,'Data controls')
b+=button(858,578,526,'Export library database','secondary','download',42)+button(858,636,526,'Export settings and skin tokens','secondary','download',42)+button(858,694,526,'Clear history and cached artwork','ghost','trash',42)+txt(858,773,'Audio files are never deleted by these actions.',11,T['muted'])
b+=player_bar()
finish('40-settings-library-privacy',b,1440,960,'Settings — sources, privacy and data control','Explicit indexed folders, local-first defaults, opt-in providers and non-destructive data export/clear actions.')

# 41 — Keyboard map
b=board('Keyboard map / predictable shortcuts','Shortcuts are scoped. Text fields keep normal editing keys; global OS shortcuts require separate permission.',1400,940,MONO)
rows=[('Space','Play / pause','Not while typing or activating a focused button'),('← / →','Seek ±5 s','Disabled for live streams'),('Shift + ← / →','Seek ±30 s','Clamp to track boundaries'),('↑ / ↓','Volume ±1%','When transport region is focused'),('M','Mute / unmute','Not while typing'),('Q','Add selection to queue','Announce count and undo'),('Alt + ↑ / ↓','Reorder queue item','Only when a queue item is focused'),('Ctrl / ⌘ + F','Search library','Focus search field'),('Ctrl / ⌘ + ,','Open settings','Preserve return focus'),('Esc','Close top layer','Then leave focus view; never quit app'),('F11 / host equivalent','Focus view','Host decides actual fullscreen shortcut'),('?','Open shortcut reference','Not while typing')]
for i,(k,a,s) in enumerate(rows):
 y=202+i*53;b+=rect(40,y,1320,48,T['panel'] if i%2==0 else T['shell'],6)+pill(54,y+8,210,k,'neutral',32)+txt(292,y+30,a,13,T['text'],600)+txt(650,y+30,s,12,T['muted'])
b+=txt(40,881,'All bindings are remappable. Conflict detection happens before save; “Restore defaults” is always available.',13,T['muted'])
finish('41-keyboard-map',b,1400,940,'Keyboard shortcut map','Scoped playback, search, queue and overlay shortcuts with conflict and text-entry rules.', 'Wireframes & maps')

# 42 — Component empty/loading/offline
b=board('05 / Empty, loading and unavailable','Every non-ideal state explains what happened, what remains usable and what to do next.',1400,940)
for i,(title,sub,action,ic) in enumerate([('No albums yet','Choose a folder to start your local library.','Choose folder','folder'),('Searching your library','1,204 of 2,418 tracks checked. Existing results stay usable.','Cancel search','search'),('This drive is offline','Reconnect it or keep playing available local tracks.','Retry connection','repeat')]):
 x=40+i*450;b+=panel(x,205,420,380,title,sub)
 b+=circle(x+210,355,52,T['raised'])+icon(ic,x+188,333,44,T['accent'] if i!=2 else T['accent2'])
 b+=txt(x+210,445,['Nothing is uploaded.','No playback interruption.','Your queue is preserved.'][i],13,T['muted'],anchor='middle')+button(x+40,505,340,action,'primary' if i==0 else 'secondary',ic,44)
b+=panel(40,625,1320,230,'State-specific rules')
for i,s in enumerate(['Empty: one primary action; no fake content or misleading counts.','Loading: preserve stale results with a timestamp; show progress only when measurable.','Offline: distinguish unavailable remote content from available local files.','Error: keep the recovery message persistent; a toast alone is insufficient.','Canceled: retain completed work; explain exactly what was kept.']):b+=txt(66,704+i*29,s,13,T['muted'])
finish('42-components-empty-loading',b,1400,940,'Component sheet — empty, loading and offline','Non-ideal states with one clear next action and honest preservation semantics.', 'Component sheets')

# 43 — Skin comparison / same screen four tokens
b=board('One anatomy, four signatures','Theme changes are token-level; the same controls and meanings survive every skin.',1400,1040)
for j,(name,th) in enumerate([('STUDIO DARK',DARK),('DAYLIGHT',LIGHT),('HIGH CONTRAST',{**DARK,'bg':'#000000','shell':'#000000','panel':'#101010','raised':'#202020','line':'#BDBDBD','text':'#FFFFFF','muted':'#E0E0E0','accent':'#A8FFDA','ink':'#000000'}),('CLASSIC METAL',{**DARK,'panel':'#303D47','raised':'#43525B','line':'#75848B','accent':'#F3C580','ink':'#252015'})]):
 x=40+(j%2)*680;y=195+(j//2)*390;old=T;T=th
 b+=rect(x,y,640,350,T['shell'],14,T['line'])+label(x+20,y+30,name)+art(x+20,y+54,136)+txt(x+176,y+86,'Slow satellites',21,T['text'],650)+txt(x+176,y+113,'Northbound',12,T['muted'])+pill(x+176,y+134,148,'FLAC · 24/96','soft',26)+transport(x+176,y+180,.65)+wave(x+20,y+260,600,48,.38)
 T=old
b+=txt(40,1008,'Classic Metal may add bevels and texture in production; it may not shrink targets, remove labels or change queue behavior.',12,T['muted'])
finish('43-skin-comparison',b,1400,1040,'Skin comparison — four semantic themes','Same player anatomy rendered with dark, light, high-contrast and classic token sets.', 'Signal & skins')

# 44 — Handoff / redlines
b=board('Handoff / flagship redlines','1440 × 960 reference canvas. Production uses logical pixels and reflows; it does not scale the entire desktop UI down.',1440,1000,MONO)
b+=rect(40,190,1360,700,T['shell'],12,T['line'])+rect(40,190,210,600,T['raised'],0)+rect(250,190,1150,64,T['panel'],0)+art(274,282,300)+rect(606,282,300,190,T['raised'],8)+rect(930,282,446,300,T['panel'],10,T['line'])+rect(274,610,1102,150,T['panel'],10,T['line'])+rect(40,790,1360,100,T['raised'],0)
for x1,y1,x2,y2,s,x,y in [(40,930,250,930,'224 nav',110,952),(274,594,574,594,'328 art',380,616),(250,270,1400,270,'24 px content gutter',760,263),(274,778,1376,778,'1102 signal width',760,798)]:
 b+=line(x1,y1,x2,y2,T['accent'],1.5)+txt(x,y,s,11,T['accent'],600,'middle')
b+=txt(40,978,'Desktop: 224 nav · 24 gutter · 328 art · 32 gap · fluid identity · 480 queue at 1440. At smaller widths, reflow per screen 17 / 25 / 38.',12,T['muted'])
finish('44-handoff-redlines',b,1440,1000,'Handoff — flagship layout redlines','Reference dimensions and reflow rules for implementation; not a fixed-scale screenshot contract.', 'Wireframes & maps')

print(f'Generated {len(ASSETS)} SVG assets')

# 45 — Navigation and header states
T=DARK
b=board('06 / Navigation and header','Navigation labels are persistent. Active, hover, focus and disabled are distinct states.',1400,920)
for i,(n,ic) in enumerate([('Now playing','play'),('Library','library'),('Playlists','list'),('Favorites','heart'),('History','clock')]):
 b+=label(40,205+i*112,n.upper())+nav_item(40,222+i*112,280,n,ic,active=i==0)
 b+=rect(360,222+i*112,280,42,T['raised'],9)+icon(ic,374,233+i*112,20)+txt(406,248+i*112,n,13,T['text'])
 b+=rect(680,222+i*112,280,42,T['panel'],9,T['focus'],2)+icon(ic,694,233+i*112,20)+txt(726,248+i*112,n,13,T['text'])
 b+=nav_item(1000,222+i*112,280,n,ic)
for x,n in [(40,'ACTIVE'),(360,'HOVER'),(680,'FOCUS'),(1000,'DEFAULT')]:b+=label(x,185,n)
b+=txt(40,858,'Disabled navigation is avoided for core destinations. Empty destinations open a useful empty state instead.',13,T['muted'])
finish('45-components-navigation',b,1400,920,'Component sheet — navigation states','Persistent labeled navigation with active, hover, focus and default treatments.', 'Component sheets')

# 46 — Shortcut settings
b=shell('Settings','Now playing')
b+=pill(248,113,90,'Audio','ghost',32)+pill(348,113,104,'Library','ghost',32)+pill(462,113,124,'Appearance','ghost',32)+pill(596,113,120,'Shortcuts','soft',32)+pill(726,113,102,'Privacy','ghost',32)
b+=rect(248,172,1160,48,T['bg'],9,T['line'])+icon('search',264,186,20)+txt(300,202,'Find a shortcut or command',13,T['dim'])+button(1190,177,218,'Restore defaults','ghost','repeat',38)
b+=panel(248,242,1160,570,'Keyboard shortcuts','Select a binding to record a replacement; conflicts are shown before saving')
for i,(a,k,scope) in enumerate([('Play / pause','Space','Playback'),('Seek forward','→','Playback'),('Search library','Ctrl / ⌘ + F','Global'),('Add to queue','Q','Selection'),('Open settings','Ctrl / ⌘ + ,','Global'),('Close top layer','Esc','Overlay')]):
 y=326+i*72;b+=txt(274,y+24,a,14,T['text'],550)+txt(274,y+46,scope,11,T['dim'])+pill(1030,y,220,k,'neutral',36,'keyboard')+ib('edit',1280,y-2,40)
 if i==0:b+=rect(1018,y-8,244,52,'none',12,T['focus'],2)
b+=rect(272,756,1112,36,T['bg'],6)+icon('info',284,764,18,T['accent2'])+txt(316,780,'System-wide media keys are managed by the host OS and are not remapped here.',12,T['muted'])
b+=player_bar()
finish('46-settings-shortcuts',b,1440,960,'Settings — remappable shortcuts','Scoped bindings, conflict-aware editing and restore defaults. OS media keys remain host-managed.')

# 47 — Output chooser
b=shell('Now playing','Now playing')
b+=rect(0,36,1440,924,'#07100F',extra='opacity=".72"')
b+=panel(420,164,600,608,'Output device','Choose where audio plays before the route changes')
for i,(n,s,ic) in enumerate([('MacBook Pro speakers','System default · available','monitor'),('Studio headphones','USB audio · available','headphones'),('Living room speaker','Network renderer · capability check required','radio')]):
 y=260+i*104;b+=rect(444,y,552,88,T['bg'],10,T['accent'] if i==0 else T['line'])+icon(ic,462,y+24,28,T['accent'] if i==0 else T['muted'])+txt(508,y+34,n,15,T['text'],600)+txt(508,y+59,s,11,T['muted'])+circle(964,y+44,9,T['accent'] if i==0 else 'none',T['line'],2)
b+=txt(444,610,'Changing devices may pause audio briefly.',13,T['muted'])+txt(444,637,'Exclusive mode is offered only after capability negotiation.',12,T['muted'])
b+=button(444,690,260,'Keep current device','secondary',h=44)+button(720,690,276,'Use selected device','primary','check',h=44)
b+=player_bar()
finish('47-output-device-dialog',b,1440,960,'Output routing — capability-aware chooser','Explicit device selection, availability and route-change warning. Network renderer support is not assumed.')

# 48 — Mobile sound studio
b=board('Mobile / sound studio','390 × 844 logical px · bands scroll horizontally as a group; primary actions remain fixed.',520,1030)
x=65;y=185
b+=rect(x,y,390,790,T['shell'],26,T['line'])+icon('back',x+20,y+58,24)+txt(x+62,y+80,'Sound studio',18,T['text'],650)+pill(x+28,y+112,112,'EQ enabled','soft',30)+button(x+218,y+108,144,'Reset all','ghost','repeat',36)
b+=txt(x+24,y+190,'Preset',12,T['muted'])+button(x+24,y+205,342,'Flat / reference','secondary','down',44)
b+=panel(x+16,y+274,358,292,'10-band equalizer','Swipe band area · numeric values stay visible')
for i,g in enumerate([0,2,3,1]):
 xx=x+62+i*82;cy=y+420-g*5;b+=line(xx,y+350,xx,y+490,T['line'],5)+rect(xx-12,cy-8,24,16,T['text'],4)+txt(xx,y+520,['31','62','125','250'][i],11,T['muted'],mono=True,anchor='middle')+txt(xx,y+542,f'{g:+d} dB',10,T['accent'],mono=True,anchor='middle')
b+=txt(x+195,y+590,'Bands 1–4 of 10  ·  swipe for more',11,T['muted'],anchor='middle')
b+=txt(x+24,y+634,'Preamp',13,T['text'])+txt(x+362,y+634,'−3.0 dB',13,T['accent'],mono=True,anchor='end')+line(x+24,y+658,x+366,y+658,T['line'],4)+circle(x+170,y+658,10,T['text'])
b+=button(x+24,y+700,342,'Save as preset','primary','check',44)
finish('48-mobile-equalizer',b,520,1030,'Mobile equalizer','Touch sound studio with horizontal band group, numeric values, preamp and fixed save action.')

# 49 — Mobile structural wireframes
b=board('Mobile / structural wireframes','Player, library and queue share a bottom transport or mini-player. No hidden core actions.',1290,1030,MONO)
for j,(name,kind) in enumerate([('PLAYER','now'),('LIBRARY','library'),('QUEUE','queue')]):
 x=40+j*420;y=185;b+=label(x,y-20,name)+rect(x,y,390,790,T['shell'],24,T['line'])+rect(x+16,y+50,358,48,T['raised'],8)+txt(x+195,y+80,'HEADER / BACK / SEARCH',11,T['muted'],600,'middle')
 if kind=='now':
  b+=rect(x+35,y+120,320,320,T['raised'],8)+txt(x+195,y+285,'ART',14,T['muted'],600,'middle')
  b+=rect(x+24,y+465,342,60,T['raised'],6)+rect(x+24,y+550,342,60,T['raised'],6)+rect(x+24,y+650,342,60,T['accent'],8)+txt(x+195,y+686,'TRANSPORT',12,T['ink'],650,'middle')
 elif kind=='library':
  b+=rect(x+24,y+120,342,54,T['raised'],6)+txt(x+195,y+153,'VIEW TABS',12,T['muted'],600,'middle')
  for i in range(4):b+=rect(x+24+(i%2)*180,y+205+(i//2)*220,162,190,T['raised'],8)
  b+=rect(x+16,y+704,358,68,T['accent'],12)+txt(x+195,y+744,'MINI PLAYER / EXPAND',12,T['ink'],650,'middle')
 else:
  for i in range(3):b+=rect(x+20,y+130+i*104,350,90,T['raised'],10)+txt(x+195,y+180+i*104,'QUEUE ITEM + HANDLE',12,T['muted'],600,'middle')
  b+=rect(x+24,y+470,342,90,T['raised'],8)+txt(x+195,y+520,'RESUME CONTEXT',12,T['muted'],600,'middle')+rect(x+24,y+650,342,48,T['raised'],8)+txt(x+195,y+680,'CLEAR QUEUE',12,T['muted'],600,'middle')
 b+=rect(x+142,y+773,106,4,T['dim'],2)
finish('49-mobile-wireframes',b,1290,1030,'Mobile structural wireframes','Region-level player, library and queue layouts before visual styling.', 'Wireframes & maps')

# 50 — Skin token editor
b=shell('Skin studio','Now playing')
b+=txt(248,120,'Edit semantic tokens. Validation runs before a skin can be applied.',13,T['muted'])+button(1210,108,198,'Validate & apply','primary','check',38)
b+=panel(248,166,566,646,'Token editor','Changes preview immediately; apply is explicit')
for i,(n,v) in enumerate([('surface.primary','#151C21'),('surface.panel','#1B242B'),('text.primary','#F3F7F6'),('text.secondary','#ADBDC5'),('accent.primary','#79E3C2'),('accent.on-primary','#10251F'),('focus.ring','#FFFFFF'),('radius.panel','12 px')]):
 y=252+i*60;b+=txt(272,y+22,n,12,T['muted'],mono=True)+rect(570,y,218,40,T['bg'],7,T['line'])+txt(584,y+25,v,12,T['text'],mono=True)
b+=pill(272,752,236,'Contrast checks pending','warn',32,'warning')
b+=panel(834,166,574,646,'Live preview','Studio Dark / modified')
b+=rect(858,246,526,330,T['bg'],12,T['line'])+art(880,268,160)+txt(1060,300,'Slow satellites',21,T['text'],650)+txt(1060,328,'Northbound',13,T['muted'])+wave(1060,365,290,66,.4)+transport(1060,465,.62)
b+=txt(858,625,'LOCKED INVARIANTS',11,T['dim'],650)+txt(858,657,'Control meanings · focus order · target sizes',12,T['muted'])+txt(858,684,'Queue semantics · error honesty · readable labels',12,T['muted'])+button(858,738,240,'Restore skin defaults','ghost','repeat',38)
b+=player_bar()
finish('50-skin-token-editor',b,1440,960,'Skin token editor and validation','Semantic token editing with live preview, explicit apply and locked accessibility/behavior invariants.')

(ROOT/'scripts'/'asset-manifest.json').write_text(json.dumps([{k:v for k,v in a.items() if k!='svg'} for a in ASSETS],indent=2))
print('Manifest:',len(ASSETS),'assets')
