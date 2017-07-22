#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-09-17 09:42:49
# @Author  : veng (veng6115@gmail.com)
# @Link    : http://www.veng.cc
# @update  : 2016-01-28 18:37
# @title   : server auto login, file transport,excute.
import os

import optparse
import datetime
import time
import ConfigParser
import pexpect
import getpass

from multiprocessing import Pool

import paramiko


VERSION = 'hhly auto manger tool 3.0'
TAGMSG = '----------------------------------------------------------------------------------\n'


def func_excute((ip, args)):
    '''excute'''
    retdict = {}
    sshhandler = args[0]
    sshkey = args[1]
    commandline = args[2]
    bsuroot = args[3]
    bpasslogin = args[4]
    sshpassword = args[5]
    bret, data = sshhandler.excute(
        ip, commandline, sshkey, bsuroot, bpasslogin, sshpassword)
    msg = ''
    retdict['ip'] = ip
    retdict['type'] = 'success' if bret else 'fail'
    if isinstance(data, list):
        for line in data:
            try:
                msg += line.strip() + '\n'
            except Exception as e:
                msg += line
    else:
        msg += data
    retdict['msg'] = msg
    return retdict


def func_upload((ip, args)):
    '''upload'''

    retdict = {}
    sshhandler = args[0]
    sshkey = args[1]
    srcpath = args[2]
    dstpath = args[3]
    bdownload = args[4]
    bret = sshhandler.upload(ip, srcpath, dstpath, sshkey, bdownload)
    if bdownload:
        msg = 'download %s to %s' % (srcpath, dstpath)
    else:
        msg = 'upload %s to %s' % (srcpath, dstpath)
    retdict['ip'] = ip
    retdict['type'] = 'success' if bret else 'fail'
    if bret:
        msg += " successed!\n"
    else:
        msg += " failed!\n"
    retdict['msg'] = msg
    return retdict


class MangerServer:

    """ 服务器管理 """

    def __init__(self, curuser, confpath='/etc/manager.conf'):
        self.user = curuser
        self.confpath = confpath if confpath is not None else '/etc/manager.conf'
        self.ipsdict = {}
        self.usersdict = {}
        self.zonesdict = {}
        self.zonenamesdict = {}

    def splitip(self, ips):
        '''分割IP'''

        iplist = []
        for line in ips.split(','):
            if '-' in line:
                endpos = line.find('-')
                bpos = line.rfind('.')

                ip = line[:bpos + 1]
                start = int(line[bpos + 1:endpos])
                end = int(line[endpos + 1:])

                for i in xrange(start, end + 1):
                    iplist.append(ip + str(i))
            else:
                iplist.append(line)
        return iplist

    def loadconf(self):
        '''加载用户配置文件'''
        ipsdict = {}
        usersdict = {}
        zonesdict = {}
        zonenamesdict = {}
        cf = ConfigParser.ConfigParser()
        cf.read(self.confpath)

        opts = cf.options("zonename")
        for opt in opts:
            zonenamesdict[opt] = cf.get("zonename", opt)

        opts = cf.options("zonelist")
        for opt in opts:
            zonesdict[opt] = eval(cf.get("zonelist", opt))

        opts = cf.options("userlist")
        for opt in opts:
            usersdict[opt] = eval(cf.get("userlist", opt))

        opts = cf.options("iplist")
        for opt in opts:
            retiplist = []
            for ips in eval(cf.get("iplist", opt)):
                retiplist += self.splitip(ips)
            ipsdict[opt] = retiplist

        self.ipsdict = ipsdict
        self.usersdict = usersdict
        self.zonesdict = zonesdict
        self.zonenamesdict = zonenamesdict

    def manger(self, dstip):
        ''' 管理用户权限 '''

        pos = dstip.find('.')
        ip = dstip
        if dstip[0:pos] in ['10', '183']:
            ip = '*' + dstip[pos:]

        for key in self.usersdict:
            if self.user in self.usersdict[key]:
                if ip in self.ipsdict[key] or dstip in self.ipsdict[key]:
                    return True
        return False

    def getzonelist(self):
        '''获取各地区的服务器ip'''

        return self.zonenamesdict, self.zonesdict, self.usersdict


class ShellManger:

    """ 服务器自动登录管理 """

    def __init__(self, sshkeypath='/data/tools/common_id_rsa',
                 sshoarg=' -o StrictHostKeyChecking=no -o GSSAPIAuthentication=no',
                 username='hhlyadmin',
                 port=2222,
                 sshkeywithpass=False,
                 sshkeypass="keyG@(D*$&_#!}Hhly"):
        self.keypath = sshkeypath
        self.sshoarg = sshoarg

        self.username = username if username is not None else 'hhlyadmin'
        self.port = port if port is not None else 2222
        self.sshkeywithpass = sshkeywithpass
        self.sshkeypass = sshkeypass

    def login(self, ip):
        '''登录服务器'''
        commandline = 'ssh -p%d %s@%s -i %s %s' % (self.port, self.username,
                                                   ip, self.keypath,
                                                   self.sshoarg)
        if self.sshkeywithpass:
            msg = "Enter passphrase for key '%s':" % self.keypath
            try:
                ssh = pexpect.spawn(commandline)
                i = ssh.expect(msg)
                if i == 0:
                    ssh.sendline(self.sshkeypass)
                ssh.interact()
            except pexpect.EOF:
                ssh.close()
            except pexpect.TIMEOUT:
                print 'connect timeout.'
                ssh.close()
        else:
            os.system(commandline)


class SSHHandler:

    """通过ssh来上传文件或者执行命令
    >>> from lib.sshproxy import SSHHandler
    >>> _sshd = SSHHandler()
    >>> bret=_sshd.upload('192.168.1.1','/home/1.txt','/tmp/')
    """

    def __init__(self, timeout=60,
                 dstport=2222,
                 dstuser='hhlyadmin',
                 privkey_path='/data/tools/common_id_rsa'):
        self.dstport = dstport
        self.dstuser = dstuser if dstuser is not None else 'hhlyadmin'
        self.privkey_path = privkey_path if privkey_path is not None else '/data/tools/common_id_rsa'
        self.timeout = timeout if timeout is not None else 60

    def getraskey(self, sshkeywithpass=False, password='keyG@(D*$&_#!}Hhly'):
        '''读取rsa证书,证书是否有设置密码'''
        sshkey = None
        try:
            privkeyfile = os.path.expanduser(self.privkey_path)
            # use for ssh ras key path with password
            if sshkeywithpass:
                sshkey = paramiko.RSAKey.from_private_key_file(
                    privkeyfile,
                    password=password)
            else:
                sshkey = paramiko.RSAKey.from_private_key_file(privkeyfile)
        except Exception as e:
            pass
        finally:
            return sshkey

    def upload(self, dstip, srcfpath, dstfpath, sshkey, bdownload):
        '''使用paramiko模块中的sftp来传输,基于rsa证书'''
        ret = False
        t = None
        sftp = None
        try:
            t = paramiko.Transport((dstip, self.dstport))
            t.connect(username=self.dstuser, pkey=sshkey)
            sftp = paramiko.SFTPClient.from_transport(t)
            if bdownload:
                sftp.get(srcfpath, dstfpath + '_' + dstip)
            else:
                sftp.put(srcfpath, dstfpath)
            ret = True
        except Exception as e:
            print e
        finally:
            if t is not None:
                t.close()
            if sftp is not None:
                sftp.close()
            return ret

    def excute(self, dstip, commandline, sshkey, bneedsu=False,
               bpasslogin=False, sshpassword=None):
        '''推送命令执行'''

        bret = False
        output = []
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if bpasslogin:
                client.connect(dstip, self.dstport, self.dstuser, sshpassword,
                               timeout=self.timeout)
            else:
                client.connect(dstip, self.dstport, self.dstuser, pkey=sshkey,
                               timeout=self.timeout)
        except Exception as e:
            if client is not None:
                client.close()
            return bret, [str(e)]
        if bneedsu:
            channel = client.invoke_shell()
            time.sleep(0.1)
            channel.recv(1024)
            channel.send('sudo su - \n')
            # 是否需要输入密码
            buf = ''
            btime = time.clock()
            while not (buf.startswith('Password: ') or
                       buf.startswith('[sudo] password') or
                       buf.endswith('#')):
                resp = channel.recv(1024)
                if not resp.startswith("sudo su -"):
                    buf += resp
                if int(time.clock() - btime) > 30:
                    channel.close()
                    client.close()
                    return bret, 'recv date timeout.'
            if (buf.startswith('Password: ') or
                    buf.startswith('[sudo] password')):
                channel.close()
                client.close()
                output = buf
                # channel.send('rootpasswd')
                # channel.send('\n')
            else:
                btime = time.clock()
                channel.send(commandline)
                channel.send('\n')
                buf = ''
                while not buf.endswith('#'):
                    resp = channel.recv(5120)
                    buf += resp
                    if int(time.clock() - btime) > self.timeout:
                        break
                channel.close()
                client.close()
                output = buf.split('\n')[1:-1]
                bret = True
        else:
            try:
                stdin, stdout, stderr = client.exec_command(commandline,
                                                            timeout=self.timeout
                                                            )
                filecontent = ''
                while True:
                    lines = stdout.readlines(10000)
                    if not lines:
                        break
                    for line in lines:
                        filecontent = filecontent + line
                output.append(filecontent)
                error = stderr.readlines()
                if error:
                    output += error
                else:
                    bret = True
            except Exception as e:
                output = [str(e)]
            client.close()

        return bret, output


class IPHandler:

    """ 分割IP为iplist,
        处理类似192.168.1.1-254,192.168.2.2,
        处理注释的IP，如#192.168.3.3
    """

    def __init__(self):
        pass

    def splitip(self, ips):
        '''分割IP'''

        iplist = []
        for line in ips.split(','):
            if '-' in line:
                endpos = line.find('-')
                bpos = line.rfind('.')

                ip = line[:bpos + 1]
                start = int(line[bpos + 1:endpos])
                end = int(line[endpos + 1:])

                for i in xrange(start, end + 1):
                    iplist.append(ip + str(i))
            else:
                if line is not None:
                    iplist.append(line)
        return iplist

    def getipfromfile(self, path):
        '''从文件中获取ip，去掉注释的ip'''

        iplist = []
        if os.path.exists(path):
            try:
                fp = open(path, 'r')
            except Exception as e:
                print 'not allowed read from %s.' % path
                return []
            for line in fp.readlines():
                if not line.startswith('#'):
                    ip = line.strip('\n')
                    if ip is not None:
                        iplist += self.splitip(ip)
            if fp is not None:
                fp.close()
            return iplist
        else:
            print 'ip file not exists.'
            return []


def todo(parser, options, zonesdict):
    '''work module'''

    bUploadFunc = False
    threadnum = 0
    bdownload = False

    sshhandler = SSHHandler(timeout=int(options.timeout), 
                            dstport=int(options.sshport),
                            dstuser=options.sshuser)
       
    if options.threadnumber is not None:
        threadnum = int(options.threadnumber)

    if options.bsuroot is not None:
        bsuroot = True
    else:
        bsuroot = False

    if options.bpasslogin is not None:
        bpasslogin = True
    else:
        bpasslogin = False

    if options.sshpass is not None:
        sshpass = options.sshpass
    else:
        sshpass = None

    if options.download is not None:
        bdownload = True
    else:
        bdownload = False
    # ssh证书是否有密码,默认没有密码
    # sshkey = sshhandler.getraskey()

    sshkey = sshhandler.getraskey(True)
    begintime = datetime.datetime.now()

    iphandler = IPHandler()
    iplist = []

    commandline = options.commandline

    if options.ip is not None:
        iplist = iphandler.splitip(options.ip)
    elif options.zone is not None:
        if ',' in options.zone:
            zonenamelist = options.zone.split(',')
            for zonename in zonenamelist:
                name = zonename.strip().lower()
                if name in zonesdict.keys():
                    zoneiplist = zonesdict[name]
                    for line in zoneiplist:
                        iplist += iphandler.splitip(line)
        else:
            name = options.zone.strip().lower()
            if name in zonesdict.keys():
                zoneiplist = zonesdict[name]
                for line in zoneiplist:
                    iplist += iphandler.splitip(line)
    else:
        if os.path.exists(options.ipfile):
            iplist = iphandler.getipfromfile(options.ipfile)

    if options.debug is not None:
        print 'will do ip list:', iplist
    if options.srcpath is not None and options.dstpath is not None:
        srcpath = options.srcpath
        bUploadFunc = True
        try:
            path, filename = os.path.split(options.srcpath)
            dstpath = os.path.join(options.dstpath, filename)
        except Exception as e:
            print e

    if iplist is not None:
        if options.commandline or bUploadFunc:
            if bUploadFunc:
                args = (sshhandler, sshkey, srcpath, dstpath, bdownload)
            else:
                args = (
                    sshhandler, sshkey, commandline,
                    bsuroot, bpasslogin, sshpass)

            if options.debug is not None:
                print 'args:', args

            ret = []
            pool = Pool() if threadnum == 0 else Pool(threadnum)

            argslist = [args for i in range(len(iplist))]
            if bUploadFunc:
                ret.append(
                    pool.map_async(func_upload, zip(iplist, argslist)).get(600))
            else:
                ret.append(
                    pool.map_async(func_excute, zip(iplist, argslist)).get(600))
            pool.close()
            pool.join()

            isuccess = ifail = 0
            successlist = []
            faillist = []
            for line in ret[0]:
                if line['type'] == 'success':
                    isuccess += 1
                    successlist.append(line)
                else:
                    ifail += 1
                    faillist.append(line)
            if options.commandline:
                print '\ncommandline:\t [%s]' % options.commandline

            print TAGMSG, TAGMSG
            print 'sucessed results:\n'
            for line in successlist:
                print '%sip:\t%s\n%s' % (TAGMSG, line['ip'], line['msg'])
            if ifail != 0:
                print TAGMSG, TAGMSG
                print 'failed results:\n'
                for line in faillist:
                    print 'ip: %s\tmsg: %s' % (line['ip'], line['msg'])
                print TAGMSG, TAGMSG

            print 'successed nums : %d, failed nums : %d' % (isuccess, ifail)

            endtime = datetime.datetime.now()
            print 'Done,all time used', endtime - begintime
            return True

    parser.print_help()

if __name__ == "__main__":

    MSG_USAGE = "%s\t%s %s\n" % ("xgo",
                                 "[-i <ip>]",
                                 "(login to dst server.)")
    MSG_USAGE += "\t\t%s %s\n" % ("[-l]",
                                  "(show all zonelist.)")
    MSG_USAGE += "\t\t%s %s %s\n" % ("[-i <ip> -I <ipfile> -z <zone>] [-c <commandline>]",
                                     "[-m] [-b -p <passwd>]",
                                     "(excute command.)")

    MSG_USAGE += "\t\t%s %s %s\n" % ("[-i <ip> -I <ipfile> -z <zone>]",
                                     "[-s < srcpath > ] [-d < dstpath > ]",
                                     "(upload file.)")
    MSG_USAGE += "\t\t%s %s %s\n" % ("[-i <ip> -I <ipfile> -z <zone>]",
                                     "[-D]  [-s < srcpath > ] [-d < dstpath > ]",
                                     "(download file.)")

    parser = optparse.OptionParser(MSG_USAGE, version=VERSION)
    parser.add_option("-c", "--commandline", dest="commandline",
                      help="commandline (e.g. \"netstat -lnpt\")")
    parser.add_option("-i", "--ip", dest="ip",
                      help="Target ip (e.g. \"120.132.32.1-25,10.10.1.21\")")
    parser.add_option("-I", "--ipf", dest="ipfile",
                      help="Target ip file path (e.g. \"/data/tools/ip.txt\")")
    parser.add_option("-z", "--zone", dest="zone",
                      help="Target zone (e.g. \"hk,th\")")
    parser.add_option("-s", "--srcpath", dest="srcpath",
                      help="src file path(e.g. \"/data/tools/1.txt\")")
    parser.add_option("-d", "--dstpath", dest="dstpath",
                      help="dst file path (e.g. \"/home/hhlyadmin/\")")
    parser.add_option("-t", "--timeout", dest="timeout",
                      help="set timeout for excuting commandline,default 60s.(e.g. \"30\")")
    parser.add_option("-n", "--threadnum", dest="threadnumber",
                      help="set work thread num,default cpu num.(e.g. \"10\")")
    parser.add_option("-m", "--needsu",
                      action="store_true", dest="bsuroot",
                      help="if need su root to excute,choose this item.")
    parser.add_option("-b", "--bpasslogin",
                      action="store_true", dest="bpasslogin",
                      help="if login with password,choose this item.")
    parser.add_option("-D", "--download",
                      action="store_true", dest="download",
                      help="if download file,choose this item.")
    parser.add_option("-l", "--listzone", dest="showzone",
                      action="store_true", help="show zone list.")
    parser.add_option("-V", "--debug", dest="debug",
                      action="store_true", help="print debug log in console.")
    parser.add_option("-p", "--sshpass", dest="sshpass",
                      help="set ssh login password,if choose this please selected '-b' item.(e.g. \"password\")")
    parser.add_option("-P", "--port", dest="sshport",
                      help="set ssh port, default 2222 port(e.g. \"2233\")")
    parser.add_option("-u", "--user", dest="sshuser",
                      help="set ssh user, default hhlyadmin port(e.g. \"xxadmin\")")

    options, _ = parser.parse_args()

    user = getpass.getuser()
    if options.debug is not None:
        ms = MangerServer(user, confpath='manager.conf')
    else:
        ms = MangerServer(user)
    ms.loadconf()
    zonenamedict, zonesdict, userdict = ms.getzonelist()

    # 登录到目标生产机
    if (options.ip is not None and
            not (options.commandline or options.srcpath or options.dstpath)):
        if ms.manger(options.ip):
            # ssh证书是否有密码,默认没有密码
            sm = ShellManger(port=int(options.sshport),username=options.sshuser)
            # sm = ShellManger(sshkeywithpass=True, 
            #                   port=int(options.sshport),
            #                   username=options.sshuser)
            sm.login(options.ip)
        else:
            print '%s %s %s, %s\n' % (user,
                                      'is not allowed login in',
                                      options.ip,
                                      'if needed, please notice admin!')
    elif options.showzone:
        print 'zone list :'
        for zone in zonesdict.keys():
            if zone in zonenamedict.keys():
                output = '%s(%s)' % (zone, zonenamedict[zone])
            else:
                output = '%s(%s)' % (zone, zone)
            print '%s--%s' % (output, zonesdict[zone])
    elif (options.ip is not None or options.ipfile is not None or
          options.zone is not None):
        # 判断是否是允许执行的用户
        if user in userdict['all']:
            todo(parser, options, zonesdict)
        else:
            print '%s %s, %s\n' % (user,
                                   'is not allowed choose function',
                                   'if needed, please notice admin!')
    else:
        parser.print_help()
