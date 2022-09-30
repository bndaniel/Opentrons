{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Italic;\f1\fnil\fcharset0 Menlo-Regular;\f2\fnil\fcharset0 Menlo-Bold;
}
{\colortbl;\red255\green255\blue255;\red83\green83\blue83;\red234\green234\blue234;\red47\green51\blue57;
\red38\green38\blue38;\red8\green83\blue255;\red14\green14\blue14;\red0\green0\blue255;\red18\green126\blue114;
\red47\green51\blue57;\red234\green234\blue234;\red18\green126\blue114;\red8\green83\blue255;}
{\*\expandedcolortbl;;\cssrgb\c40000\c40000\c40000;\cssrgb\c93333\c93333\c93333;\cssrgb\c24314\c26275\c28627;
\cssrgb\c20000\c20000\c20000;\cssrgb\c0\c43529\c100000;\cssrgb\c6667\c6667\c6667;\cssrgb\c0\c0\c100000;\cssrgb\c1569\c56078\c52157;
\cssrgb\c24314\c26275\c28627;\cssrgb\c93333\c93333\c93333;\cssrgb\c1569\c56078\c52157;\cssrgb\c0\c43529\c100000;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\i\fs21\fsmilli10800 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # metadata
\f1\i0 \cf4 \strokec4 \
metadata \cf5 \strokec5 =\cf4 \strokec4  \{\
    \cf6 \strokec6 'protocolName'\cf4 \strokec4 : \cf6 \strokec6 'My Protocol'\cf4 \strokec4 ,\
    \cf6 \strokec6 'author'\cf4 \strokec4 : \cf6 \strokec6 'Name <opentrons@example.com>'\cf4 \strokec4 ,\
    \cf6 \strokec6 'description'\cf4 \strokec4 : \cf6 \strokec6 'Simple protocol to get started using the OT-2'\cf4 \strokec4 ,\
    \cf6 \strokec6 'apiLevel'\cf4 \strokec4 : \cf6 \strokec6 '2.13'\cf4 \strokec4 \
\}\
\

\f0\i \cf2 \strokec2 # protocol run function
\f1\i0 \cf4 \strokec4 \
\pard\pardeftab720\partightenfactor0

\f2\b \cf7 \strokec7 def
\f1\b0 \cf4 \strokec4  \cf8 \strokec8 run\cf4 \strokec4 (protocol: protocol_api\cf5 \strokec5 .\cf4 \strokec4 ProtocolContext):\
\
    
\f0\i \cf2 \strokec2 # labware
\f1\i0 \cf4 \strokec4 \
    plate \cf5 \strokec5 =\cf4 \strokec4  protocol\cf5 \strokec5 .\cf4 \strokec4 load_labware(\cf6 \strokec6 'corning_96_wellplate_360ul_flat'\cf4 \strokec4 , location\cf5 \strokec5 =\cf6 \strokec6 '1'\cf4 \strokec4 )\
    tiprack \cf5 \strokec5 =\cf4 \strokec4  protocol\cf5 \strokec5 .\cf4 \strokec4 load_labware(\cf6 \strokec6 'opentrons_96_tiprack_300ul'\cf4 \strokec4 , location\cf5 \strokec5 =\cf6 \strokec6 '2'\cf4 \strokec4 )\
\
    
\f0\i \cf2 \strokec2 # pipettes
\f1\i0 \cf4 \strokec4 \
    left_pipette \cf5 \strokec5 =\cf4 \strokec4  protocol\cf5 \strokec5 .\cf4 \strokec4 load_instrument(\
         \cf6 \strokec6 'p300_single'\cf4 \strokec4 , mount\cf5 \strokec5 =\cf6 \strokec6 'left'\cf4 \strokec4 , tip_racks\cf5 \strokec5 =\cf4 \strokec4 [tiprack])\
\
    
\f0\i \cf2 \strokec2 # commands
\f1\i0 \cf4 \strokec4 \
    left_pipette\cf5 \strokec5 .\cf4 \strokec4 pick_up_tip()\
    left_pipette\cf5 \strokec5 .\cf4 \strokec4 aspirate(\cf9 \strokec9 30\cf4 \strokec4 , plate[\cf6 \strokec6 'A1'\cf4 \strokec4 ])\
    left_pipette\cf5 \strokec5 .\cf4 \strokec4 dispense(\cf9 \strokec9 30\cf4 \strokec4 , plate[\cf6 \strokec6 'B1\'92\cf4 \strokec4 ])	\
    
\fs21\fsmilli10800 \cf10 \cb11 \outl0\strokewidth0 left_pipette\cf5 .\cf10 aspirate(\cf12 30\cf10 , plate[\cf13 'A1'\cf10 ])\
\pard\pardeftab720\partightenfactor0
\cf10     left_pipette\cf5 .\cf10 dispense(\cf12 30\cf10 , plate[\cf13 'B1\'92\cf10 ])
\fs21\fsmilli10800 \cf4 \cb3 \outl0\strokewidth0 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf4     left_pipette\cf5 \strokec5 .\cf4 \strokec4 drop_tip()\
\
\
}