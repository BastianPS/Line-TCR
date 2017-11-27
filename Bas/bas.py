# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from googletrans import Translator
import time,random,sys,json,codecs,threading,glob,re,datetime,subprocess,urllib3,os,requests,urllib,urllib2,wikipedia
import ast,re
import tempfile

satpam = LINETCR.LINE() # Koplaxs # Login Pake Akun Utama Kalian(Gunanya Supaya Akun Utama Ke Kick bisa Terima Undangan dari Bot Otomatis)
satpam.login(token="EmEa5lfF1USDQqukESf0.N3vAvt5fxLmSAbiNsyQ74a.4UUi6aTkNj3aXUrugk7Z2gbdSF3jKDQ9+3O/driZwS0=")
satpam.loginResult()

cl = LINETCR.LINE() #Luffy
cl.login(token="EnnyiqxYAGirLAh285z9.ZZzFJv6fobaG1M6zazPt6q.PBXOHf1pVw1UtgLjNKbWhr+HkIuVDrk+TPZVKG2nous=")
cl.loginResult()

ki = LINETCR.LINE() #Zorro
ki.login(token="Emv23safaGZzg03Llef6.Bo5VT5hIMzEPG1zBCPvfXG.MQ5Yhp01qgUMtSy+x03xJNerJYynypQC3vUKjpHWynY=")
ki.loginResult()

kk = LINETCR.LINE() #Sanji
kk.login(token="Em7dkfKhyCBe4T2BINg3.R6RMrIgS09xT2jSr2ctQqW.GEKHkqvimMRr+J/Kgs/iTgXJTTnWaQYHlvit9WkbhX0=")
kk.loginResult()

kc = LINETCR.LINE() #Ussop
kc.login(token="EmkJhDAxO33we1nK4uC8.WLFfwfa6DQYY+Ms1W6byQa.6YwgdGiKOe9zfmJZgQ0LVUemTJr6UutUbkrG8hHaBhk=")
kc.loginResult()

ks = LINETCR.LINE() #Chooper
ks.login(token="EmGpaheZovq8v9c3sEBe.ojsBOB8CFcMcdA48KSnhJG.MkefvQVuy+KSO5UFTF8aheEAzGzX5QsbAwiTpGTrgE4=")
ks.loginResult()

ka = LINETCR.LINE() #Franky
ka.login(token="Em7VYM593wfX0Q3ikPMf.HvoLsvcX69JYmPwB7DU/hW.nm3Zalkd/tVizQ9sXQbzeL2DLVaYK98dvOcoYxet4fA=")
ka.loginResult()

kb = LINETCR.LINE() #Brook
kb.login(token="EmOV0UDWnEuLBR4fnh78.4YgtBnqYLI66dq4+AJkHMa.VL/N/Uf47WxHND5u842SW+rEsNpO+k6c54Hy0/SSbn4=")
kb.loginResult()

ko = LINETCR.LINE() #Nami
ko.login(token="EmSlPXeAsRNXtUUlBRy6.+TTUQTkgndLSz6GtkvU6zG.g1I2on9C5XEL91AVWpCEjES2swOa+iKsrRy0paM8iKk=")
ko.loginResult()

ke = LINETCR.LINE() #Robin
ke.login(token="EmXmuyMBtqpcxLEFPTC1.2b+G/MamoMUtzasQEUSI8q.+ic2iw/hDPLkAA3ke9RudzWHowPTb4sTgEuvERe6FHU=")
ke.loginResult()

ku = LINETCR.LINE() # Jinbei
ku.login(token="EmTqh3qtzJi4dhZDdn1f.6o96YHdRW52PEP0xga0BxW.Aw6Iqkwl0LoaJpYnKFtp/rlKPewsUArbdREG8nGHM8Y=")
ku.loginResult()

k1 = LINETCR.LINE() #Backup (Gunanya Kalo Akun Utama Ke Kick, Dy masuk ke Group dan Ngekick yang Kick Akun Utama Dan Akun Utama Di undang sama dia,lalu dy leave lagi :D)
k1.login(token="Em5KZ4bgqghIpPPjRT08.J7+basj57IigdSYxzMWm/a.aa/04j3x00E1DkpUSqXbzlTkDyC2AJFVcc1u73YgBsY=")
k1.loginResult()

print "login success plak"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" ∆_∆|T͢E͢A͢M͢ B͢O͢T͢ T͢E͢A͢M͢ |∆_∆
=============================
!New Command!
=> Youtube: = Search yt
=> Music = mendengar + mendownload music
=> .say = Suara Mbah Google
=============================

=============================
!Command Members!
=> Creator = Melihat Pembuat Bot
=> Crott = Tag Semua orang
=> Gcreator = Check Creator Grup
=> Lihat = Set Sider
=> Ciduk loh = Lihat Sider
=============================

=============================
!Command Creator!
=> Admin add @ = Menambahkan Admin
=> Admin remove @ = Menghapus Admin
=> Adminlist = Cek Admin
=============================

=============================
!Command Admin!
=> Id = Menampilkan Id Bot
=> Mid = Menampilkan Mid Bot
=> Mid @ = Menampilkan Mid By Tag
=> Me = Menampilkan Kontak Bot
=> Contact on/off = On/Off Menampilkan mid
=> Join on/off = On/Off Masuk Grup
=> Leave on/off = Auto Leave
=> Add on/off = Auto Add
=> Share on/off = Auto Share
=> Jam on/off = On/Off Jam(rusak)
=> Up = Memperbaharui Jam (rusak)
=> Gurl = Menyalakan Url Grup
=> Ginfo = Menampilkan Info Grup
=> Cancel = Membatalkan Undangan DiGrup
=> Gn = Mengganti Nama Grup
=> Kuy = Invite semua Bot
=> Kaboor = Keluar Dari Grup
=> Invite = Invite Menggunakan Mid
=> Cn = Ganti Nama
=> Gift = Memberi Hadiah
=> Respon = Merespon Bot
=> random: = Spam Nama Grup
=> LG = Cek Semua Grup
=> Getpp @ = Mengambil Gambar Dp Target
=> Getcover = Mengambil Gambar Sampul Target
=============================

=============================
!Command Mimic!
=> Mimic On/Off = menghidupkan/mematikan mimic
=> Mimic:add: @ = Ngetag Mana Yang Mau Jadi Target
=============================

=============================
!CommandPenting!
=> Cancel On/Off = AutoKick Bagi Yang Invite Member
=> Qr On/Off = AutoKick Bagi Yang Membuka QR
=> Banned @ = Ban Menggunakan Tag
=> Unban @ = Unban Menggunakan Tag
=> Ban = Ban Menggunakan Contact
=> Unban = Unban Mengunakan Contact
=> Kill Ban = Kill Yang DiBan
=> Kill @ = Kill Yang Di Tag
=> Nk @ = Mengeluarkan Anggota Dari Grup
=> Salam = Membersihkan Grup
=> Admin menu = Hanya admin saja yg boleh tau
=============================
ṡȗƿƿȏяṭєԀ ɞʏ:
DraBas
Hanya Admin Yang Bisa Menggunakan Bot Sepenuhnya
OWNER •✓DraBas•"""

Setgroup =""" 
    [Admin Menu]
==============
||[Protect QR]
||- Qr on/off
||[Protect Join]
||- Join on/off
||[Mid Via Contact]
||- Contact on/off
||-[Cancel Invited]
||- Cancel all
==============
 F̳͉̼͉̙͔͈͕̂̉̇e̮̟͈̣̖̰̩̹͈̾ͨ̑͑l͕͖͉̭̰ͬ̍ͤ͆̊ͨe̮̟͈̣̖̰̩̹͈̾ͨ̑͑r̼̯̤̗̲̞̥̈ͭ̃ͨ̆ T̘̟̼̉̈́͐͋͌̊e̮̟͈̣̖̰̩̹͈̾ͨ̑͑a̘̫͈̭͌͛͌̇̇̍m̘͈̺̪͓̺ͩ͂̾ͪ̀̋ B͎̣̫͈̥̗͒͌̃͑̔̾ͅo̜̓̇ͫ̉͊ͨt̉̈́
=============="""
KAC=[cl,ki,kk,kc,ks,ka,kb,ko,ke,ku]
DEF1=[ki,kk,kc,ks,ka,kb,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF2=[cl,kk,kc,ks,ka,kb,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF3=[cl,ki,kc,ks,ka,kb,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF4=[cl,ki,kk,ks,ka,kb,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF5=[cl,ki,kk,kc,ka,kb,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF6=[cl,ki,kk,kc,ks,kb,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF7=[cl,ki,kk,kc,ks,ka,ko,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF8=[cl,ki,kk,kc,ks,ka,kb,ke,ku] #Udah Ga Kepake(Boleh di apus)
DEF9=[cl,ki,kk,kc,ks,ka,kb,ko,ku] #Udah Ga Kepake(Boleh di apus)
DEF10=[cl,ki,kk,kc,ks,ka,kb,ko,ke] #Udah Ga Kepake(Boleh di apus)
mid = cl.getProfile().mid #Luffy
Amid = ki.getProfile().mid #Zorro
Bmid = kk.getProfile().mid #Sanji
Cmid = kc.getProfile().mid #Ussop
Dmid = ks.getProfile().mid #Chooper
Emid = ka.getProfile().mid #Franky
Fmid = kb.getProfile().mid #Brook
Gmid = ko.getProfile().mid #Nami
Hmid = ke.getProfile().mid #Robin
Imid = ku.getProfile().mid #Jinbei
Smid = satpam.getProfile().mid #Akun Utama
mid1 = k1.getProfile().mid #Backup

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Smid,mid1,"u9f755a553e455e532c681227498abbe0"]
admin=["u9f755a553e455e532c681227498abbe0"] 
owner=["u9f755a553e455e532c681227498abbe0"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'tag':True,
    'message':"""тerima Kasih Sudah Menambahkan Aku Jadi Teman
≫ Aku Ga Jawab PM Karna aq Cuma Bot Protect ≪
≫ TEAM BOT PROTECT ≪

Ready:

≫ bot protect ≪
≫ SelfBot ≪ 

ṡȗƿƿȏяṭєԀ ɞʏ:
  
☆ TEAM BOT PROTECT ☆
☆ SMULE VOICE FAMILY ☆
☆ FOUNDER COMMUNITY ☆
☆ Generasi Kickers Killers ☆


Minat? Silahkan PM!
Idline: http://line.me/ti/p/~mdnreborn""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"™Luffy™ ",
    "cName2":"™Zorro™ ",
    "cName3":"™Sanji™ ",
    "cName4":"™Ussop™ ",
    "cName5":"™Chooper™ ",
    "cName6":"™Franky™ ",
    "cName7":"™Brook™ ",
    "cName8":"™Nami™ ",
    "cName9":"™Robin™ ",
    "cName10":"™Jinbei™ ",
    "cName11":"",
    "cName12":"™ONE PIECE BOT™ ",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    #"Protectjoin":True, # Ga Kepake(Yang Gabung langsung di kick :D) Udah  Udah ada Protect Cancell
    "Protectcancl":True,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":True,
    "target":{}
}
setTime = {}
setTime = wait2['setTime']

contact = satpam.getProfile()
mybackup = satpam.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

#def NOTIFIED_READ_MESSAGE(op):
    #try:
        #if op.param1 in wait2['readPoint']:
            #Name = cl.getContact(op.param2).displayName
            #if Name in wait2['readMember'][op.param1]:
                #pass
            #else:
                #wait2['readMember'][op.param1] += "\n・" + Name
                #wait2['ROM'][op.param1][op.param2] = "・" + Name
        #else:
            #pass
    #except:
        #pass


def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if op.param2 not in Bots:
              G = random.choice(KAC).getGroup(op.param1)
              G.preventJoinByTicket = True
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).updateGroup(G)
              random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")
        #------Protect Group Kick finish-----#
        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            if op.param2 not in Bots:
              group = cl.getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                if wait["autoJoin"] == True:
                  if op.param2 in Bots or owner:
                    cl.acceptGroupInvitation(op.param1)
                  else:
                    cl.rejectGroupInvitation(op.param1)
            
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                  if op.param2 in Bots or owner:
                    ki.acceptGroupInvitation(op.param1)
                  else:
                    ki.rejectGroupInvitation(op.param1)
                        
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                  if op.param2 in Bots or owner:
                    kk.acceptGroupInvitation(op.param1)
                  else:
                    kk.rejectGroupInvitation(op.param1)
            
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                  if op.param2 in Bots or owner:
                    kc.acceptGroupInvitation(op.param1)
                  else:
                    kc.rejectGroupInvitation(op.param1)
                    
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                  if op.param2 in Bots or owner:
                    ks.acceptGroupInvitation(op.param1)
                  else:
                    ks.rejectGroupInvitation(op.param1)
                    
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                  if op.param2 in Bots or owner:
                    ka.acceptGroupInvitation(op.param1)
                  else:
                    ka.rejectGroupInvitation(op.param1)
                    
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                  if op.param2 in Bots or owner:
                    kb.acceptGroupInvitation(op.param1)
                  else:
                    kb.rejectGroupInvitation(op.param1)
            
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                  if op.param2 in Bots or owner:
                    ko.acceptGroupInvitation(op.param1)
                  else:
                    ko.rejectGroupInvitation(op.param1)
                    
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                  if op.param2 in Bots or owner:
                    ke.acceptGroupInvitation(op.param1)
                  else:
                    ke.rejectGroupInvitation(op.param1)
                    
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                  if op.param2 in Bots or owner:
                    ku.acceptGroupInvitation(op.param1)
                  else:
                    ku.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        #------Joined User Kick start------#
        #if op.type == 17: #awal 17 ubah 13
           #if wait["Protectjoin"] == True:
               #if op.param2 not in admin and Bots : # Awalnya admin doang
                   #random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Joined User Kick start------#
        if op.type == 17:
            if op.param2 not in Bots:
                joinblacklist = op.param2.replace("·",',')
                joinblacklistX = joinblacklist.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, joinblacklistX)
                if matched_list == []:
                    pass
                else:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])

        if op.type == 19: #Member Ke Kick
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          else:
            try:
              cl.kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
              wait["blacklist"][op.param2] = True
              #f=codecs.open('st2__b.json','w','utf-8')
              #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            except:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
              wait["blacklist"][op.param2] = True
              #f=codecs.open('st2__b.json','w','utf-8')
              #json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
            
        
        if op.type == 19: 
          if op.param3 in admin: #Kalo Admin ke Kick
            if op.param2 in Bots:
              pass
            if op.param2 in owner:
              pass
            else:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
        
        if op.type == 19:
          if op.param3 in mid:
                   G = ki.getGroup(op.param1)
                   G.preventJoinByTicket = False
                   Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                   k1.acceptGroupInvitationByTicket(op.param1, Ticket)
                   time.sleep(0.01)
                   k1.kickoutFromGroup(op.param1,[op.param2])
                   k1.inviteIntoGroup(op.param1,[op.param3])
                   k1.leaveGroup(op.param1)
        
        if op.type == 19:
          try:
            if op.param3 in Smid: 
              G = random.choice(KAC).getGroup(op.param1)
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              G.preventJoinByTicket = False
              random.choice(KAC).updateGroup(G)
              Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
              satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              G.preventJoinByTicket = True
              random.choice(KAC).updateGroup(G)
              satpam.updateGroup(G)
              wait["blacklist"][op.param2] = True
                                
            if op.param3 in mid:
              if op.param2 not in Bots or admin:
                try:
                  G = ki.getGroup(op.param1)
                  kk.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kk.updateGroup(G)
                  Ticket = kk.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  kk.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC)(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  #cl.updateGroup(G)
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                
            if op.param3 in Bmid:
              if op.param2 not in Bots or admin:
                try:
                  G = kc.getGroup(op.param1)
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC)(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  #cl.updateGroup(G)
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                
            if op.param3 in Cmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ks.getGroup(op.param1)
                  ks.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ks.updateGroup(G)
                  Ticket = ks.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ks.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC)(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  #cl.updateGroup(G)
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                
            if op.param3 in Dmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ka.getGroup(op.param1)
                  ka.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ka.updateGroup(G)
                  Ticket = ka.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ka.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC)(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  #cl.updateGroup(G)
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                
            if op.param3 in Emid:
              if op.param2 not in Bots or admin:
                try:
                  G = kb.getGroup(op.param1)
                  kb.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kk.updateGroup(G)
                  Ticket = kb.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  kb.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC)(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  #cl.updateGroup(G)
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                
            if op.param3 in Fmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ku.getGroup(op.param1)
                  ku.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ku.updateGroup(G)
                  Ticket = ku.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ku.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC)(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  #cl.updateGroup(G)
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                
            if op.param3 in Gmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ko.getGroup(op.param1)
                  ko.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ko.updateGroup(G)
                  Ticket = ko.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ko.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC)(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  #cl.updateGroup(G)
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                
            if op.param3 in Hmid:
              if op.param2 not in Bots or admin:
                try:
                  G = ke.getGroup(op.param1)
                  ke.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kk.updateGroup(G)
                  Ticket = ke.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  ke.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC)(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  #cl.updateGroup(G)
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                
            if op.param3 in Imid:
              if op.param2 not in Bots or admin:
                try:
                  G = cl.getGroup(op.param1)
                  cl.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except:
                  G = random.choice(KAC)(op.param1)
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  random.choice(KAC).updateGroup(G)
                  Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                  cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.01)
                  G.preventJoinByTicket = True
                  #cl.updateGroup(G)
                  random.choice(KAC).updateGroup(G)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
          except:
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#--------------------------------
        
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                            ki.acceptGroupInvitation(op.param1)
                            kk.acceptGroupInvitation(op.param1)
                            kc.acceptGroupInvitation(op.param1)
                            ks.acceptGroupInvitation(op.param1)
                            ka.acceptGroupInvitation(op.param1)
                            kb.acceptGroupInvitation(op.param1)
                            ko.acceptGroupInvitation(op.param1)
                            ke.acceptGroupInvitation(op.param1)
                            ku.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ki.acceptGroupInvitation(op.param1)
                        kk.acceptGroupInvitation(op.param1)
                        kc.acceptGroupInvitation(op.param1)
                        ks.acceptGroupInvitation(op.param1)
                        ka.acceptGroupInvitation(op.param1)
                        kb.acceptGroupInvitation(op.param1)
                        ko.acceptGroupInvitation(op.param1)
                        ke.acceptGroupInvitation(op.param1)
                        ku.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")
                        kc.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")
                        kc.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        kc.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
                        kc.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Admin menu"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("Luffy gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("Zorro gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")
            elif ("Sanji gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv3 gn ","")
                    kc.updateGroup(X)
                else:
                    kc.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
            elif "Luffy kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_second kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Zorro kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_third kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Sanji kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_fourth kick ","")
                kc.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "Luffy invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("sinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "Zorro invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("tinvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])
            elif "Zorro invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("finvite ","")
                kc.findAndAddContactsByMid(midd)
                kc.inviteIntoGroup(msg.to,[midd])
    #--------------- SC Add Admin ---------
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"Admin Ditambahkan")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                gs = ka.getGroup(msg.to)
                gs = kb.getGroup(msg.to)
                gs = ku.getGroup(msg.to)
                gs = ke.getGroup(msg.to)
                gs = ko.getGroup(msg.to)
                gs = satpam.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"Admin Dihapus")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  cl.sendText(msg.to,"The stafflist is empty")
              else:
                  cl.sendText(msg.to,"Tunggu...")
                  mc = "||Admin Team Bot||\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
    #--------------------------------------
    #-------------- Add Friends ------------
            elif "Bot Add @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in owner:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)
                  gs = kc.getGroup(msg.to)
                  gs = ks.getGroup(msg.to)
                  gs = ka.getGroup(msg.to)
                  gs = kb.getGroup(msg.to)
                  gs = ke.getGroup(msg.to)
                  gs = ko.getGroup(msg.to)
                  gs = ku.getGroup(msg.to)
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)
                        kc.findAndAddContactsByMid(target)
                        ks.findAndAddContactsByMid(target)
                        ka.findAndAddContactsByMid(target)
                        kb.findAndAddContactsByMid(target)
                        ko.findAndAddContactsByMid(target)
                        ke.findAndAddContactsByMid(target)
                        ku.findAndAddContactsByMid(target)
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Perintah Ditolak")
                cl.sendText(msg.to,"Perintah ini Hana Untuk Owner Kami")
                  
    #-------------=SC AllBio=---------------- Ganti Bio Semua Bot Format => Allbio: SUKA SUKA KALIAN :D
            elif "Allbio:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ka.getProfile()
                    profile.statusMessage = string
                    ka.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kb.getProfile()
                    profile.statusMessage = string
                    kb.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ku.getProfile()
                    profile.statusMessage = string
                    ku.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ke.getProfile()
                    profile.statusMessage = string
                    ke.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ko.getProfile()
                    profile.statusMessage = string
                    ko.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
    #--------------=Finish=----------------
            elif msg.text in ["Clear ban"]:
              if msg.from_ in admin:
                    cl.sendText(msg.to,"Waiting for clearing Ban "+ str(len(wait["blacklist"]))+ " users ...")
                    wait["blacklist"] = {}
                    cl.sendText(msg.to,"Clear ban users done ~")
    
    #--------------= SC Ganti nama Owner=--------------
            
            elif "Mycopy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Mycopy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = satpam.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            satpam.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    satpam.cloneContactProfile(target)
                                    satpam.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
                                    
            elif msg.text in ["Mybackup"]:
              if msg.from_ in admin:    
                try:
                    satpam.updateDisplayPicture(mybackup.pictureStatus)
                    satpam.updateProfile(mybackup)
                    satpam.sendText(msg.to, "Backup Sukses Bosqu")
                except Exception as e:
                    satpam.sendText(msg.to, str (e))
            
            elif "Grup image" in msg.text:
			  if msg.from_ in admin:
					group = satpam.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
					cl.sendImageWithURL(msg.to,path)
            
            elif "Getpp @" in msg.text:            
              if msg.from_ in admin:
                print "[Command]dp executing"
                _name = msg.text.replace("Getpp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"

            elif "Getcover @" in msg.text:
              if msg.from_ in admin:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)          
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
            elif "Myname:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name Menjadi : " + string + "")
    #-------------- copy profile----------
            elif "Spam: " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam: ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                if txt[1] == "on":
                    if jmlh <= 300:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Kelebihan batas:v")
                elif txt[1] == "off":
                    if jmlh <= 300:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Kelebihan batas :v")
    #-----------------=Selesai=------------------
            elif msg.text in ["Bot?"]: #Ngirim Semua Kontak Bot
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kb.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ko.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ke.sendMessage(msg)
            elif msg.text in ["Me"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Cv2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Op cancel","Bot cancel"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Buka qr","Open qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"QR Sudah Dibuka")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Terbuka Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Luffy buka qr","Luffy open qr"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done Plak")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Zorro buka qr","Zorro open qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Plak")
                    else:
                        ki.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sanji open qr","Sanji buka qr"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Plak")
                    else:
                        kc.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Tutup qr","Close qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Kode QR Sudah Di Tutup")
                    else:
                        random.choice(KAC).sendText(msg.to,"Sudah Tertutup Plak")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Luffy close qr","Luffy tutup qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done Plak")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Zorro tutup qr","Zorro close qr"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done Plak")
                    else:
                        kk.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Sanji tutup qr","Sanji close qr"]:
                if msg.toType == 2:
                    X = kc.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Done Plak")
                    else:
                        kc.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kc.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kc.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
                     
            elif "Info Group" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "Close"
                    else:
                      QR = "Open"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "[•]" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "[•]" + gCreator + "\n\n[Group Status]\n" + "[•]Status QR =>" + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")
                
            elif "My mid" == msg.text:
              if msg.from_ in admin:
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif "Mid Bot" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
                kc.sendText(msg.to,Cmid)
                ks.sendText(msg.to,Dmid)
                ka.sendText(msg.to,Emid)
                kb.sendText(msg.to,Fmid)
                ko.sendText(msg.to,Gmid)
                ke.sendText(msg.to,Hmid)
                ku.sendText(msg.to,Imid)
            elif "Koplaxs" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,Smid)
            elif "Luffy" == msg.text:
              if msg.from_ in admin:
                ki.sendText(msg.to,mid)
            elif "Zorro" == msg.text:
              if msg.from_ in admin:
                kk.sendText(msg.to,Amid)
            elif "Sanji" == msg.text:
              if msg.from_ in admin:
                kc.sendText(msg.to,Bmid)
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL: "]:
              if msg.from_ in admin:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Bot1 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot2 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Bot3 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Mc "]:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            #elif msg.text in ["Joinn on","joinn on"]:
              #if msg.from_ in admin:
                #if wait["Protectjoin"] == True:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"Kick Joined Group On")
                    #else:
                        #cl.sendText(msg.to,"Done")
                #else:
                    #wait["Protectjoin"] = True
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"Kick Joined Group On")
                    #else:
                        #cl.sendText(msg.to,"done")
            #elif msg.text in ["Joinn off","joinn off"]:
              #if msg.from_ in admin:
                #if wait["Protectjoin"] == False:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"kick Joined Group Off")
                    #else:
                        #cl.sendText(msg.to,"done")
                #else:
                    #wait["Protectjoin"] = False
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"kick Joined Group Off")
                    #else:
                        #cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᏟᎪNᏟᎬᏞ ᏚᎬᎷᏌᎪ ᏌNᎠᎪNᏩᎪN ᎾN ᏴᎾᏚ!")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᏟᎪNᏟᎬᏞ ᏚᎬᎷᏌᎪ ᏌNᎠᎪNᏩᎪN ᎾN ᏴᎾᏚ!")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᏟᎪNᏟᎬᏞ ᏚᎬᎷᏌᎪ ᏌNᎠᎪNᏩᎪN ᎾFF ᏴᎾᏚ!")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"ᏟᎪNᏟᎬᏞ ᏚᎬᎷᏌᎪ ᏌNᎠᎪNᏩᎪN ᎾFF ᏴᎾᏚ!")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Lewat Share Kontak Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["Tag on"]:
              if msg.from_ in admin:
                if wait["tag"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on")
                    else:
                        cl.sendText(msg.to,"Tag On")
                else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag On")
                    else:
                        cl.sendText(msg.to,"already on")
            elif msg.text in ["Tag off"]:
              if msh.from_ in admin:
                if wait["tag"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off")
                    else:
                        cl.sendText(msg.to,"Tag Off")
                else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Tag Off")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Status","Set"]:
              if msg.from_ in admin:
                md = "✃┈┈☫ รεƭƭเɳɠร ☫┈┈✍ \n ================\n"
                if wait["contact"] == True: md+=" ❂͜͡☆➣ Contact:on \n"
                else: md+=" ❂͜͡☆➣Contact:off􀜁􀄰 \n"
                if wait["autoJoin"] == True: md+=" ❂͜͡☆➣ Auto Join:on \n"
                else: md +=" ❂͜͡☆➣ Auto Join:off \n"
                if wait["autoCancel"]["on"] == True:md+=" ❂͜͡☆➣ Auto cancel:" + str(wait["autoCancel"]["members"]) + " \n"
                else: md+=" ❂͜͡☆➣ Group cancel:off \n"
                if wait["leaveRoom"] == True: md+=" ❂͜͡☆➣ Auto leave:on \n"
                else: md+=" ❂͜͡☆➣ Auto leave:off \n"
                if wait["timeline"] == True: md+=" ❂͜͡☆➣ Share:on \n"
                else:md+=" ❂͜͡☆➣ Share:off \n"
                if wait["autoAdd"] == True: md+=" ❂͜͡☆➣ Auto add:on \n"
                else:md+=" ❂͜͡☆➣ Auto add:off \n"
                if wait["commentOn"] == True: md+=" ❂͜͡☆➣ Auto Coment:on \n"
                else:md+=" ❂͜͡☆➣ Auto Coment:off \n"
                if wait["Protectgr"] == True: md+=" ❂͜͡☆➣ ProtectQr:on \n"
                else:md+=" ❂͜͡☆➣ PotectQr:off \n"
                if wait["Protectcancl"] == True: md+=" ❂͜͡☆➣  Protect Invite:on \n"
                else:md+=" ❂͜͡☆➣ Protect Invite:off \n"
                if wait["tag"] == True: md+=" ❂͜͡☆➣ Tag:on \n"
                else: md+=" ❂͜͡☆➣Tag:off􀜁􀄰 \n"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#Sc


            elif "Spamcontact @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Spamcontact @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       kb.sendText(g.mid,"Apa Lo Njeng !")  
                       ka.sendText(g.mid,"Apa Lo Njeng !")  
                       ko.sendText(g.mid,"Apa Lo Njeng !")
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ku.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(g.mid,"Apa Lo Njeng !")
                       kk.sendText(g.mid,"Apa Lo Njeng !")  
                       ki.sendText(g.mid,"Apa Lo Njeng !")  
                       kc.sendText(g.mid,"Apa Lo Njeng !")
                       ks.sendText(g.mid,"Apa Lo Njeng !")
                       cl.sendText(msg.to, "sᴜᴋsᴇs ʙᴏss")
                       print " Spammed !"

                    #-------------mmc-------------------#           
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
             text = msg.text
             if text is not None:
              cl.sendText(msg.to,text)
             else:
              if msg.contentType == 7:
               msg.contentType = 7
               msg.text = None
               msg.contentMetadata = {
                      "STKID": "6",
                      "STKPKGID": "1",
                      "STKVER": "100" }
               cl.sendMessage(msg)
              elif msg.contentType == 13:
               msg.contentType = 13
               msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
               cl.sendMessage(msg)
            elif "Mimic:" in msg.text:
             if msg.from_ in admin:
              cmd = msg.text.replace("Mimic:","")
              if cmd == "on":
               if mimic["status"] == False:
                mimic["status"] = True
                cl.sendText(msg.to,"Mimic on")
               else:
                cl.sendText(msg.to,"Mimic already on")
              elif cmd == "off":
               if mimic["status"] == True:
                mimic["status"] = False
                cl.sendText(msg.to,"Mimic off")
               else:
                cl.sendText(msg.to,"Mimic already off")
              elif "add:" in cmd:
               target0 = msg.text.replace("Mimic:add:","")
               target1 = target0.lstrip()
               target2 = target1.replace("@","")
               target3 = target2.rstrip()
               _name = target3
               gInfo = cl.getGroup(msg.to)
               targets = []
               for a in gInfo.members:
                if _name == a.displayName:
                 targets.append(a.mid)
               if targets == []:
                cl.sendText(msg.to,"No targets")
               else:
                for target in targets:
                 try:
                  mimic["target"][target] = True
                  cl.sendText(msg.to,"Success added target")
                  #cl.sendMessageWithMention(msg.to,target)
                  break
                 except:
                  cl.sendText(msg.to,"Failed")
                  break
              elif "del:" in cmd:
               target0 = msg.text.replace("Mimic:del:","")
               target1 = target0.lstrip()
               target2 = target1.replace("@","")
               target3 = target2.rstrip()
               _name = target3
               gInfo = cl.getGroup(msg.to)
               targets = []
               for a in gInfo.members:
                if _name == a.displayName:
                 targets.append(a.mid)
               if targets == []:
                cl.sendText(msg.to,"No targets")
             else:
                for target in targets:
                 try:
                  del mimic["target"][target]
                  cl.sendText(msg.to,"Success deleted target")
                  #cl.sendMessageWithMention(msg.to,target)
                  break
                 except:
                  cl.sendText(msg.to,"Failed!")
                  break       
#---------------------Sc invite owner ke group------
            elif "/invitemeto: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("/invitemeto: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
#--------===---====--------------
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv3 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kc.updateGroup(x)
                    gurl = kc.reissueGroupTicket(msg.to)
                    kc.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
              if msg.from_ in admin:
                if wait["clock"] == True:
                    kc.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
              if msg.from_ in admin:
                if wait["clock"] == False:
                    kc.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kc.sendText(msg.to,"Jam Sedang Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
         
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kc.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"Sukses update")
                else:
                    kc.sendText(msg.to,"Aktifkan jam terlebih dulu")
        #-------------Fungsi Jam Update Finish-------------------#
            
            elif msg.text in ["Lihat"]:
                 if msg.toType == 2:
                    cl.sendText(msg.to, "Sini Muncul lo Anjing!")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    print "Lurkset"
            elif msg.text in ["Ciduk loh"]:
                 if msg.toType == 2:
                    print "\nSider check aktif..."
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "✔ Read : %s\n\n✖ Sider :\n%s\nPoint creation date n time:\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "\nReading Point Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "lukers"
                        cl.sendText(msg.to, "Ga senang? PC aja KENTOD!")
                    else:
                        cl.sendText(msg.to, "Set Lurkes first")
#-----------------------------------------------
#-----------------------------------------------
            elif "Say " in msg.text:
                say = msg.text.replace("Say ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#-----------------------------------------------
#----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Kuy","One piece","Join kuy"]:
              if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        print "Semua Sudah Lengkap"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
  
            elif msg.text in ["Sini","Kunyuk"]:
              if msg.from_ in admin:
                        G = satpam.getGroup(msg.to)
                        ginfo = satpam.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        satpam.updateGroup(G)
                        invsend = 0
                        Ticket = satpam.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = satpam.getGroup(msg.to)
                        ginfo = satpam.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        satpam.updateGroup(G)
                        print "Semua Sudah Lengkap"
                        G.preventJoinByTicket(G)
                        satpam.updateGroup(G)

            elif msg.text in ["Kampret join"]:
              if msg.form_ in admin:
                  x = ki.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  ki.updateGroup(x)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["Luffy join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["Zorro join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
                  
            elif msg.text in ["Sanji Join"]:
              if msg.from_ in admin:
                  X = cl.getGroup(msg.to)
                  X.preventJoinByTicket = False
                  cl.updateGroup(X)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kc.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)
    #----------------------Fungsi Join Group Finish---------------#
            elif "youtube:" in msg.text.lower():
                   query = msg.text.split(":")
                   try:
                       if len(query) == 3:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Bye op","Kabur all","Kaboor all"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            
            elif msg.text in ["Kaboor"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        #cl.leaveGroup(msg.to)
                    except:
                        pass
                      
            elif msg.text in ["Bye zorro"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye sanji"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Bye Ussop"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ojo koyo kuwe1"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ojo koyo kuwe2"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Ojo koyo kuwe3"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kc.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag all","Crott"]:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#
            elif msg.text in ["Bot Like", "Bot like"]: #Semua Bot Ngelike Status Akun Utama
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Owner")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in ["Like temen", "Bot like temen"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Kami Siap Like Status Teman Boss")
                try:
                  autolike()
                except:
                  pass
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Selamat tinggal")
                        random.choice(KAC).sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,ks,ka,kb,ku,ke,ko]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
        #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Salam" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Salam","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = ks.getGroup(msg.to)
                    gs = ka.getGroup(msg.to)
                    gs = kb.getGroup(msg.to)
                    gs = ku.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = ko.getGroup(msg.to)
                    random.choice(KAC).sendText(msg.to,"Makasih udh undang kami yah")
                    random.choice(KAC).sendText(msg.to,"Kami siap Protect Group kamu")
                    random.choice(KAC).sendText(msg.to,"Tapi Boong........... hehehhehe")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    random.choice(KAC).sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KAC).sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target in Bots:
                            pass
                          elif target in admin:
                            pass
                          else:
                            try:
                                klist=[ki,kk,kc,ks,ka,kb,ku,ke,ko]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                random.choice(KAC).sendText(msg.to,"Jangan Baper")
                                random.choice(KAC).sendText(msg.to,"Dasar lemah")
                                random.choice(KAC).sendText(msg.to,"Ga senang cht aja owner kami")

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
              if msg.from_ in admin:
                nk0 = msg.text.replace("Nk ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                       targets.append(s.mid)
                if targets == []:
                   sendMessage(msg.to,"user does not exist")
                   pass
                else:
                   for target in targets:
                      try:
                        k1.kickoutFromGroup(msg.to,[target])
                        print (msg.to,[g.mid])
                      except:
                        k1.leaveGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        gs.preventJoinByTicket = True
                        cl.updateGroup(gs)
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = random.choice(KAC).getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            random.choice(KAC).sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    random.choice(KAC).sendText(msg.to,"Succes Plak")
                                except:
                                    random.choice(KAC).sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Sukses"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Dilarang Banned Bot")
                        ki.sendText(msg.to,"Dilarang Banned Bot")
                        kk.sendText(msg.to,"Dilarang Banned Bot")
                        kc.sendText(msg.to,"Dilarang Banned Bot")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KAC).sendText(msg.to,"Akun telah sukses di banned")
                            except:
                                random.choice(KAC).sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            elif msg.text == "Link Anu":
                    cl.sendText(msg.to,"nekopoi.host")
                    cl.sendText(msg.to,"sexvideobokep.com")
                    cl.sendText(msg.to,"memek.com")
                    cl.sendText(msg.to,"pornktube.com")
                    cl.sendText(msg.to,"faketaxi.com")
                    cl.sendText(msg.to,"videojorok.com")
                    cl.sendText(msg.to,"watchmygf.mobi")
                    cl.sendText(msg.to,"xnxx.com")
                    cl.sendText(msg.to,"xvideos.com")
                    cl.sendText(msg.to,"m.xhamster.com")
                    cl.sendText(msg.to,"xxmovies.pro")
                    cl.sendText(msg.to,"youporn.com")
                    cl.sendText(msg.to,"anyporn.com")
                    cl.sendText(msg.to,"rubyourdick.com")
                    cl.sendText(msg.to,"anybunny.mobi")
                    cl.sendText(msg.to,"cliphunter.com")
                    cl.sendText(msg.to,"sexloving.net")
                    cl.sendText(msg.to,"free.goshow.tv")
                    cl.sendText(msg.to,"eporner.com")
                    cl.sendText(msg.to,"Pornhd.josex.net")
                    cl.sendText(msg.to,"m.hqporner.com")
                    cl.sendText(msg.to,"m.spankbang.com")
                    cl.sendText(msg.to,"m.4tube.com")
                    cl.sendText(msg.to,"brazzers.com")
                    cl.sendText(msg.to,"pornhd.com")
                    cl.sendText(msg.to,"vidz7.com")
                    cl.sendText(msg.to,"pornhub.com")
                    cl.sendText(msg.to,"hdsexdino.com")
                    cl.sendText(msg.to,"Udh gw ksh nih link simpanen gue")
                    cl.sendText(msg.to,"Ga ush MUNAFIK ddeh KENTOD! kalau lu emng mau nonton ya tonton aja!!")
      #--------------------------------- DUGEM ------------------------------------
            elif "kedapkedip " in msg.text.lower():
                txt = msg.text.replace("kedapkedip ", "")
                cl.kedapkedip(msg.to,txt)
                print "[Command] Kedapkedip"
#----------------------------------------------------------------------------
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
		        print song[0,1,2,3,4,5]
#--------------------------------- INSTAGRAM --------------------------------
            elif '.instagram ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace(".instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "INSTAGRAM INFO USER\n"
                    details = "\nINSTAGRAM INFO USER"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            #----------------------------------------------------------------------------
            elif "Uni" in msg.text:
                cl.sendText(msg.to,"1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.01.0.1.0.1.0.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.01.0.1.0.1.0.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.00.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.10.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1..0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.01.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.01.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0.1.0")

            #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------
            elif 'wikipedia ' in msg.text.lower():
                  try:
                      wiki = msg.text.lower().replace("wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
         #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"Tidak Ditemukan.....")
                        kk.sendText(msg.to,"Tidak Ditemukan.....")
                        kc.sendText(msg.to,"Tidak Ditemukan.....")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
          #----------------Fungsi Unbanned User Target Finish-----------------------#
            
            elif msg.text == "Trans":
                cl.sendText(msg.to,"Translator\n tr-id:  -> All bahasa-Indonesia\n tr-en:  -> Indonesia-English\n tr-fr:  -> Indonrsia-French\n tr-ar:  -> Indonesia-Arabic\n tr-cn:  -> Indonesia-China\n tr-de:  -> Indonesia-German\n tr-hi:  -> Indonesia-Hindi\n tr-ja:  -> Indonesia-Japanese\n tr-jw:  -> Indonesia-Jawa\n tr-ko:  -> Indonesia-Korean\n tr-th:  -> Indonesia-Thailand\n tr-af:  -> Indonesia-Afrikaans\n tr-sq:  -> Indonesia-Albanian\n tr-th:  -> Indonesia-Thailand\n tr-hy:  -> Indonesia-Armenian\n tr-bn:  -> Indonesia-Bengali\n tr-ca:  -> Indonesia-Catalan\n tr-tw:  -> Indonesia-Taiwan\n tr-yue:  -> Indonesia-Cantonese\n tr-hr:  -> Indonesia-Crotian\n tr-cs:  -> Indonesia-Czech\n tr-da:  -> Indonesia-Danish\n tr-nl:  -> Indonesia-Dutch\n tr-au:  -> Indonesia-English (Australia)\n tr-uk:  -> Indonesia-English (United Kingdom)\n tr-us:  -> Indonesia-English (United States)\n tr-eo:  -> Indonesia-Esperanto\n tr-fi:  -> Indonesia-Finnish\n")
            elif "tr-id:" in msg.text:
                isi = msg.text.replace("tr-id:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-en: " in msg.text:
                isi = msg.text.replace("tr-en:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-fr: " in msg.text:
                isi = msg.text.replace("tr-fr:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='fr')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-ar: " in msg.text:
                isi = msg.text.replace("tr-ar:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-cn: " in msg.text:
                isi = msg.text.replace("tr-cn:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='zh-CN')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-de: " in msg.text:
                isi = msg.text.replace("tr-de:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='de')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-hi: " in msg.text:
                isi = msg.text.replace("tr-hi:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='hi')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-ja: " in msg.text:
                isi = msg.text.replace("tr-ja:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-jw: " in msg.text:
                isi = msg.text.replace("tr-jw:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='jw')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-ko: " in msg.text:
                isi = msg.text.replace("tr-ko:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-th: " in msg.text:
                isi = msg.text.replace("tr-th:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='th')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-af: " in msg.text:
                isi = msg.text.replace("tr-af:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='af')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-sq: " in msg.text:
                isi = msg.text.replace("tr-sq:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='sq')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-hy: " in msg.text:
                isi = msg.text.replace("tr-hy:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='hy')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-bn: " in msg.text:
                isi = msg.text.replace("tr-bn:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='bn')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-ca: " in msg.text:
                isi = msg.text.replace("tr-ca:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ca')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-tw: " in msg.text:
                isi = msg.text.replace("tr-tw:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='zh-tw')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-yue: " in msg.text:
                isi = msg.text.replace("tr-yue:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='zh-yue')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-hr: " in msg.text:
                isi = msg.text.replace("tr-hr:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='hr')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-cs: " in msg.text:
                isi = msg.text.replace("tr-cs:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='cs')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-da: " in msg.text:
                isi = msg.text.replace("tr-da:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='da')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-nl: " in msg.text:
                isi = msg.text.replace("tr-nl:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='nl')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-au: " in msg.text:
                isi = msg.text.replace("tr-au:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en-au')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-uk: " in msg.text:
                isi = msg.text.replace("tr-uk:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en-uk')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-us: " in msg.text:
                isi = msg.text.replace("tr-us:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en-us')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-eo: " in msg.text:
                isi = msg.text.replace("tr-eo:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='eo')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-fi: " in msg.text:
                isi = msg.text.replace("tr-fi:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='fi')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-el: " in msg.text:
                isi = msg.text.replace("tr-el:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='el')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-hu: " in msg.text:
                isi = msg.text.replace("tr-hu:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='hu')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-is: " in msg.text:
                isi = msg.text.replace("tr-is:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='is')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-it: " in msg.text:
                isi = msg.text.replace("tr-it:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='it')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-la: " in msg.text:
                isi = msg.text.replace("tr-la:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='la')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-lv: " in msg.text:
                isi = msg.text.replace("tr-lv:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='lv')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-mk: " in msg.text:
                isi = msg.text.replace("tr-mk:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='mk')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-no: " in msg.text:
                isi = msg.text.replace("tr-no:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='no')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-pl: " in msg.text:
                isi = msg.text.replace("tr-pl:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='pl')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-pt: " in msg.text:
                isi = msg.text.replace("tr-pt:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='pt')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-ro: " in msg.text:
                isi = msg.text.replace("tr-ro:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ro')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)
            elif "tr-ru: " in msg.text:
                isi = msg.text.replace("tr-ru:","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ru')
                A = hasil.text
                A = A.encode('utf-8')
                cl.sendText(msg.to, A)


        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                cl.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
                ki.sendText(msg.to,"P 􀔃􀆶squared up!����")
                kk.sendText(msg.to,"P 􀔃􀆶squared up!􏿿")
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg.from_ in owner:
                 bctxt = msg.text.replace("Bc ","")
                 a = cl.getGroupIdsJoined()
                 a = ki.getGroupIdsJoined()
                 a = kk.getGroupIdsJoined()
                 a = kc.getGroupIdsJoined()
                 a = ks.getGroupIdsJoined()
                 a = ka.getGroupIdsJoined()
                 a = ku.getGroupIdsJoined()
                 a = ke.getGroupIdsJoined()
                 a = ko.getGroupIdsJoined()
                 a = kb.getGroupIdsJoined()
                 for taf in a:
                     cl.sendText(taf, (bctxt))
                     ki.sendText(taf, (bctxt))
                     kk.sendText(taf, (bctxt))
                     kc.sendText(taf, (bctxt))
                     ks.sendText(taf, (bctxt))
                     ka.sendText(taf, (bctxt))
                     kb.sendText(taf, (bctxt))
                     ke.sendText(taf, (bctxt))
                     ku.sendText(taf, (bctxt))
                     ko.sendText(taf, (bctxt))
      #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["LG"]: #Melihat List Group
              if msg.from_ in admin:
                 gids = cl.getGroupIdsJoined()
                 h = ""
                 for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += "[•]%s Member\n" % (cl.getGroup(i).name   +"👉"+str(len(cl.getGroup(i).members)))
                 cl.sendText(msg.to,"=======[List Group]======\n"+ h +"Total Group :"+str(len(gids)))
                
            elif msg.text in ["LG2"]: #Melihat List Group + ID Groupnya (Gunanya Untuk Perintah InviteMeTo:)
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
      #--------------List Group------------
       #------------ Keluar Dari Semua Group------
            elif msg.text in ["Bot out","Op bye"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in owner:
                 gid = cl.getGroupIdsJoined()
                 gid = ki.getGroupIdsJoined()
                 gid = kk.getGroupIdsJoined()
                 gid = kc.getGroupIdsJoined()
                 gid = ks.getGroupIdsJoined()
                 gid = ka.getGroupIdsJoined()
                 gid = kb.getGroupIdsJoined()
                 gid = ko.getGroupIdsJoined()
                 gid = ke.getGroupIdsJoined()
                 gid = ku.getGroupIdsJoined()
                 for i in gid:
                   ku.leaveGroup(i)
                   ke.leaveGroup(i)
                   ko.leaveGroup(i)
                   kb.leaveGroup(i)
                   ka.leaveGroup(i)
                   ks.leaveGroup(i)
                   kc.leaveGroup(i)
                   ki.leaveGroup(i)
                   kk.leaveGroup(i)
                   cl.leaveGroup(i)
                 if wait["lang"] == "JP":
                   cl.sendText(msg.to,"Sayonara")
                 else:
                   cl.sendText(msg.to,"He declined all invitations")
 #------------------------End---------------------

 #-----------------End-----------
            elif msg.text in ["Op katakan hi"]:
                ki.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hi buddy 􀜁􀅔Har Har􏿿")

#-----------------------------------------------
            elif msg.text in ["Cv say hinata pekok"]:
                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say didik pekok"]:
                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Selamat datang di Group Kami")
                kk.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Absen","Absen bot","Absen dulu","Respon"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Hadir Bos")
                ki.sendText(msg.to,"Hadir Bos")
                kk.sendText(msg.to,"Hadir Bos")
                kc.sendText(msg.to,"Hadir Bos")
                ks.sendText(msg.to,"Hadir Bos")
                ka.sendText(msg.to,"Hadir Bos")
                kb.sendText(msg.to,"Hadir Bos Hadir Bos mulu lu njing")
                ko.sendText(msg.to,"Bodo aamat gw kick lu baru tau")
                ke.sendText(msg.to,"Apaan nih ribut ribut-_")
                ku.sendText(msg.to,"Udh oi")
                cl.sendText(msg.to,"Mohon maaf anak buat gw agak gesrek\nIntinya yah... Bodo amat lah\n")
      #-------------Fungsi Respon Finish---------------------#
            elif msg.text in ["Restart"]:
              if msg.from_ in owner:
                cl.sendText(msg.to, "Reboot Bot DraBas")
                restart_program()
                print "Sukses Di Restart Bas"                  
      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#

#----------
            elif "Setimage " in msg.text:
                wait["Pap"] = msg.text.replace("Setimage ","")
                cl.sendText(msg.to,"Image Has Ben Set To")

            elif msg.text in ["Papimage","Papim"]:
                cl.sendImageWithURL(msg.to,wait["Pap"])
#-----------
            elif "Setvideo " in msg.text:
                wait["Pap"] = msg.text.replace("Setvideo ","")
                cl.sendText(msg.to,"Video Has Ben Set To")

            elif msg.text in ["Papvideo","Papvid"]:
                cl.sendVideoWithURL(msg.to,wait["Pap"])
#-----------
       
       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","Sp"]:
              if msg.from_ in admin and owner:
                start = time.time()
                cl.sendText(msg.to, "Sabar Plak...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sDetik" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
              if msg.from_ in owner:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                ki.sendText(msg.to,"Kirim contact")
                kk.sendText(msg.to,"Kirim contact")
                kc.sendText(msg.to,"Kirim contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in owner:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Kirim contact")
                ki.sendText(msg.to,"Kirim contact")
                kk.sendText(msg.to,"Kirim contact")
                kc.sendText(msg.to,"Kirim contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["Creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'u9f755a553e455e532c681227498abbe0'}
              cl.sendText(msg.to,"======================")
              cl.sendMessage(msg)
              cl.sendText(msg.to,"======================")
              cl.sendText(msg.to,"Itu Creator Kami! Pea lu 😜")
                
      #-------------Fungsi Chat ----------------
            elif msg.text in ["Woy","woy","Woi","woi","bot","Bot"]:
                 quote = ['Istri yang baik itu Istri yang Mengizinkan Suaminya untuk Poligami 😂😂😂.','Kunci Untuk Bikin Suami Bahagia itu cuma satu..\nIzinkan Suamimu Untuk Selingkuh Coyyy ','Ah Kupret Lu','Muka Lu Kaya Jamban','Ada Orang kah disini?','Sange Euy','Ada Perawan Nganggur ga Coy?']
                 psn = random.choice(quote)
                 cl.sendText(msg.to,psn)
            
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    random.choice(KAC).sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
    #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    random.choice(KAC).sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    random.choice(KAC).sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#------------------------
        
        if "@􀄆􀜁☬Bas􏿿􀔃􀄩􏿿"+cl.getProfile().displayName in msg.text:
                if wait["tag"] == True:
                    tanya = msg.text.replace("@􀄆􀜁☬Bas􏿿􀔃􀄩􏿿"+cl.getProfile().displayName,"")
                    jawab = (cl.getProfile().displayName+"Bas sedang sibuk/Off\nJika penting silakan Pesonal chat\n#Automatically Answered by Bots")
                    jawaban = (jawab)
                    satpam.sendText(msg.to,jawaban)
        
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・ " + Name + datetime.datetime.today().strftime(' [%d - %H:%M:%S]')
                        wait2['ROM'][op.param1][op.param2] = "・ " + Name
                        wait2['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    pass
            except:
                pass
#---------------------
        if op.type == 17:
           if op.param2 in Bots:
              return
           ginfo = cl.getGroup(op.param1)
           #random.choice(KAC).sendText(op.param1, "Selamat Datang Di Grup  " + str(ginfo.name))
           random.choice(KAC).sendText(op.param1, "Pembuat Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
           #random.choice(KAC).sendText(op.param1,"Budayakan Baca Note !!! yah Ka 😊\nSemoga Betah Kk 😘")
           print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
           if op.param2 in Bots:
              return
           random.choice(KAC).sendText(op.param1, "Babay yah ")
           print "MEMBER HAS LEFT THE GROUP"
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def autolike():
    for zx in range(0,20):
      hasil = cl.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          satpam.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          satpam.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"👉Auto Like by ⭐⭐Ayang beb⭐⭐👈\n\n™awkarin")
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kc.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ks.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ka.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kb.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ku.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ku.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ke.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          ko.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ko.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Aku Juga Ikutin Boss Aku Like Status Kamu Ka\n\n Like Back yah Ka 😊")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.60)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kc.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ks.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ka.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kb.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ku.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ke.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ko.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by Team Protect Bot\nStatus Boss udah Kami Like\nOwner Kami :\nIndra Bas")
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like Plak"
                
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5a)

                profile6 = ka.getProfile()
                profile6.displayName = wait["cName6"]
                ka.updateProfile(profile6)

                profile7 = kb.getProfile()
                profile7.displayName = wait["cName7"]
                kb.updateProfile(profile7)

                profile8 = ko.getProfile()
                profile8.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile9 = ke.getProfile()
                profile9.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile10 = ku.getProfile()
                profile10.displayName = wait["cName10"]
                ku.updateProfile(profile10)
                
                profile11 = satpam.getProfile()
                profile11.displayName = wait["cName11"]
                satpam.updateProfile(profile11)
                
                profile12 = k1.getProfile()
                profile12.displayName = wait["cName12"]
                k1.updateProfile(profile12)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
