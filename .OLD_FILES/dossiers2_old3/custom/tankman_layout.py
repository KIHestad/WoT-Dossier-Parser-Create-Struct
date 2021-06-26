# uncompyle6 version 3.7.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)]
# Embedded file name: scripts/common/dossiers2/custom/tankman_layout.py
from dossiers2.common.DossierBlockBuilders import *
_tmanTotalBlockLayout = [
 'battlesCount']
_tmanTotalBlockBuilder = StaticSizeBlockBuilder('total', _tmanTotalBlockLayout, {}, [])
TMAN_ACHIEVEMENTS_BLOCK_LAYOUT = [
 'warrior',
 'invader',
 'sniper',
 'defender',
 'steelwall',
 'supporter',
 'scout',
 'evileye',
 'medalWittmann',
 'medalOrlik',
 'medalOskin',
 'medalHalonen',
 'medalBurda',
 'medalBillotte',
 'medalKolobanov',
 'medalFadin',
 'medalRadleyWalters',
 'medalBrunoPietro',
 'medalTarczay',
 'medalPascucci',
 'medalDumitru',
 'medalLehvaslaiho',
 'medalNikolas',
 'medalLafayettePool',
 'heroesOfRassenay',
 'medalDeLanglade',
 'medalTamadaYoshio',
 'huntsman',
 'sniper2',
 'mainGun']
_tankmanAchievementsBlockBuilder = StaticSizeBlockBuilder('achievements', TMAN_ACHIEVEMENTS_BLOCK_LAYOUT, {}, [])
tmanDossierLayout = (
 _tmanTotalBlockBuilder, _tankmanAchievementsBlockBuilder)