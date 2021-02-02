import discord 
from discord.ext import commands
import json
import embeds

class Staff(commands.Cog):
    def __init__(self, client):
        with open(r"C:\Users\Bailey\Documents\Programs\Nexus\nexus-bot\servers.json") as f:
            data=json.load(f)
        arl_helper=[765588833181106177, 740768860273377342, 740768665145966702, 739742785178959883, 635413949940236301, 704635627890540646, 712312250513489980]
        rl_sec=[712312463722545254, 660345011472302101, 741380973991690250, 622559732833583104, 675690340614668311, 635413949759619082, 635413945624166417, 739743084337823804, 741201475509813311, 739600725914681354, 739736106622255215, 740768341068611627, 740766560347750421, 561442281492578313, 561468399083978763, 765588833181106178, 765588833181106180]
        hrl_off=[777665314800009266, 765588833181106181, 592145305252921346, 591027955355090965, 740764452877762612, 740761925713133673, 739724272171483208, 739749891747741706, 635413945074843648, 635413947314601994, 669629906707021825, 769946380885688330, 700599202337652806, 660345394026381312]
        devs=[687427792735961144, 741777167867707504, 551217293087080448, 643145196002869329, 739592756820836403, 740766137951715358, 765588833190150144]
        admin_mod=[699890121473785856, 660345573957828619, 660345720792023043, 706174498956640327, 622564706183413761, 309110175300583451, 528069029521391628, 635413943791255615, 739750940394913812, 739759423664160860, 739957900562268210, 602415504891576341, 765588833181106183, 765588833190150146]
        self.arl_helper=arl_helper
        self.rl_sec=rl_sec
        self.hrl_off=hrl_off
        self.devs=devs
        self.admin_mod=admin_mod
        self.data = data
        self.client=client
        print('exchange started')

    async def update(self, member):
        exchange=self.client.get_guild(694841846794289242)
        if member.guild.id == 694841846794289242:
            for g in self.client.guilds:
                if member in g.get_all_members():
                    server_roles=data[g.name]["roles"]
                    for r in server_roles:
                        role=g.get_role(r)
                        if role in member.roles:
                            if role.id in self.arl_helper:
                                role=exchange.get_role(694841846811197469)
                            elif role.id in self.rl_sec:
                                role=exchange.get_role(694841846823911434)
                            elif role.id in self.hrl_off:
                                role=exchange.get_role(694841846823911439)
                            elif role.id in self.devs:
                                role=exchange.get_role(724514718689263649)       
                            elif role.id in self.admin_mod:       
                                role=exchange.get_role(698225101853687818)                         
                            else:
                                role=exchange.get_role(739709639012122647)
                            in_exchange=exchange.get_member(member.id)
                            try:
                                in_exchange.add_roles(role, reason='Verification',atomic=True)
                                embed=embeds.verify_ex_em(member.guild)
                                await member.send("Welcome!", embed=embed)
                            except discord.Forbidden:
                                print('Forbidden')
                        else:
                            pass
                else:
                    pass
        #elif member.guild.id==699852946363514902:
        #    ob=self.client.get_guild(798525391308193812)
        #    blist=self.client.get_guild(699852946363514902)
        #    print('got servers')
        #    if member in ob.members:
        #        testr=ob.get_role(801178473979969547)
        #        ob_mem = ob.get_member(member.id)
        #        print('got test role and ob mem')
        #        if testr in ob_mem.roles:
        #            blist_role=blist.get_role(699890121473785856)
        #            print('attempting to add role')
        #            await member.add_roles(blist_role)
        #            embed=embeds.verify_ex_em(member.guild)
        #            await member.send("Welcome!", embed=embed)


    @commands.Cog.listener()
    async def on_member_join(self, member):
        print('member joined')
        if member.guild.id==694841846794289242: #or member.guild.id==699852946363514902:
            print('calling function')
            await self.update(member)

def setup(client):
    client.add_cog(Staff(client))