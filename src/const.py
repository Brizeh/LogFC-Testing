import pickle

BIG = 10**20
all_bosses = []
all_mvp = []
all_lvp = []

boss_dict = {
    15438 : "vg",
    15429 : "gors",
    15375 : "sab",
    
    16123 : "sloth",
    16115 : "matt",
    
    16253 : "esc",
    16235 : "kc",
    16246 : "xera",
    
    17194 : "cairn",
    17172 : "mo",
    17188 : "sam",
    17154 : "dei",
    
    19767 : "sh",
    19450 : "dhuum",
    
    43974 : "ca",
    21105 : "twins",
    20934 : "qadim",
    
    22006 : "adina",
    21964 : "sabir",
    22000 : "qpeer",
    
    16199 : "golem"}

with open('wingman_updater/all_times_nm.pickle', 'rb') as f:  # Python 3: open(..., 'rb')
    nm_dict = pickle.load(f)
    
with open('wingman_updater/all_times_cm.pickle', 'rb') as f:  # Python 3: open(..., 'rb')
    cm_dict = pickle.load(f)
    
emote_wingman = ":wing:"

################################ DATA VG ################################



################################ DATA GORS ################################



################################ DATA SABETHA ################################

pos_sab = [376.7,364.4]
pos_canon1 = [346.9,706.7]
pos_canon2 = [35.9,336.8]
pos_canon3 = [403.3,36.0]
pos_canon4 = [713.9,403.1] 

canon_detect_radius = 45

################################ DATA SLOTH ################################



################################ DATA MATTHIAS ################################



################################ DATA ESCORT ################################



################################ DATA KC ################################



################################ DATA XERA ################################

xera_debut = [497.1,86.4]
xera_l1 = [663.0,314.9]
xera_l2 = [532.5,557.4]
xera_fin = [268.3,586.4]
xera_r1 = [208.2,103.4]
xera_r2 = [87.0,346.8]
xera_centre = [366.4,323.4]

xera_debut_radius = 85
xera_centre_radius = 140

################################ DATA CAIRN ################################



################################ DATA MO ################################



################################ DATA SAMAROG ################################

sama_top_left_corn = [278.0,645.2]
sama_top_right_corn = [667.6,660.7]
sama_bot_left_corn = [299.4,58.6]
sama_bot_right_corn = [690.7,73.6]

################################ DATA DEIMOS ################################



################################ DATA SH ################################



################################ DATA DHUUM ################################



################################ DATA CA ################################



################################ DATA LARGOS ################################



################################ DATA QADIM ################################

qadim_center = [411.5,431.1]
qadim_fdp_radius = 70

################################ DATA ADINA ################################



################################ DATA SABIR ################################



################################ DATA QTP ################################