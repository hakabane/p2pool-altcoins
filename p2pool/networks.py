from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    bitcoin=math.Object(
        PARENT=networks.nets['bitcoin'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='fc70035c7a81bc6f'.decode('hex'),
        PREFIX='2472ef181efcd37b'.decode('hex'),
        P2P_PORT=9333,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=True,
        WORKER_PORT=9332,
        BOOTSTRAP_ADDRS='forre.st vps.forre.st 74.220.242.6:9334 93.97.192.93 66.90.73.83 67.83.108.0 219.84.64.174 24.167.17.248 109.74.195.142 83.211.86.49 94.23.34.145 168.7.116.243 94.174.40.189:9344 89.79.79.195 portals94.ns01.us'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool',
        VERSION_CHECK=lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v,
    ),
    bitcoin_testnet=math.Object(
        PARENT=networks.nets['bitcoin_testnet'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=60*60//10, # shares
        REAL_CHAIN_LENGTH=60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=3, # blocks
        IDENTIFIER='5fc2be2d4f0d6bfb'.decode('hex'),
        PREFIX='3f6057a15036f441'.decode('hex'),
        P2P_PORT=19333,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=19332,
        BOOTSTRAP_ADDRS='forre.st vps.forre.st liteco.in'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v,
    ),
    
    litecoin=math.Object(
        PARENT=networks.nets['litecoin'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=12, # blocks
        IDENTIFIER='e037d5b8c6923410'.decode('hex'),
        PREFIX='7208c1a53ef629b0'.decode('hex'),
        P2P_PORT=9338,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=9327,
        BOOTSTRAP_ADDRS='forre.st vps.forre.st 199.255.95.94 75.12.89.18 181.28.244.151 83.142.189.132 66.90.82.155:11332 201.57.241.77 80.222.255.91 142.68.214.29 24.52.247.82 72.230.179.177 94.127.200.29 200.204.161.215 91.121.9.7 91.235.254.37 198.154.98.195 178.79.136.10'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    litecoin_testnet=math.Object(
        PARENT=networks.nets['litecoin_testnet'],
        SHARE_PERIOD=3, # seconds
        CHAIN_LENGTH=20*60//3, # shares
        REAL_CHAIN_LENGTH=20*60//3, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=12, # blocks
        IDENTIFIER='cca5e24ec6408b1e'.decode('hex'),
        PREFIX='ad9614f6466a39cf'.decode('hex'),
        P2P_PORT=19338,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2000 - 1,
        PERSIST=False,
        WORKER_PORT=19327,
        BOOTSTRAP_ADDRS='forre.st vps.forre.st'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),

    terracoin=math.Object(
        PARENT=networks.nets['terracoin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=24*60*60//30, # shares
        REAL_CHAIN_LENGTH=24*60*60//30, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=15, # blocks
        IDENTIFIER='a41b2356a1b7d35e'.decode('hex'),
        PREFIX='5623b62178d2b8a3'.decode('hex'),
        P2P_PORT=9323,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=True,
        WORKER_PORT=9322,
        BOOTSTRAP_ADDRS='seed1.p2pool.terracoin.org seed2.p2pool.terracoin.org forre.st vps.forre.st 93.97.192.93 66.90.73.83 67.83.108.0 219.84.64.174 24.167.17.248 109.74.195.142 83.211.86.49 94.23.34.145 168.7.116.243 94.174.40.189:9344 89.79.79.195 portals94.ns01.us'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    terracoin_testnet=math.Object(
        PARENT=networks.nets['terracoin_testnet'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=60*60//30, # shares
        REAL_CHAIN_LENGTH=60*60//30, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=15, # blocks
        IDENTIFIER='b41b2356a5b7d35d'.decode('hex'),
        PREFIX='1623b92172d2b8a2'.decode('hex'),
        P2P_PORT=19323,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**32 - 1,
        PERSIST=False,
        WORKER_PORT=19322,
        BOOTSTRAP_ADDRS='seed1.p2pool.terracoin.org seed2.p2pool.terracoin.org forre.st vps.forre.st'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    feathercoin=math.Object(     
        PARENT=networks.nets['feathercoin'],
        SHARE_PERIOD=30, # seconds
        CHAIN_LENGTH=60*60//10, # shares
        REAL_CHAIN_LENGTH=60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=120, # blocks
        IDENTIFIER='4665617468657221'.decode('hex'),
        PREFIX='b131010ba6d4729a'.decode('hex'),
        P2P_PORT=19339,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=19327,
        BOOTSTRAP_ADDRS='i.hashfaster.com ftc.p2pool.skralg.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    chncoin=math.Object(
        PARENT=networks.nets['chncoin'],
        SHARE_PERIOD=15, # seconds
        CHAIN_LENGTH=12*60*60//10, # shares
        REAL_CHAIN_LENGTH=12*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=30, # blocks
        IDENTIFIER='e137d5b8c6923410'.decode('hex'),
        PREFIX='7218c1a53ef629b0'.decode('hex'),
        P2P_PORT=13389,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8800,
        BOOTSTRAP_ADDRS='chncoin.no-ip.biz pool01-cnc.coinloot.com pool04-cnc.coinloot.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    junkcoin=math.Object(
        PARENT=networks.nets['junkcoin'],
        SHARE_PERIOD=60, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=70, # shares coinbase maturity
        SPREAD=120, # blocks
        IDENTIFIER='e031F5b8c6924210'.decode('hex'),
        PREFIX='e290192ba6d4729a'.decode('hex'),
        P2P_PORT=19455,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=19327,
        BOOTSTRAP_ADDRS='jkc.sytes.net trollbox.chickenkiller.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    bbqcoin=math.Object(
        PARENT=networks.nets['bbqcoin'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=30, # blocks
        IDENTIFIER='626974636f696e21'.decode('hex'),
        PREFIX='6772696c6c697421'.decode('hex'),
        P2P_PORT=12339,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8900,
        BOOTSTRAP_ADDRS='bbq.crabdance.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    mincoin=math.Object(
        PARENT=networks.nets['mincoin'],
        SHARE_PERIOD=30, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=70, # shares coinbase maturity
        SPREAD=15, # blocks
        IDENTIFIER='6031F5b8c6924210'.decode('hex'),
        PREFIX='6290192ba6d4729a'.decode('hex'),
        P2P_PORT=8732,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=9771,
        BOOTSTRAP_ADDRS='chncoin.no-ip.biz'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    royalcoin=math.Object(
        PARENT=networks.nets['royalcoin'],
        SHARE_PERIOD=60, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=70, # shares coinbase maturity
        SPREAD=120, # blocks
        IDENTIFIER='f143F5b8c6924210'.decode('hex'),
        PREFIX='c387192ba6d4729a'.decode('hex'),
        P2P_PORT=9779,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=9771,
        BOOTSTRAP_ADDRS='chncoin.no-ip.biz'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ), 
    franko=math.Object(
        PARENT=networks.nets['franko'],
        SHARE_PERIOD=15, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=30, # blocks
        IDENTIFIER='be43F5b8c6924210'.decode('hex'),
        PREFIX='b587192ba6d4729a'.decode('hex'),
        P2P_PORT=9777,
        MIN_TARGET=0,
		MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=9777,
        BOOTSTRAP_ADDRS='chncoin.no-ip.biz'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
    digital=math.Object(
        PARENT=networks.nets['digital'],
        SHARE_PERIOD=30, # seconds target spacing
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=200, # shares coinbase maturity
        SPREAD=72, # blocks
        IDENTIFIER='a5aed03050126d6d'.decode('hex'),
        PREFIX='b6c0601991aa19a3'.decode('hex'),
        P2P_PORT=25396,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=True,
        WORKER_PORT=25397,
        BOOTSTRAP_ADDRS='pool.bounceme.net'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
