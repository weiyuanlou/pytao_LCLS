from lcls_live.datamaps import get_datamaps
from lcls_live.archiver import lcls_archiver_restore
from lcls_live.tools import isotime

import matplotlib.pyplot as plt
import numpy as np

import os

from pytao import Tao
import pandas as pd

from copy import deepcopy

import epics
from epics import caget_many, caget
from time import sleep, time

def get_DM_GOOD(tao, MODEL):

    def ele_info(ele):
        dat = tao.ele_head(ele)
        dat.update(tao.ele_gen_attribs(ele))
        return dat

    def ele_table(match="*"):
        ix_ele = tao.lat_list(match, "ele.ix_ele", flags="-no_slaves")
        dat = list(map(ele_info, ix_ele))
        df = pd.DataFrame(dat, index=ix_ele)
        df.L.fillna(0, inplace=True)
        df['s_center'] = df['s'] - df['L']/2
        df['s_beginning'] = df['s'] - df['L']
        return  df

    df = ele_table()

    # Elements with device names
    devices = df[df['alias'] != '']
   

    def filter_datamap(dm, bmad_names):
        bnames = dm.data['bmad_name'] 
        bmad_names = set(bmad_names)
        ix = bnames[[name in bmad_names for name in bnames]].index
        dm2 = deepcopy(dm)
        dm2.data = dm.data.loc[ix]
        return dm2    
    
    
    DM0 = get_datamaps(MODEL)
    
      
    good_names = set(df['name'])
    bad_eles = [] # any bad eles

    for ele in bad_eles:
        good_names.remove(ele)

    DM = {}
    for name, dm in DM0.items():
        if name == 'tao_energy_measurements':
            # don't filter
            #DM[name] = dm
            pass
        else:
            DM[name] = filter_datamap(dm, good_names)    
    
    
    # datamaps to exclude
    ######################
    DENYLIST = ['correctors']
    #DENYLIST = ['bpms', 'cavities', 'correctors','quad']
    
    PVLIST =  []
    for name, dm in DM.items():
        if name in DENYLIST:
            continue
        PVLIST.extend(dm.pvlist)
    PVLIST = list(set(PVLIST))
    #######################
    
    
    # Identify bad PVs with readback value = None
    ########################
    PVDATA = caget_dict(PVLIST)
    BAD_DEVICES = set()
    PVLIST_GOOD = []

    for k, v in PVDATA.items():
        if v is None:
            print('Bad PV:', k)
            device = ':'.join((k.split(':')[:-1]))
            BAD_DEVICES.add(device)
        else:
            PVLIST_GOOD.append(k)

    # Get bmad names
    bdf = devices[['alias', 'name']].set_index('alias')
    BAD_NAMES = list(bdf.loc[list(BAD_DEVICES)]['name'])
    
    MONITOR = {pvname:epics.PV(pvname) for pvname in PVLIST_GOOD}
    #########################

    
    # Filter DM again to exclude bad PVs
    ##############################
    for name in BAD_NAMES:
        good_names.remove(name)
    
    DM_GOOD = {}
    for name, dm in DM.items():
        if name == 'tao_energy_measurements':
            # don't filter
            DM_GOOD[name] = dm
        else:
            DM_GOOD[name] = filter_datamap(dm, good_names)    
    ##############################
    
    #def save_cmds(cmds, filename='cmds.tao'): # Write to file for running with vanilla Tao
    #    with open(filename, 'w') as f:
    #        f.write('set global lattice_calc_on = F\n')
    #        f.write('set global plot_on = F\n')    
    #        for cmd in CMDS:
    #            f.write(cmd+'\n')
    #        f.write('set global lattice_calc_on = T\n')        
    #        f.write('set global plot_on = T\n')      
    
    return MONITOR, DM_GOOD


def caget_dict(pvlist):
    return dict(zip(pvlist, caget_many(pvlist)))

# Match HTR to design
def set_htr_twiss(tao):
    cmds="""
vv
vd
use dat HTR.midtwiss[1:4]
use var begtwiss[1:4]
olmdif
""".split('\n') 
    tao.cmds(cmds)
    tao.cmd('set global lattice_calc_on = T')
    tao.cmd('run')
    #tao.cmd('set global plot_on = T')
    
    
def get_pvdata(MONITOR):   
    itime = isotime()
    pvdata =  {k:MONITOR[k].get() for k in MONITOR}
    return pvdata

def tao_commands(pvdata, DM_GOOD):
    cmds = []
    for name, dm in DM_GOOD.items():
        cmds.extend(dm.as_tao(pvdata))
    return cmds


def run1(tao, MONITOR, DM_GOOD):
    #sleep(.001)
    t1 = time()
    pvdata = get_pvdata(MONITOR)
    cmds = tao_commands(pvdata, DM_GOOD)
    
    #cmds.append('set ele CAVL011 phi0 = 0.0') # CHEATING
    
    #tao.cmd('set global plot_on = F')
    tao.cmd('set global lattice_calc_on = F')
    tao.cmds(cmds); # Apply


    tao.cmd('set global lattice_calc_on = T')
    #tao.cmd('set global plot_on = T')
    #toggle_beam()
    
    dt = time()-t1
    print("Updating Bmad live model took (sec):",  dt)   
