schedulers = []

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.schedulers.forcesched import ForceScheduler, FixedParameter, ChoiceStringParameter

from metabbotcfg import builders
from metabbotcfg.debian import schedulers as deb_schedulers

schedulers.append(SingleBranchScheduler(name="all", branch='master',
                                 treeStableTimer=2,
                                 builderNames=[ b['name'] for b in builders.builders ]))

#schedulers.append(SingleBranchScheduler(name="release", branch='buildbot-0.8.9',
#                                 treeStableTimer=10,
#                                 builderNames=[ b['name'] for b in builders.builders if b['name'] not in ('docs',) ]))

schedulers.append(ForceScheduler(name="force",
    repository=FixedParameter(name="repository", default='git://github.com/buildbot/buildbot.git'),
    branch=ChoiceStringParameter(name="branch", default="master", choices=["master", "eight"]),
    project=FixedParameter(name="project", default=""),
    properties=[],
    builderNames=[ b['name'] for b in builders.builders ]))

schedulers += deb_schedulers
