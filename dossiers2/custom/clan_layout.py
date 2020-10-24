# uncompyle6 version 3.7.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)]
# Embedded file name: scripts/common/dossiers2/custom/clan_layout.py
from dossiers2.common.DossierBlockBuilders import *
_rareAchievementsBlockBuilder = ListBlockBuilder('rareAchievements', 'I', {})
clanDossierLayout = (
 _rareAchievementsBlockBuilder,)
CLAN_DOSSIER_LIST_BLOCKS = [ b.name for b in clanDossierLayout if type(b) == ListBlockBuilder ]