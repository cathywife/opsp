#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#
# @author: wei.yang <wei.yang@jinmuinfo.com>
# Created on 2017/06/24


import xmlrpclib 

class CobblerAPI(object):
    def __init__(self,url,user,password):
        self.cobbler_user = user
        self.cobbler_pass = password
        self.cobbler_url = url
    
    def add_system(self,hostname,ip_add,mac_add,profile,kopts):
        '''
        Add Cobbler System Infomation
        '''
        ret = {
            "result": True,
            "comment": [],
        }
        
        remote = xmlrpclib.Server(self.cobbler_url)
        token = remote.login(self.cobbler_user,self.cobbler_pass) 
        system_id = remote.new_system(token) 
        remote.modify_system(system_id,"name",hostname,token) 
        remote.modify_system(system_id,"hostname",hostname,token) 
        remote.modify_system(system_id,'modify_interface', { 
            "macaddress-eth0" : mac_add, 
            "ipaddress-eth0" : ip_add, 
            "dnsname-eth0" : hostname, 
        }, token) 
        remote.modify_system(system_id,"profile",profile,token)
        #if kopts:
        remote.modify_system(system_id,"kopts",kopts,token) 
        remote.save_system(system_id, token) 
        try:
            remote.update(token)
            remote.sync_dhcp(token)
        except Exception as e:
            ret['result'] = False
            ret['comment'].append(str(e))
        return ret
    def edit_system(self,hostname,netboot):
        '''
        Add Cobbler System Infomation
        '''
        ret = {
            "result": True,
            "comment": [],
        }
        
        remote = xmlrpclib.Server(self.cobbler_url)
        token = remote.login(self.cobbler_user,self.cobbler_pass) 
        system_id = remote.get_system_handle(hostname,token) 
        remote.modify_system(system_id,"netboot_enabled",netboot,token)        
        remote.save_system(system_id, token) 
        try:
            #remote.sync(token)
            remote.update(token)
            remote.sync_dhcp(token)
        except Exception as e:
            ret['result'] = False
            ret['comment'].append(str(e))
        return ret
        
    def del_system(self,hostname):
        '''
        Del Cobbler System Infomation
        '''
        ret = {
            "result": True,
            "comment": [],
        }
        
        remote = xmlrpclib.Server(self.cobbler_url)
        token = remote.login(self.cobbler_user,self.cobbler_pass)       
        try:
            remote.remove_system(hostname,token)
            remote.update(token)
            remote.sync_dhcp(token)
            #remote.sync(token)
        except Exception as e:
            ret['result'] = False
            ret['comment'].append(str(e))
        return ret
    def del_system_list(self,hostdict):
        '''
        Del Cobbler System Infomation from dict
        '''
        ret = {"True":[],"False":[]}
        
        remote = xmlrpclib.Server(self.cobbler_url)
        token = remote.login(self.cobbler_user,self.cobbler_pass) 
        for host in hostdict:       
            try:                              
                remote.remove_system(host["hostname"],token)
                remote.update(token)
                ret['True'].append(host["hostname"])
            except Exception as e:
                try:
                    status=remote.find_system({"hostname":host["hostname"]})  #如果system中不存在也标记删除成功
                except:
                    status = ["False"]
                if len(status)== 0:
                    ret['True'].append(host["hostname"])
                else:
                    ret['False'].append(host["hostname"])
        try:            
            remote.sync_dhcp(token)
            #remote.sync(token)
        except Exception as e:
            pass
        return ret
    def get_system(self,hostname):
        ret = {
            "result": True,
            "comment": [],
        }
        remote = xmlrpclib.Server(self.cobbler_url) 
        try:
            ret = remote.find_profile({"name":"*"})
        except Exception as e:
            ret['result'] = False
            ret['comment'].append(str(e))
        return ret
    
    def get_proflies(self):
        '''
        get cobbler profiles
        '''
        ret = {
            "result": True,
            "comment": [],
        }
        remote = xmlrpclib.Server(self.cobbler_url)
        try:
            profiles_list=remote.get_profiles()
            profiles=[]
            for profile in profiles_list:
                if profile['enable_menu'] == 1:
                    profiles.append(profile['name'])
            ret = profiles
        except Exception as e:
            ret['result'] = False
            ret['comment'].append(str(e))
        return ret