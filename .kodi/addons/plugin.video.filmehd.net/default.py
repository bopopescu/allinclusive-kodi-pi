### ############################################################################################################
###	#	
### # Site: 				#		FilmeHD.net - http://www.filmehd.net
### # Author: 			#		The Highway
### # Description: 	#		
###	#	
### ############################################################################################################
### ############################################################################################################
### Imports ###
import xbmc
import os,sys,string,StringIO,logging,random,array,time,datetime,re
try: import copy
except: pass
import urllib,urllib2,xbmcaddon,xbmcplugin,xbmcgui
from common import *
from common import (_addon,_artIcon,_artFanart,_addonPath,_debugging,_SaveFile,_OpenFile)
### ############################################################################################################
### ############################################################################################################
SiteName='FilmeHD.net'
SiteTag='filmehd.net'
mainSite='http://filmehd.net'
mainSite2='http://www.filmehd.net'
iconSite=_artIcon #
fanartSite=_artFanart #
colors={'0':'white','1':'red','2':'blue','3':'green','4':'yellow','5':'orange','6':'lime','7':'','8':'cornflowerblue','9':'blueviolet','10':'hotpink','11':'pink','12':'tan','13':'firebrick','14':'mediumpurple'}

CR='[CR]'
MyAlphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#MyGenres=['Seriale','Animatie','Aventura','Biografic','Comedie','Dragoste','Drama','Familie','Fantezie','Filme-Vechi','Horror','Istoric','Mister','Muzica','Psihologic','Razboi','Romantic','Science-Fiction','Sport','Thriller','Western','Filme-Documentare-Online','Film-Noir','Filme-Indiene']
MyGenres=[['Filme-Vechi','Filme Vechi','Old Movies'],['Animatie','Animatie','Animation'],['Aventura','Aventura','Adventure'],['Biografic','Biografic','Biographical'],['Comedie','Comedie','Comedy'],['Dragoste','Dragoste','Love'],['Drama','Drama','Drama'],['Familie','Familie','Family'],['Fantezie','Fantezie','Fantasy'],['Horror','Horror','Horror'],['Istoric','Istoric','Historical'],['Mister','Mister','Mystery'],['Muzica','Muzica','Music'],['Psihologic','Psihologic','Psychological'],['Razboi','Razboi','War'],['Romantic','Romantic','Romance'],['Science-Fiction','Science Fiction','Sci-Fi'],['Sport','Sport','Sports'],['Thriller','Thriller','Thriller'],['Western','Western','Western'],['Filme-Documentare-Online','Filme Documentare Online','Documentary Film Online'],['Film-Noir','Film Noir','Film Noir'],['despre/filme-indiene','Filme Indiene','Indian Movies'],['despre/filme-nominalizate-la-oscar','Filme Nominalizate la Oscar','Nominated for Oscar'],['despre/filme-oscar','Filme Oscar','Oscar Movies'],['despre/nominalizari-globul-de-aur','Nominalizari Globul de Aur','Golden Globe Nominations'],['Seriale','Seriale','Series']]
MyYears=['2015','2014','2013','2012','2011','2010','2009','2008','2007','2006','2005','2004','2003','2002','2001','2000','1999','1998','1997','1996','1995','1994','1993','1992','1991','1990','1980','1970']
MyBrowser=['User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3']
ww6='[COLOR black]@[/COLOR]'; 
ww7='[COLOR FF0098BD]@[/COLOR]'; 
colorA='FF0098BD'; colorB='FF6E81BB'; 
workingUrl=mainSite+'ram.pls'
### ############################################################################################################
### ############################################################################################################
site=addpr('site','')
section=addpr('section','')
url=addpr('url','')
sections={'series':'series','movies':'movies'}
thumbnail=addpr('img','')
fanart=addpr('fanart','')
page=addpr('page','')
### ############################################################################################################
### ############################################################################################################
def About(head=''+cFL(SiteName,'blueviolet')+'',m=''):
	m=''
	if len(m)==0:
		m+='IRC Chat:  '+cFL('#The_Projects','blueviolet')+' @ '+cFL('irc.snoonet.org','blueviolet')
		m+=CR+'Site Name:  '+SiteName
		#m+=CR+'Site Tag:  '+SiteTag
		#m+=CR+'Site Domain:  '+mainSite+CR+'Site Icon:  '+iconSite+CR+'Site Fanart:  '+fanartSite
		m+=CR+'Age:  Please make sure you are of a valid age to watch the material shown.'
		m+=CR+CR+'Known Hosts for Videos:  '
		m+=CR+'* [embed.nowvideo.sx], [api.video.mail.ru], [vk.com]'
		m+=CR+CR+'Features:  '
		m+=CR+'* Browse Movies, Shows, Host Links'
		m+=CR+'* Play Videos with UrlResolver where available'
		m+=CR+'* Play Videos without UrlResolver where supported'
		m+=CR+'* MetaData for Shows and Movies where available'
		m+=CR+'* Favorites, AutoView'
		m+=CR+'* Core Player Selector'
		#m+=CR+'* Download Videos with UrlResolver'
		#m+=CR+'* '
		m+=CR+CR+'Notes:  '
		m+=CR+'* Thanks to: dotSmart Media Player, Eleazar, and TheHighway.'
		#m+=CR+'* '+ps('ReferalMsg')
		m+=CR+''
		m+=CR+''
		m+=CR+''
	try: DoA('Back'); 
	except: pass
	try: String2TextBox(message=cFL(m,'cornflowerblue'),HeaderMessage=head)
	except: pass
	#RefreshList()
def spAfterSplit(t,ss):
	if ss in t: t=t.split(ss)[1]
	return t
def spBeforeSplit(t,ss):
	if ss in t: t=t.split(ss)[0]
	return t
def FixImage(img):
	if 'http://' not in img: img=mainSite+img; 
	return img
def AFColoring(t): 
	if len(t)==0: return t
	elif len(t)==1: return cFL(t,colorA) #colorA)
	else: return cFL(cFL_(t,colorA),colorB) #colorA),colorB)
def RoAFColoring(t,t2): 
	if addst('mylanguage1','Romanian').lower()=='romanian': return AFColoring(t)
	else: return AFColoring(t2)
def wwA(t,ww): #for Watched State Display
	#if   ww==7: t=ww7+t
	#elif ww==6: t=ww6+t
	return t

### ############################################################################################################
### ############################################################################################################

def psgnR(x,t=".png"): ## Romanian
	s="http://i.imgur.com/"; 
	try:
		return {
			'search': 										ROartp('button_search')
			,'all': 											ROartp('button_all')
			,'about': 										ROartp('button_about')
			,'genre': 										ROartp('button_genres')
			,'year': 										ROartp('button_years')
			#,'latest': 										ROartp('button_latest')
			,'favorites': 								artp('button_favorites')
			,'favorites 1': 							artp('button_favorites')
			,'favorites 2': 							artp('button_favorites')
			,'favorites 3': 							artp('button_favorites')
			,'favorites 4': 							artp('button_favorites')
			,'favorites 5': 							artp('button_favorites')
			,'favorites 6': 							artp('button_favorites')
			,'favorites 7': 							artp('button_favorites')
			,'img_next':									artp('button_next')
			,'img_prev':									artp('button_prev')
		}[x]
	except: print 'failed to find graphc for %s' % (x); return ''

def psgn(x,t=".png"): ## English
	s="http://i.imgur.com/"; 
	if addst('mylanguage1','Romanian').lower()=='romanian': return psgnR(x,t)
	try:
		return {
			'search': 										artp('button_search')
			,'all': 											artp('button_all')
			,'about': 										artp('button_about')
			,'genre': 										artp('button_genres')
			,'year': 										artp('button_years')
			#,'latest': 										artp('button_latest')
			,'favorites': 								artp('button_favorites')
			,'favorites 1': 							artp('button_favorites')
			,'favorites 2': 							artp('button_favorites')
			,'favorites 3': 							artp('button_favorites')
			,'favorites 4': 							artp('button_favorites')
			,'favorites 5': 							artp('button_favorites')
			,'favorites 6': 							artp('button_favorites')
			,'favorites 7': 							artp('button_favorites')
			,'img_next':									artp('button_next')
			,'img_prev':									artp('button_prev')
#			,'': 								s+""+t
#			,'': 								s+""+t
#			,'': 								s+""+t
#			,'': 								s+""+t
		}[x]
	except: print 'failed to find graphc for %s' % (x); return ''
### ############################################################################################################
### ############################################################################################################
def PlayFromCHost(Url):
	if len(Url)==0: return
	if (mainSite not in Url) and (mainSite2 not in Url): Url=mainSite+Url; 
	deb('Url',Url); html=messupText(nolines(nURL(Url)),True,True); deb('length of html',str(len(html))); #debob(html); 
	#s='<center>\s*(Partea .*?)</center>\s*<iframe .*?src="(\D+://(.+?)/.+?)"'; 
	#try: results=re.compile(s).findall(html);
	
	
	return
	##

def GetMedia(Url,title,imdb_id,img,fimg,stitle,etitle,enumber,snumber,enumber2,wwT=''):
	if len(snumber)==0: snumber='0'; 
	if len(Url)==0: return
	if (mainSite not in Url) and (mainSite2 not in Url): Url=mainSite+Url; 
	###
	_addon.addon.setSetting(id="LastShowListedURL", value=Url)
	_addon.addon.setSetting(id="LastShowListedNAME", value=title)
	_addon.addon.setSetting(id="LastShowListedIMG", value=img)
	_addon.addon.setSetting(id="LastShowListedFANART", value=fimg)
	_addon.addon.setSetting(id="LastShowListedIMDBID", value=imdb_id)
	_addon.addon.setSetting(id="LastShowListedwwT", value=wwT)
	###
	deb('imdb_id',imdb_id); deb('title',title); deb('Url',Url); html=messupText(nolines(nURL(Url)),True,True); deb('length of html',str(len(html))); #debob(html); 
	if len(html)==0: return
	s="<script language='JavaScript' type='text/javascript' src='(/js_content.php.h=[0-9a-zA-Z]+)'></script>"; 
	try: content_url=re.compile(s).findall(html)[0]; 
	except: content_url=''; 
	if (mainSite not in content_url) and (mainSite2 not in content_url): content_url=mainSite+content_url; 
	deb('url for list of links',content_url); html=messupText(nolines(nURL(content_url)),True,True); deb('length of html',str(len(html))); #debob(html); 
	#html=html.replace("' ;","' \n\r;").replace("; var",";\n\r var").replace('</iframe>','</_iframe>\n\r</iframe_>').replace("='","= '</iframe_>")#.replace('</center><center>','</__center__><center>')
	#debob(html); 
	#s='<center>\s*([^<]+)</center>(?:<center>\s*(Partea [^<]+)</center>)?<.*?\s+src="(\D+://([^/]+)/[^"]+)"'; 
	s='(?:<center>\s*([^<]+)</center>)?<center>\s*([^<]+)</center><.*?\s+src="(\D+://([^/]+)/[^"]+)"'; 
	#try: rrRhtml2p1=re.compile(s,re.IGNORECASE).findall(html.replace('</center><','</center>\n\r<'));
	try: rrRhtml2p1=re.compile(s,re.IGNORECASE).findall(html.replace('><center> Server','>\n\r<center> Server'));
	#try: rrRhtml2p1=re.compile(s,re.IGNORECASE).findall(html);
	except: rrRhtml2p1=''
	debob(['rrRhtml2p1',rrRhtml2p1]); 
	iC1=len(rrRhtml2p1); 
	iC=len(rrRhtml2p1); 
	
#	s='</iframe_>.*?</_iframe>'; 
#	try: html2p1=re.compile(s,re.IGNORECASE).findall(html.replace("' ;","' \n\r;").replace("; var",";\n\r var").replace('</iframe>','</_iframe>\n\r</iframe_>').replace("='","= '</iframe_>"));
#	#try: html2p1=re.compile(s,re.IGNORECASE).findall(html);
#	except: html2p1=''
#	debob(['html2p1',html2p1]); 
#	iC1=len(html2p1); 
	if iC1 > 0:
				aSortMeth(xbmcplugin.SORT_METHOD_TITLE); 
				phtml2p=""; CentA=''; #html2p1=sorted(html2p1); 
#		aSortMeth(xbmcplugin.SORT_METHOD_TITLE); 
#		phtml2p=""; CentA=''; #html2p1=sorted(html2p1); 
#		for html2p in html2p1:
#			if phtml2p==html2p: next
#			
#			if '</center><center>' in html2p:
#				try: resultC=re.compile('<center>\s*([0-9a-zA-Z\s\-]+)\s*</center><center>',re.IGNORECASE).findall(html2p)[0];
#				except: resultC=''
#				if len(resultC) > 1: CentA=resultC+' - '; 
#			if '<center> Partea ' in html2p:
#				s='<center>\s*(Partea [^<]*)</center>\s*.*?src="(\D+://([^/]+)/[^"]+)"'; typ=0; 
#				#s='<center>\s*(Partea [^<]*)</center>\s*<iframe .*?src="(\D+://([^/]+)/[^"]+)"'; typ=0; 
#			else:
#				s='<center>\s*(Server [^<]*)</center>\s*.*?src="(\D+://([^/]+)/[^"]+)"'; typ=1; 
#				#s='<center>\s*(Server [^<]*)</center>\s*<iframe .*?src="(\D+://([^/]+)/[^"]+)"'; typ=1; 
#				##s='<center>\s*(.*?)</center><center>\s*(.*?)</center>\s*<iframe .*?src="(\D+://(.+?)/.+?)"'; typ=1; 
#			try: results=re.compile(s,re.IGNORECASE).findall(html2p);
#			except: results=''
#			iC=len(results)+iC1; 
#			if iC > 0:
#				debob(results); 
#				#results=sorted(results,key=lambda item: (item[0],item[2]),reverse=False)
				try: 
						URIed=True; 
						import urlresolver; 
						#importURLResolver()
						_plugin_path=xbmc.translatePath(os.path.join(_addonPath,'resources','lib','plugins'))
						urlresolver.plugnplay.plugin_dirs=[]
						urlresolver.plugnplay.set_plugin_dirs(urlresolver.common.plugins_path,_plugin_path)
						##urlresolver.plugnplay.set_plugin_dirs(_plugin_path,urlresolver.common.plugins_path,_plugin_path)
						##urlresolver.plugnplay.set_plugin_dirs(_plugin_path,urlresolver.common.plugins_path)
						urlresolver.plugnplay.load_plugins()
						##
						
				except: URIed=False
				for (name1,name2,url1,domain) in rrRhtml2p1:
#				for (name,url1,domain) in results:
					if len(name1) > 0: CentA=''+name1.strip()
					name=''+name2.strip()
					if len(CentA) > 0: name=' '+name
					if not url1.lower().startswith('http'): next
					name=name.replace('Partea a IIII-a','Partea IIII').replace('Partea a III-a','Partea III').replace('Partea a II-a','Partea II').replace('Partea I-a','Partea I'); 
					if not addst('mylanguage1','Romanian').lower()=='romanian': 
						name=name.replace('Partea I','Part I'); 
					if ' ~~ ' in wwT: wwT+=CentA+' - '+name
					else: wwT=title+' ~~ '+CentA+' - '+name
#					try: 
#						URIed=True; 
#						#import urlresolver; 
#						importURLResolver()
#					except: URIed=False
					TestUrlResolver=True; #TestUrlResolver=False; 
					if domain.lower() in ['bit.ly','7est.ro']:
						pass
					elif (domain in ['videomega.tv']) and (TestUrlResolver==False):
						debob({'domain':domain,'url':url1})
						if 'http://videomega.tv/cdn.php?ref=' in url1: url1=url1.replace('videomega.tv/cdn.php','videomega.tv/iframe.php')
						if 'http://videomega.tv/iframe.php?ref=' in url1:
							try:
								if '/cdn.' in url1: url1=url1.replace('/cdn.','/iframe.')
								ref_url=url1.replace('/iframe.php','/')
								if '&width=' in ref_url: ref_url=ref_url.split('&width=')[0]
								url1=url1.replace('/iframe.php','/cdn.php')
								headers={'Referer':ref_url}
								html_ref=nURL(ref_url,headers=headers); 
								html_cdn_js=nURL('http://videomega.tv/cdn.js',headers=headers)
								#print 'fetching:  '+'http://videomega.tv/cdn.js'; print html_cdn_js
								vmHtml=nURL(url1,headers=headers); 
								deb("len of html",str(len(vmHtml))); 
								eD=re.search('document.write\(unescape\("(.+?)"\)\)',vmHtml); 
								if eD:
									ueD=urllib.unquote_plus(eD.group(1))
									r=re.search(',\s*file\s*:\s*"(.+?)"\s*,',ueD)
									if r:
										stream_url=urllib.unquote_plus(r.group(1))
										#stream_url+="|Referer="+ref_url
										#stream_url+="|Referer="+urllib.quote_plus(ref_url)
										#stream_url+="|User-Agent="+urllib.quote_plus(MyBrowser[1])
										USER_AGENT='Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:30.0) Gecko/20100101 Firefox/30.0'
										#stream_url+="|User-Agent="+USER_AGENT
										print ['stream_url',stream_url]
										time.sleep(4)
										cMI=[]; labs={}; pars={'site':site,'mode':'PlayURL','url':stream_url,'title':title,'studio':CentA+''+name,'img':img,'fimg':fimg,'wwT':wwT,'imdb_id':imdb_id }
										labs['title']=''+CentA+''+name+' - '+domain+''; 
										try: _addon.add_directory(pars,labs,is_folder=False,contextmenu_items=cMI,total_items=iC,fanart=fimg,img=img)
										except: pass
									else: deb("videomega error","unable to find video url."); 
								else: deb("videomega error","unable to find escaped data."); 
							except Exception, e: debob(['error',e]); 
							except: pass
						else: deb("videomega error","impropper url."); 
					
					#elif domain in ['playreplay.net']:
					#		vId=url1.split('/')[-1]
					#		if '?' in vId: 
					#			try: vId=vId.split('?')[0]
					#			except: pass
					#		
					#		
					#		
					#		pass
					#elif domain in ['api.video.mail.ru']:
					elif domain.lower() in ['api.video.mail.ru','videoapi.my.mail.ru']:
						if (('://videoapi.my.mail.ru/videos/embed/gmail.com/' in url1.lower()) or ('://videoapi.my.mail.ru/videos/embed/list/' in url1.lower()) or ('://videoapi.my.mail.ru/videos/embed/mail/' in url1.lower())) and ('/_myvideo/' in url1.lower()):
							quality=str(addst("quality-api.video.mail.ru","HD")).upper(); 
							### 		http://api.video.mail.ru/videos/embed/gmail.com/clicksud.com/_myvideo/601
							### sd	http://api.video.mail.ru/file/video/v/gmail.com/clicksud.com/_myvideo/601
							### md http://api.video.mail.ru/file/video/hv/gmail.com/clicksud.com/_myvideo/601
							#if   quality=='HD': url1=url1.replace('.html','').replace('/videos/embed/gmail.com/','/file/video/hv/gmail.com/'); 		#HD
							#elif quality=='MD': url1=url1.replace('.html','').replace('/videos/embed/gmail.com/','/file/video/hv2/gmail.com/'); 	#MD
							#elif quality=='SD': url1=url1.replace('.html','').replace('/videos/embed/gmail.com/','/file/video/v/gmail.com/'); 		#SD
							cookyRu=art('cookies.mailru.txt')
							cookyRu2=art('cookies.mailru2.txt')
							url1=url1.replace('https://','http://')
							
							debob(['url1',url1])
							#_SaveFile(cookyRu,'#LWP-Cookies-2.0')
							##htmlMAILruE=messupText(nolines(nURL(url1,cookie_file=cookyRu,save_cookie=True)),True,True); 
							#htmlMAILruE,netRu=nURL(url1,cookie_file=cookyRu,save_cookie=True,ReturnObj=True); 
							#htmlMAILruE,netRu=nURL(url1,cookie_file=cookyRu,load_cookie=True,save_cookie=True,ReturnObj=True); 
							
							#htmlMAILruE=messupText(nolines(htmlMAILruE),True,True); 
							#deb('length of htmlMAILruE',str(len(htmlMAILruE))); #debob(htmlMAILru); 
							#CookiesMailRu=_OpenFile(cookyRu)
							#CookiesMailRu11=str(netRu.get_cookies())
							#debob(['CookiesMailRu11',CookiesMailRu11])
							
							url1=url1.replace('.html','.json').replace('/videos/embed/','/videos/')
							
							debob(['url1',url1])
							#_SaveFile(cooky,'')
							_SaveFile(cookyRu2,'#LWP-Cookies-2.0')
							#htmlMAILru=nURL(url1,cookie_file=cookyRu2,save_cookie=True)
							htmlMAILru,netRu2=nURL(url1,cookie_file=cookyRu2,save_cookie=True,ReturnObj=True)
							htmlMAILru,netRu2=nURL(url1,cookie_file=cookyRu2,load_cookie=True,save_cookie=True,ReturnObj=True)
							
							htmlMAILru=messupText(nolines(htmlMAILru),True,True); 
							deb('length of htmlMAILru',str(len(htmlMAILru))); #debob(htmlMAILru); 
							CookiesMailRu2=_OpenFile(cookyRu2)
							CookiesMailRu22=str(netRu2.get_cookies())
							debob(['CookiesMailRu22',CookiesMailRu22])
							
							try: 
								VideoKeyMailRu=str(re.compile("(?: name='video_key', value='| name=\"video_key\", value=\")([0-9A-Za-z]+)(?:'|\")").findall(CookiesMailRu22)[0])
							except: VideoKeyMailRu=''
							debob(['VideoKeyMailRu',VideoKeyMailRu])
							
							try: sourcesMailRu=re.compile('{"key":\s*"(\d+\D*)",\s*"url":\s*"(\D+://.*?)",\s*"seekSchema":\s*\d+}').findall(htmlMAILru)
							except: sourcesMailRu=[]
							if len(sourcesMailRu) > 0:
								for resMailRu,srcMailRu in sourcesMailRu:
										debob([resMailRu,srcMailRu])
										#srcMailRu+=' timeout=20'
										#srcMailRu+='|Cookie=%s'%(CookiesMailRu)
										if len(VideoKeyMailRu) > 0:
											#srcMailRu+='|Cookie=video_key%3D%s'%(urllib.quote_plus(VideoKeyMailRu))
											#srcMailRu+='|Cookie=video_key%3D%s'%(urllib.quote_plus(str(VideoKeyMailRu)))
											srcMailRu+='|Cookie=%s'%(urllib.quote_plus('video_key='+str(VideoKeyMailRu)))
											
										#srcMailRu+='|Cookie=%s'%('video_key%3Da57a3496b3c9aa76abfbafbe22955e1d76cb9e06')
										#srcMailRu+='|Cookie=%s'%(urllib.quote_plus(CookiesMailRu3))
										debob(['srcMailRu',srcMailRu])
										cMI=[]; labs={}; pars={'site':site,'mode':'PlayURL','url':srcMailRu,'title':title,'studio':CentA+''+name,'img':img,'fimg':fimg,'wwT':wwT,'imdb_id':imdb_id }
										#labs['title']=cFL(''+CentA+''+name+' - '+domain+' ['+quality+']','orange'); 
										labs['title']=''+CentA+''+name+' - '+domain+' ['+resMailRu+']'; 
										try: _addon.add_directory(pars,labs,is_folder=False,contextmenu_items=cMI,total_items=iC,fanart=fimg,img=img)
										except: pass
						elif 'http://api.video.mail.ru/videos/embed/mail/' in url1:
							quality=str(addst("quality-api.video.mail.ru","HD")).upper(); 
							if   quality=='HD': url1=url1.replace('.html','').replace('/videos/embed/mail/','/file/video/hv/mail/'); 		#HD
							elif quality=='MD': url1=url1.replace('.html','').replace('/videos/embed/mail/','/file/video/hv2/mail/'); 	#MD
							elif quality=='SD': url1=url1.replace('.html','').replace('/videos/embed/mail/','/file/video/v/mail/'); 		#SD
							cMI=[]; labs={}; pars={'site':site,'mode':'PlayURL','url':url1,'title':title,'studio':CentA+''+name,'img':img,'fimg':fimg,'wwT':wwT,'imdb_id':imdb_id }
							#labs['title']=cFL(''+CentA+''+name+' - '+domain+' ['+quality+']','orange'); 
							labs['title']=''+CentA+''+name+' - '+domain+' ['+quality+']'; 
							try: _addon.add_directory(pars,labs,is_folder=False,contextmenu_items=cMI,total_items=iC,fanart=fimg,img=img)
							except: pass
						elif ('http://api.video.mail.ru/videos/embed/mail/' in url1.lower()) or ('http://videoapi.my.mail.ru/videos/embed/mail/' in url1.lower()):
							quality=str(addst("quality-api.video.mail.ru","HD")).upper(); 
							if   quality=='HD': url1=url1.replace('.html','').replace('/videos/embed/mail/','/file/video/hv/mail/'); 		#HD
							elif quality=='MD': url1=url1.replace('.html','').replace('/videos/embed/mail/','/file/video/hv2/mail/'); 	#MD
							elif quality=='SD': url1=url1.replace('.html','').replace('/videos/embed/mail/','/file/video/v/mail/'); 		#SD
							cMI=[]; labs={}; pars={'site':site,'mode':'PlayURL','url':url1,'title':title,'studio':CentA+''+name,'img':img,'fimg':fimg,'wwT':wwT,'imdb_id':imdb_id }
							#labs['title']=cFL(''+CentA+''+name+' - '+domain+' ['+quality+']','orange'); 
							labs['title']=''+CentA+''+name+' - '+domain+' ['+quality+']'; 
							try: _addon.add_directory(pars,labs,is_folder=False,contextmenu_items=cMI,total_items=iC,fanart=fimg,img=img)
							except: pass
						elif ('http://api.video.mail.ru/videos/embed/gmail.com' in url1.lower()) or ('http://videoapi.my.mail.ru/videos/embed/gmail.com' in url1.lower()):
							quality=str(addst("quality-api.video.mail.ru","HD")).upper(); 
							## 		http://api.video.mail.ru/videos/embed/gmail.com/clicksud.com/_myvideo/601
							## sd	http://api.video.mail.ru/file/video/v/gmail.com/clicksud.com/_myvideo/601
							## md http://api.video.mail.ru/file/video/hv/gmail.com/clicksud.com/_myvideo/601
							if   quality=='HD': url1=url1.replace('.html','').replace('/videos/embed/gmail.com/','/file/video/hv/gmail.com/'); 		#HD
							elif quality=='MD': url1=url1.replace('.html','').replace('/videos/embed/gmail.com/','/file/video/hv2/gmail.com/'); 	#MD
							elif quality=='SD': url1=url1.replace('.html','').replace('/videos/embed/gmail.com/','/file/video/v/gmail.com/'); 		#SD
							cMI=[]; labs={}; pars={'site':site,'mode':'PlayURL','url':url1,'title':title,'studio':CentA+''+name,'img':img,'fimg':fimg,'wwT':wwT,'imdb_id':imdb_id }
							#labs['title']=cFL(''+CentA+''+name+' - '+domain+' ['+quality+']','orange'); 
							labs['title']=''+CentA+''+name+' - '+domain+' ['+quality+']'; 
							try: _addon.add_directory(pars,labs,is_folder=False,contextmenu_items=cMI,total_items=iC,fanart=fimg,img=img)
							except: pass
						else:
							cMI=[]; labs={}; pars={'site':site,'mode':'PlayURL','url':url1,'title':title,'studio':CentA+''+name,'img':img,'fimg':fimg,'wwT':wwT,'imdb_id':imdb_id }
							labs['title']=''+CentA+''+name+' - '+domain+' ['+'Not Supported'+']'; 
							try: _addon.add_directory(pars,labs,is_folder=False,contextmenu_items=cMI,total_items=iC,fanart=fimg,img=img)
							except: pass
					elif (tfalse(addst('internal-vk.com','false'))==True) and (domain.lower() in ['vk.com','vk.me']):
						#quality=str(addst("quality-vk.com","720")); 
						if (URIed==True) and (urlresolver.HostedMediaFile(url1).valid_url()): 
							cMI=[]; labs={}; pars={'mode':'PlayFromHost','url':url1,'title':title,'studio':CentA+''+name,'img':img,'fimg':fimg,'wwT':wwT,'imdb_id':imdb_id }
							#labs['title']=cFL(''+CentA+''+name+' - '+domain,'blue'); 
							labs['title']=''+CentA+''+name+' - '+domain+' [UrlResolver]'; 
							#Clabs={'title':title,'year':'','url':m,'destfile':destfile,'img':img,'fanart':fimg,'plot':'','todoparams':_addon.build_plugin_url(pars),'site':site,'section':section}; 
							#cMI=ContextMenu_Hosts(Clabs); 
							try: _addon.add_directory(pars,labs,is_folder=False,contextmenu_items=cMI,total_items=iC,fanart=fimg,img=img)
							except: pass
						if '&amp;' in url1: url1=url1.replace('&amp;','&')
						#if '&#038;' in url1: url1=url1.replace('&#038;','&')
						if 'http://' in url1: url1=url1.replace('http://','https://')
						#if 'https://' in url1: url1=url1.replace('https://','http://')
						htmlVK=messupText(nolines(nURL(url1)),True,True); deb('length of htmlVK',str(len(htmlVK))); #debob(htmlVK); 
						#s='url'+quality+'=(\D+://.+?)&'; #deb('s',s); 
						#s='&(\D+)(\d+)=(\D+://.+?)&'; #deb('s',s); 
						s='"(\D+)(\d+)"\s*:\s*"(\D+:.+?)"'; #deb('s',s); 
						htmlVK=htmlVK.replace('&amp;','&'); 
						htmlVK=htmlVK.replace('\\/','\/').replace('\/','/'); 
						#debob(htmlVK); 
						#try: rLink=re.compile(s).findall(htmlVK)[0];
						try: rLink=re.compile(s).findall(htmlVK);
						except: rLink=''
						if len(rLink) > 0:
							pLink=""; debob(rLink); 
							rLink=sorted(rLink,key=lambda item: (item[1],item[0]),reverse=False)
							rLink=sorted(rLink,key=lambda item: (item[0]),reverse=True)
							for rW,rQ,rL in rLink:
								if (rW in ['url','cache']) and (not pLink==rL):
									quality=rW+' '+rQ; 
									#if rL.startswith('https://'): rL=rL.replace('https://','http://')
									cMI=[]; labs={}; pars={'site':site,'mode':'PlayURL','url':rL,'title':title,'studio':CentA+''+name,'img':img,'fimg':fimg,'wwT':wwT,'imdb_id':imdb_id }
									#labs['title']=cFL(''+CentA+''+name+' - '+domain+' ['+quality+']','green'); 
									labs['title']=''+CentA+''+name+' - '+domain+' ['+quality+']'; 
									try: _addon.add_directory(pars,labs,is_folder=False,contextmenu_items=cMI,total_items=iC,fanart=fimg,img=img)
									except: pass
									pLink=""+rL
					elif (URIed==True) and (urlresolver.HostedMediaFile(url1).valid_url()): 
						#if '&amp;' in url1: url1=url1.replace('&amp;','&')
						cMI=[]; labs={}; pars={'mode':'PlayFromHost','url':url1,'title':title,'studio':CentA+''+name,'img':img,'fimg':fimg,'wwT':wwT,'imdb_id':imdb_id }
						#labs['title']=cFL(''+CentA+''+name+' - '+domain,'blue'); 
						labs['title']=''+CentA+''+name+' - '+domain; 
						#Clabs={'title':title,'year':'','url':m,'destfile':destfile,'img':img,'fanart':fimg,'plot':'','todoparams':_addon.build_plugin_url(pars),'site':site,'section':section}; 
						#cMI=ContextMenu_Hosts(Clabs); 
						try: _addon.add_directory(pars,labs,is_folder=False,contextmenu_items=cMI,total_items=iC,fanart=fimg,img=img)
						except: pass
					else:
						#cMI=[]; labs={}; pars={'site':site,'mode':'PlayFromCHost','url':url1,'title':title,'studio':CentA+''+name,'img':img,'fimg':fimg,'wwT':title+" ~~ "+name}
						##cMI=[]; labs={}; pars={'site':site,'mode':'PlayURL','url':url1,'title':title,'studio':name,'img':img,'fimg':fimg}
						#labs['title']=cFL(''+CentA+''+name+' - '+domain,'red'); 
						debob([name,url1,domain,'Host domain not currently supported.']); 
						#try: _addon.add_directory(pars,labs,is_folder=False,contextmenu_items=cMI,total_items=iC)
						#except: pass
#			phtml2p=""+html2p; 
	set_view('list',view_mode=addst('links-view')); eod()

def TagAnimeName(animename):
	#return animename
	try:
		return animename
	except: return animename

def ListShows(Url):
	if len(Url)==0: return
	if (mainSite not in Url) and (mainSite2 not in Url): Url=mainSite+Url; 
	deb('Url',Url); html=messupText(nolines(nURL(Url)),True,True); deb('length of html',str(len(html))); #debob(html); 
	#eod(); return
	if len(html)==0: return
	s ='<div id="post-\d+" class="[^"]+">\s*'; 
	s+='<h2 class="entry-title">\s*<a href="([^"]+)" title="([^"]+)" rel="bookmark">\s*'; 
	s+='<img style="height:188px;width:128px;" src="([^"]+)" alt="[^"]+" />\s*</a>\s*</h2>\s*'; 
	s+='<h2 class="entry-title">\s*<a href="[^"]+" title="\s*[^"]+" rel="bookmark">[^<]+</a>\s*</h2>\s*'; 
	s+='</div'; 
	##s+='</div><!-- #post-## --'; 
	#if mainSite+'/?s=' in Url: s='<div class="span3" style="width:\d+px;margin-left:1%;margin-bottom:10px;"><div class="item"><a href="http://www.justanimestream.net/anime-series/gantz-ii-perfect-answer/" data-toggle="tooltip" data-placement="right" data-original-title="Gantz II: Perfect Answer"><figure><img src="/bimages/gantz-ii-perfect-answer.jpg" class="animethumbs" alt="Gantz II: Perfect Answer" width="125px" height="190px"/><div class="overlay"><i class="icon-play"></i></div></figure><article><h5>(.+?)</h5></article></a></div></div>'; 
	### url,img,name
	try: matches=re.compile(s).findall(html.replace('</div><div id="post-','</div>\n<div id="post-')); deb('# of matches found',str(len(matches))); #debob(matches)
	except: matches=''; 
	if len(matches) > 0:
		iC=len(matches); enMeta=tfalse(addst("enableMeta","false")); 
		if "' class='previouspostslink'>" in html:
			try: PrEVIOUS= html.split("' class='previouspostslink'>")[0].split("<a href='")[-1]; #re.compile("<a href='(.+?)' class='previouspostslink'>").findall(html)[0]; 
			except: PrEVIOUS=Url; 
			deb('previous',PrEVIOUS); _addon.add_directory({'mode':'ListShows','url':PrEVIOUS,'site':site,'section':section},{'title':cFL('<< Previous','green')+'  '+PrEVIOUS.replace(mainSite,'').replace(mainSite2,'')},is_folder=True,fanart=fanartSite,img=psgn('img_prev'))
		elif '<a class="previouspostslink" href="' in html:
			try: PrEVIOUS= html.split('<a class="previouspostslink" href="')[-1].split('">')[0]; #re.compile("<a href='(.+?)' class='previouspostslink'>").findall(html)[0]; 
			except: PrEVIOUS=Url; 
			deb('previous',PrEVIOUS); _addon.add_directory({'mode':'ListShows','url':PrEVIOUS,'site':site,'section':section},{'title':cFL('<< Previous','green')+'  '+PrEVIOUS.replace(mainSite,'').replace(mainSite2,'')},is_folder=True,fanart=fanartSite,img=psgn('img_prev'))
		elif '<a class="previouspostslink" rel="prev" href="' in html:
			try: PrEVIOUS= html.split('<a class="previouspostslink" rel="prev" href="')[-1].split('"')[0]; #re.compile("<a href='(.+?)' class='previouspostslink'>").findall(html)[0]; 
			except: PrEVIOUS=Url; 
			deb('previous',PrEVIOUS); _addon.add_directory({'mode':'ListShows','url':PrEVIOUS,'site':site,'section':section},{'title':cFL('<< Previous','green')+'  '+PrEVIOUS.replace(mainSite,'').replace(mainSite2,'')},is_folder=True,fanart=fanartSite,img=psgn('img_prev'))
		#
		if enMeta==True:
			try: from metahandler import metahandlers; grab=metahandlers.MetaData(preparezip=False); 
			except: debob("filed to import metahandler"); 
		for (url,name,img) in matches: #for (url,img,name) in matches:
			name1=''+name; 
			if 'filme online' in name: TyP='movie'
			elif 'Serial TV' in name: TyP='tv'
			else: TyP='movie'
			name=name.replace(') - filme online',')').replace(') Serial TV - ',') - ')
			name2=""+name; 
			if '(' in name2: 
				try: Year=name2.split('(')[1].split(')')[0]
				except: Year=''
				name2=name2.split('(')[0]
			else:
				Year=''
			if ' - ' in name2: name2=name2.split(' - ')[0]
			img=FixImage(img); cMI=[]; img=img.replace(' ','%20'); fimg=fanartSite; deb('img',img); Genres2=""; g="<a href='http://www.animefate.com/.genre=.+?'>\s*(.+?)\s*</a>"; plot=""; labs={}; 
			genres=""; 
			#try: Genres1=re.compile(g).findall(genres); debob(Genres1); 
			#except: Genres1=""; 
			#for g in Genres1: Genres2+="["+g+"] "; 
			#Genres2=str(Genres1); 
			wwT=name+" ~~ "; 
			#wwT=name2+" ~~ "; 
			try:
				if visited_check(wwT)==True: ww=7
				#if visited_check2(wwT)==True: ww=7
				else: ww=6
			except: ww=6
			if enMeta==True: 
				if 'filme online' in name1:
					#try: labs=grab.get_meta('movie',TagAnimeName(name2),overlay=ww); debob(labs); 
					try: labs=grab.get_meta('movie',TagAnimeName(name2)); debob(labs); 
					except: pass
				else:
					#try: labs=grab.get_meta('tvshow',TagAnimeName(name2),overlay=ww); debob(labs); 
					try: labs=grab.get_meta('tvshow',TagAnimeName(name2)); debob(labs); 
					except: pass
				try:
					if len(labs[u'cover_url']) > 0: img=labs[u'cover_url']; 
				except: pass
				try:
					if len(labs[u'backdrop_url']) > 0: fimg=labs[u'backdrop_url']; 
				except:
					try:
						if len(labs['backdrop_url']) > 0: fimg=labs['backdrop_url']; 
					except: pass
			else: labs[u'plot']=''; labs[u'imdb_id']=''; labs[u'title']=''+name; labs[u'year']=''; 
			try:
				if len(labs['imdb_id'])==0: labs[u'imdb_id']=''
			except: labs[u'imdb_id']=''
			#plot+=CR+"Genres:  [COLOR purple]"+Genres2+"[/COLOR]"; #plot+="[CR]Year: [COLOR purple]"+year+"[/COLOR]"; #plot+="[CR]Status: [COLOR purple]"+status+"[/COLOR]"; #plot+="[CR]Number of Episodes: [COLOR purple]"+NoEps+"[/COLOR]"; 
			#pars={'mode':'ListEpisodes','url':url,'title':name,'imdb_id':labs[u'imdb_id'],'img':img,'fimg':fimg,'site':site,'section':section}; 
			pars={'mode':'GetMedia','url':url,'title':name,'imdb_id':labs[u'imdb_id'],'img':img,'fimg':fimg,'site':site,'section':section,'wwT':wwT}; 
			labs[u'plot']=plot+CR+cFL(labs[u'plot'],'mediumpurple'); labs[u'title']=AFColoring(name); 
			#Clabs=labs; 
			labs[u'title']=wwA(labs[u'title'],ww); 
			Clabs={'title':name,'year':labs[u'year'],'url':url,'commonid':labs[u'imdb_id'],'img':img,'fanart':fimg,'plot':labs[u'plot'],'todoparams':_addon.build_plugin_url(pars),'site':site,'section':section}; 
			try: cMI=ContextMenu_Series(Clabs,TyP); 
			except: pass
			try: _addon.add_directory(pars,labs,is_folder=True,fanart=fimg,img=img,contextmenu_items=cMI,total_items=iC,context_replace=True)
			except: pass
		#debob(html); 
		if ('<a href="' in html) and ('">Vezi toate filmele online de pe site ></a>' in html):
			try: NeXT=html.split('">Vezi toate filmele online de pe site ></a>')[0].split("<a href='")[-1]; #re.compile("</span><a href='("+mainSite+"/.+?/)' class='nextpostslink'>").findall(html)[0]; 
			except: NeXT=Url; 
			deb('next',NeXT); _addon.add_directory({'mode':'ListShows','url':NeXT,'site':site,'section':section},{'title':cFL('>> Next','green')+'  '+NeXT.replace(mainSite,'').replace(mainSite2,'')},is_folder=True,fanart=fanartSite,img=psgn('img_next'))
		elif "' class='nextpostslink'>" in html:
			try: NeXT=html.split("' class='nextpostslink'>")[0].split("<a href='")[-1]; #re.compile("</span><a href='("+mainSite+"/.+?/)' class='nextpostslink'>").findall(html)[0]; 
			except: NeXT=Url; 
			deb('next',NeXT); _addon.add_directory({'mode':'ListShows','url':NeXT,'site':site,'section':section},{'title':cFL('>> Next','green')+'  '+NeXT.replace(mainSite,'').replace(mainSite2,'')},is_folder=True,fanart=fanartSite,img=psgn('img_next'))
		elif '<a class="nextpostslink" href="' in html:
			try: NeXT=html.split('<a class="nextpostslink" href="')[-1].split('">')[0]; #re.compile("</span><a href='("+mainSite+"/.+?/)' class='nextpostslink'>").findall(html)[0]; 
			except: NeXT=Url; 
			deb('next',NeXT); _addon.add_directory({'mode':'ListShows','url':NeXT,'site':site,'section':section},{'title':cFL('>> Next','green')+'  '+NeXT.replace(mainSite,'').replace(mainSite2,'')},is_folder=True,fanart=fanartSite,img=psgn('img_next'))
		elif '<a class="nextpostslink" rel="next" href="' in html:
			try: NeXT=html.split('<a class="nextpostslink" rel="next" href="')[-1].split('"')[0]; #re.compile("</span><a href='("+mainSite+"/.+?/)' class='nextpostslink'>").findall(html)[0]; 
			except: NeXT=Url; 
			deb('next',NeXT); _addon.add_directory({'mode':'ListShows','url':NeXT,'site':site,'section':section},{'title':cFL('>> Next','green')+'  '+NeXT.replace(mainSite,'').replace(mainSite2,'')},is_folder=True,fanart=fanartSite,img=psgn('img_next'))
		if "' class='last'>Ultima " in html:
			try: LaST=html.split("' class='last'>Ultima ")[0].split("<a href='")[-1]; #re.compile("<a href='("+mainSite+"/.+?/)' class='last'>Last ").findall(html)[0]; 
			except: LaST=Url; 
			deb('last',LaST); _addon.add_directory({'mode':'ListShows','url':LaST,'site':site,'section':section},{'title':cFL('>> >> Last','green')+'  '+LaST.replace(mainSite,'').replace(mainSite2,'')},is_folder=True,fanart=fanartSite,img=psgn('img_next'))
		elif '<a class="last" href="' in html:
			try: LaST=html.split('<a class="last" href="')[-1].split('">')[0]; #re.compile("<a href='("+mainSite+"/.+?/)' class='last'>Last ").findall(html)[0]; 
			except: LaST=Url; 
			deb('last',LaST); _addon.add_directory({'mode':'ListShows','url':LaST,'site':site,'section':section},{'title':cFL('>> >> Last','green')+'  '+LaST.replace(mainSite,'').replace(mainSite2,'')},is_folder=True,fanart=fanartSite,img=psgn('img_next'))
	set_view('tvshows',view_mode=addst('tvshows-view')); eod()

def Fav_List(site='',section='',subfav=''):
	debob(['test1',site,section,subfav]); 
	favs=fav__COMMON__list_fetcher(site=site,section=section,subfav=subfav); 
	ItemCount=len(favs); 
	debob('test2 - '+str(ItemCount)); 
	if len(favs)==0: myNote('Favorites','None Found'); eod(); return
	favs=sorted(favs,key=lambda item: (item[0],item[1]),reverse=False); 
	debob(favs); 
	for (_name,_year,_img,_fanart,_Country,_Url,_plot,_Genres,_site,_subfav,_section,_ToDoParams,_commonID,_commonID2) in favs:
		debob([_name,_year,_img,_fanart,_Country,_Url,_plot,_Genres,_site,_subfav,_section,_ToDoParams,_commonID,_commonID2]); 
		if _img > 0: img=_img
		else: img=iconSite
		if _fanart > 0: fimg=_fanart
		else: fimg=fanartSite
		debob('_ToDoParams'); debob(_ToDoParams)
		pars=_addon.parse_query(_ToDoParams)
		pars[u'fimg']=_fanart; pars[u'img']=_img; 
		#if len(_commonID) > 0: pars['imdb_id']=_commonID
		try:
			if len(pars['imdb_id']) > 0: pars['imdb_id']='0'; 
		except: pars['imdb_id']='0'; 
		debob('pars'); debob(pars)
		_title=AFColoring(_name)
		if (len(_year) > 0) and (not _year=='0000'): _title+=cFL('  ('+cFL(_year,'mediumpurple')+')',colorA)
		if len(_Country) > 0: _title+=cFL('  ['+cFL(_Country,'mediumpurple')+']',colorA)
		wwT=_name+" ~~ "; 
		try:
			if visited_check2(wwT)==True: ww=7
			else: ww=6
		except: ww=6
		contextLabs={'title':_name,'year':_year,'img':_img,'fanart':_fanart,'country':_Country,'url':_Url,'plot':_plot,'genres':_Genres,'site':_site,'subfav':_subfav,'section':_section,'todoparams':_ToDoParams,'commonid':_commonID,'commonid2':_commonID2}
		##contextLabs={'title':_name,'year':'0000','url':_url,'img':img,'fanart':fimg,'DateAdded':'','todoparams':_addon.build_plugin_url(pars),'site':site,'section':section}
		contextMenuItems=ContextMenu_Favorites(contextLabs)
		contextMenuItems.append( ('Empty List','XBMC.RunPlugin(%s)' % _addon.build_plugin_url({'mode':'cFavoritesEmpty','site':site,'section':section,'subfav':subfav}) ) )
		#contextMenuItems=[]
		_title=wwA(_title,ww); 
		_addon.add_directory(pars,{'title':_title,'plot':_plot},is_folder=True,fanart=fimg,img=img,total_items=ItemCount,contextmenu_items=contextMenuItems)
		#
	#
	if 'movie' in section.lower(): content='movies'
	else: content='tvshows'
	set_view(content,view_mode=int(addst('tvshows-view'))); eod()


### ############################################################################################################
### ############################################################################################################
def MenuAZ(url):
	#_addon.add_directory({'mode':'ListShows','url':url+'/','site':site,'section':section},{'title':AFColoring('ALL')},is_folder=True,fanart=fanartSite,img=psgn('all')); 
	_addon.add_directory({'mode':'ListShows','url':url+'/0/','site':site,'section':section},{'title':AFColoring('#')},is_folder=True,fanart=fanartSite,img=psgn('0')); 
	for az in MyAlphabet:
		az=az.upper(); _addon.add_directory({'mode':'ListShows','url':url+'/'+az.lower()+'/','site':site,'section':section},{'title':AFColoring(az)},is_folder=True,fanart=fanartSite,img=psgn(az.lower())); 
	set_view('list',view_mode=addst('default-view')); eod()

def DoSearch(title='',Url='/?s='):
	if len(Url)==0: return
	if mainSite not in Url: Url=mainSite+Url; 
	if len(title)==0: title=showkeyboard(txtMessage=title,txtHeader="Search:  ("+site+")")
	if (title=='') or (title=='none') or (title==None) or (title==False): return
	deb('Searching for',title); title=title.replace('+','%2B').replace('&','%26').replace('?','%3F').replace(':','%3A').replace(',','%2C').replace('/','%2F').replace('=','%3D').replace('@','%40').replace(' ','+'); 
	deb('Searching for',title); ListShows( Url+( title.replace(' ','+') ) ); 

def MenuGenre():
	for aL,azRo,azEn in MyGenres: 
		if addst('mylanguage1','Romanian').lower()=='romanian': az=azRo
		else: az=azEn
		i=psgn(az.lower())
		if len(i)==0: i=iconSite
		_addon.add_directory({'mode':'ListShows','url':'/'+aL.lower().replace(' ','-')+'/','site':site,'section':section},{'title':AFColoring(az)},is_folder=True,fanart=fanartSite,img=i); 
	set_view('list',view_mode=addst('list-view')); eod()

def MenuYear():
	for az in MyYears: 
		i=psgn(az.lower())
		if len(i)==0: i=iconSite
		_addon.add_directory({'mode':'ListShows','url':'/despre/filme-'+az.lower().replace(' ','-')+'/','site':site,'section':section},{'title':AFColoring(az)},is_folder=True,fanart=fanartSite,img=i); 
	set_view('list',view_mode=addst('list-view')); eod()
def SectionMenu():
	#addstv('firstrun','') ## To reset first-run value for testing ##
	if len(addst('firstrun',''))==0: 
		L=popYN(title='FilmeHD.net',line1='                                          Selectarea limbii',line2='                                       Language Selection',line3='',n='English',y='Romanian'); #deb("L",str(L)); 
		if str(L)=='1': addstv('mylanguage1','Romanian'); 
		else: addstv('mylanguage1','English'); 
		addstv('firstrun','no'); 
	#_addon.add_directory({'mode':'GetMedia','site':site,'url':'/tremors-4-the-legend-begins-tremors-4-inceputul-legendei-2004-filme-online.html'},{'title':AFColoring('Testing')},is_folder=True,fanart=fanartSite,img=iconSite)
	_addon.add_directory({'mode':'ListShows','site':site,'url':'/page/1'},{'title':RoAFColoring('Toate','ALL')},is_folder=True,fanart=fanartSite,img=psgn('all')) #iconSite)
	_addon.add_directory({'mode':'MenuGenre','site':site},{'title':RoAFColoring('Categorie','Genres')},is_folder=True,fanart=fanartSite,img=psgn('genre'))
	_addon.add_directory({'mode':'MenuYear','site':site},{'title':RoAFColoring('Ani','Years')},is_folder=True,fanart=fanartSite,img=psgn('year'))
	_addon.add_directory({'mode':'Search','site':site,'url':'/?s='},{'title':RoAFColoring('Cautare','Search')},is_folder=True,fanart=fanartSite,img=psgn('search'))
	
	_addon.add_directory({'mode':'FavoritesList','site':site,'section':section             },{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL('Filme - Movies',colorB)},fanart=fanartSite,img=psgn('favorites 1'))
	_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'2'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL('Seriale - TV Shows',colorB)},fanart=fanartSite,img=psgn('favorites 2'))
	
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section             },{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.1.name'),colorB)},fanart=fanartSite,img=psgn('favorites 1'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'2'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.2.name'),colorB)},fanart=fanartSite,img=psgn('favorites 2'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'3'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.3.name'),colorB)},fanart=fanartSite,img=psgn('favorites 3'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'4'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.4.name'),colorB)},fanart=fanartSite,img=psgn('favorites 4'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'5'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.5.name'),colorB)},fanart=fanartSite,img=psgn('favorites 5'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'6'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.6.name'),colorB)},fanart=fanartSite,img=psgn('favorites 6'))
	#_addon.add_directory({'mode':'FavoritesList','site':site,'section':section,'subfav':'7'},{'title':cFL(ps('WhatRFavsCalled'),colorA)+cFL(addst('fav.tv.7.name'),colorB)},fanart=fanartSite,img=psgn('favorites 7'))
	###
	if (len(addst("LastShowListedURL")) > 0): 
		pars={'site':site,'section':section,'mode':'GetMedia','url':addst("LastShowListedURL"),'title':addst("LastShowListedNAME"),'imdb_id':addst("LastShowListedIMDBID"),'img':addst("LastShowListedIMG"),'fimg':addst("LastShowListedFANART"),'wwT':addst("LastShowListedwwT")}; 
		title=AFColoring(addst("LastShowListedNAME"))+CR+cFL('[Last Show]',colorA); 
		_addon.add_directory(pars,{'title':title},fanart=addst("LastShowListedFANART"),img=addst("LastShowListedIMG"),is_folder=True); 
	#if (len(addst("LastEpisodeListedURL")) > 0): 
	#	pars={'site':site,'section':section,'mode':'GetMedia','url':addst("LastEpisodeListedURL"),'title':addst("LastEpisodeListedNAME"),'imdb_id':addst("LastEpisodeListedIMDBID"),'img':addst("LastEpisodeListedIMG"),'fimg':addst("LastEpisodeListedFANART"),'stitle':addst("LastEpisodeListedSTITLE"),'etitle':addst("LastEpisodeListedETITLE"),'e':addst("LastEpisodeListedEpNo"),'s':addst("LastEpisodeListedSNo"),'e2':addst("LastEpisodeListedEpNo2")}; 
	#	title=AFColoring(addst("LastEpisodeListedNAME"))+CR+cFL('[Last Episode]',colorA); 
	#	_addon.add_directory(pars,{'title':title},fanart=addst("LastEpisodeListedFANART"),img=addst("LastEpisodeListedIMG"),is_folder=True); 
	###
	_addon.add_directory({'mode':'About','site':site,'section':section},{'title':RoAFColoring('Despre','About')},is_folder=True,fanart=fanartSite,img=psgn('about')) #'http://i.imgur.com/0h78x5V.png') # iconSite
	###
	set_view('list',view_mode=addst('default-view')); eod()
### ############################################################################################################
### ############################################################################################################
def mode_subcheck(mode='',site='',section='',url=''):
	deb('mode',mode); 
	if (mode=='SectionMenu'): 		SectionMenu()
	elif (mode=='') or (mode=='main') or (mode=='MainMenu'): SectionMenu()
	elif (mode=='SubMenu'): 			SubMenu()
	elif (mode=='ListShows'): 		ListShows(url)
	elif (mode=='GetMedia'): 			GetMedia(url,addpr('title',''),addpr('imdb_id',''),addpr('img',''),addpr('fimg',''),addpr('stitle',''),addpr('etitle',''),addpr('e',''),addpr('s',''),addpr('e2',''),addpr('wwT',''))
	elif (mode=='Search'):				DoSearch(addpr('title',''),url)
	#elif (mode=='Hosts'): 				Browse_Hosts(url)
	#elif (mode=='Search'): 			Search_Site(title=addpr('title',''),url=url,page=page,metamethod=addpr('metamethod','')) #(site,section)
	#elif (mode=='SearchLast'): 	Search_Site(title=addst('LastSearchTitle'+SiteTag),url=url,page=page,metamethod=addpr('metamethod',''),endit=tfalse(addpr('endit','true'))) #(site,section)
	elif (mode=='About'): 				eod(); About()
	#elif (mode=='FavoritesList'): Fav_List(site=site,section=section,subfav=addpr('subfav',''))
	elif (mode=='MenuAZ'): 				MenuAZ(url)
	elif (mode=='MenuGenre'): 		MenuGenre()
	elif (mode=='MenuYear'): 		MenuYear()
	elif (mode=='FavoritesList'): Fav_List(site=site,section=section,subfav=addpr('subfav',''))
	elif (mode=='PlayFromCHost'): 			PlayFromCHost(url)
	elif (mode=='PlayURL'): 						PlayURL(url)
	elif (mode=='PlayURLs'): 						PlayURLs(url)
	elif (mode=='PlayURLstrm'): 				PlayURLstrm(url)
	elif (mode=='PlayFromHost'): 				PlayFromHost(url)
	elif (mode=='PlayFromHostMT'): 			PlayFromHostMT(url)
	elif (mode=='PlayVideo'): 					PlayVideo(url)
	elif (mode=='PlayItCustom'): 				PlayItCustom(url,addpr('streamurl',''),addpr('img',''),addpr('title',''))
	elif (mode=='PlayItCustomL2A'): 		PlayItCustomL2A(url,addpr('streamurl',''),addpr('img',''),addpr('title',''))
	elif (mode=='Settings'): 						_addon.addon.openSettings() # Another method: _plugin.openSettings() ## Settings for this addon.
	elif (mode=='ResolverSettings'): 		import urlresolver; urlresolver.display_settings()  ## Settings for UrlResolver script.module.
	elif (mode=='ResolverUpdateHostFiles'):	import urlresolver; urlresolver.display_settings()  ## Settings for UrlResolver script.module.
	elif (mode=='TextBoxFile'): 				TextBox2().load_file(url,addpr('title','')); #eod()
	elif (mode=='TextBoxUrl'):  				TextBox2().load_url(url,addpr('title','')); #eod()
	elif (mode=='Download'): 						
		try: _addon.resolve_url(url)
		except: pass
		debob([url,addpr('destfile',''),addpr('destpath',''),str(tfalse(addpr('useResolver','true')))])
		DownloadThis(url,addpr('destfile',''),addpr('destpath',''),tfalse(addpr('useResolver','true')))
	elif (mode=='toJDownloader'): 			SendTo_JDownloader(url,tfalse(addpr('useResolver','true')))
	elif (mode=='cFavoritesEmpty'):  	fav__COMMON__empty( site=site,section=section,subfav=addpr('subfav','') ); xbmc.executebuiltin("XBMC.Container.Refresh"); 
	elif (mode=='cFavoritesRemove'):  fav__COMMON__remove( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year','') )
	elif (mode=='cFavoritesAdd'):  		fav__COMMON__add( site=site,section=section,subfav=addpr('subfav',''),name=addpr('title',''),year=addpr('year',''),img=addpr('img',''),fanart=addpr('fanart',''),plot=addpr('plot',''),commonID=addpr('commonID',''),commonID2=addpr('commonID2',''),ToDoParams=addpr('todoparams',''),Country=addpr('country',''),Genres=addpr('genres',''),Url=url ) #,=addpr('',''),=addpr('','')
	elif (mode=='AddVisit'):							
		try: visited_add(addpr('title')); RefreshList(); 
		except: pass
	elif (mode=='RemoveVisit'):							
		try: visited_remove(addpr('title')); RefreshList(); 
		except: pass
	elif (mode=='EmptyVisit'):						
		try: visited_empty(); RefreshList(); 
		except: pass
	elif (mode=='refresh_meta'):			refresh_meta(addpr('video_type',''),TagAnimeName(addpr('title','')),addpr('imdb_id',''),addpr('alt_id',''),addpr('year',''))
	else: myNote(header='Site:  "'+site+'"',msg=mode+' (mode) not found.'); import mMain
mode_subcheck(addpr('mode',''),addpr('site',''),addpr('section',''),addpr('url',''))
### ############################################################################################################
### ############################################################################################################
