# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

import os
import sys
import glob
import time
import types
import logging
import argparse
import xml.etree.ElementTree as ET

import PETRglobals  # global variables
import PETRreader_ud  # input routines
import PETRreader
import PETRreader_old
import PETRwriter
import utilities
import PETRtree

def main():

    cli_args = parse_cli_args()
    utilities.init_logger('PETRARCH.log')
    logger = logging.getLogger('petr_log')

    PETRglobals.RunTimeString = time.asctime()


    if cli_args.command_name == 'parse' or cli_args.command_name == 'batch':

        if cli_args.config:
            print('Using user-specified config: {}'.format(cli_args.config))
            logger.info(
                'Using user-specified config: {}'.format(cli_args.config))
            PETRreader.parse_Config(cli_args.config)
        else:
            logger.info('Using default config file.')
            PETRreader.parse_Config(utilities._get_data('data/config/',
                                                        'PETR_config.ini'))

        read_dictionaries()
        start_time = time.time()
        print('\n\n')
        '''
        paths = PETRglobals.TextFileList
        if cli_args.inputs:
            if os.path.isdir(cli_args.inputs):
                if cli_args.inputs[-1] != '/':
                    paths = glob.glob(cli_args.inputs + '/*.xml')
                else:
                    paths = glob.glob(cli_args.inputs + '*.xml')
            elif os.path.isfile(cli_args.inputs):
                paths = [cli_args.inputs]
            else:
                print(
                    '\nFatal runtime error:\n"' +
                    cli_args.inputs +
                    '" could not be located\nPlease enter a valid directory or file of source texts.')
                sys.exit()
        
        out = "" #PETRglobals.EventFileName
        if cli_args.outputs:
                out = cli_args.outputs
             
        if cli_args.command_name == 'parse':
            run(paths, out, cli_args.parsed)

        else:
            run(paths, out , True)  ## <===

        print("Coding time:", time.time() - start_time)

    print("Finished")
	'''

def parse_cli_args():
    """Function to parse the command-line arguments for PETRARCH."""
    __description__ = """
PETRARCH
(https://openeventdata.github.io/) (v. 0.01)
    """
    aparse = argparse.ArgumentParser(prog='petrarch',
                                     description=__description__)

    sub_parse = aparse.add_subparsers(dest='command_name')
    parse_command = sub_parse.add_parser('parse', help=""" DEPRECATED Command to run the
                                         PETRARCH parser. Do not use unless you've used it before. If you need to 
                                         process unparsed text, see the README""",
                                         description="""DEPRECATED Command to run the
                                         PETRARCH parser. Do not use unless you've used it before.If you need to 
                                         process unparsed text, see the README""")
    parse_command.add_argument('-i', '--inputs',
                               help='File, or directory of files, to parse.',
                               required=True)
    parse_command.add_argument('-P', '--parsed', action='store_true',
                               default=False, help="""Whether the input
                               document contains StanfordNLP-parsed text.""")
    parse_command.add_argument('-o', '--output',
                               help='File to write parsed events.',
                               required=True)
    parse_command.add_argument('-c', '--config',
                               help="""Filepath for the PETRARCH configuration
                               file. Defaults to PETR_config.ini""",
                               required=False)
    
    
    batch_command = sub_parse.add_parser('batch', help="""Command to run a batch
                                         process from parsed files specified by
                                         an optional config file.""",
                                         description="""Command to run a batch
                                         process from parsed files specified by
                                         an optional config file.""")
    batch_command.add_argument('-c', '--config',
                               help="""Filepath for the PETRARCH configuration
                               file. Defaults to PETR_config.ini""",
                               required=False)
                               
    batch_command.add_argument('-i', '--inputs',
                               help="""Filepath for the input XML file. Defaults to 
                               data/text/Gigaword.sample.PETR.xml""",
                               required=False)
                               
    batch_command.add_argument('-o', '--outputs',
                               help="""Filepath for the input XML file. Defaults to 
                               data/text/Gigaword.sample.PETR.xml""",
                               required=False)

    args = aparse.parse_args()
    return args

    
def read_dictionaries(validation=False):

    #'''
    print('Verb dictionary:', PETRglobals.VerbFileName)
    verb_path = utilities._get_data(
        'data/dictionaries',
        PETRglobals.VerbFileName)
    PETRreader.read_verb_dictionary(verb_path)

    #for key,value in PETRglobals.VerbDict['phrases']['ENTER']['NAVY']['*'].items():
    for key,value in PETRglobals.VerbDict['phrases']['RAISE']['*'].items():
    #for key,value in PETRglobals.VerbDict['phrases']['ALERT']['*'].items():#['SECURITY']['|']['OVER']['-'].items():
        print(key)
        print(value)
    #print(PETRglobals.VerbDict['phrases']['ALERT']['*'])
    #print(PETRglobals.VerbDict['phrases']['REFUSE']['HUNGER-STRIKER']['*']['NUTRITION'][','])
    #print(PETRglobals.VerbDict['phrases']['PHYSICAL_CONFLICT']['*']['AT'])
    #print(PETRglobals.VerbDict['phrases']['EXPLOSIVE_DESTRUCTION']['MACHINE'][',']['WEAPON'])
    #print(PETRglobals.VerbDict['phrases']['DRAFT']['*']['REINFORCEMENT'])
    #print(PETRglobals.VerbDict['verbs']['OUTLINE'])

    #'''   
    '''    
    print('Actor dictionaries:', PETRglobals.ActorFileList)
    for actdict in PETRglobals.ActorFileList:
        actor_path = utilities._get_data('data/dictionaries', actdict)
        PETRreader.read_actor_dictionary(actor_path)'''

    #PETRreader.read_actor_dictionary('/users/ljwinnie/Desktop/petrarch2/petrarch/petrarch2/petrarch2/data/dictionaries/Phoenix.Countries.actors.txt') #actor_dict_test.txt')
    #print(len(PETRglobals.ActorDict))
    #print(PETRglobals.ActorDict.get("UFFE"))
    #print(PETRglobals.ActorDict.get("MURATBEK"))
    #print(PETRglobals.ActorDict.get("GERMANY"))
    #print(PETRglobals.ActorDict.get("TUNISIAN"))

    '''
    print('Agent dictionary:', PETRglobals.AgentFileName)
    agent_path = utilities._get_data('data/dictionaries',
                                     PETRglobals.AgentFileName)
    PETRreader.read_agent_dictionary(agent_path)

    print('Discard dictionary:', PETRglobals.DiscardFileName)
    discard_path = utilities._get_data('data/dictionaries',
                                       PETRglobals.DiscardFileName)
    PETRreader.read_discard_list(discard_path)

    if PETRglobals.IssueFileName != "":
        print('Issues dictionary:', PETRglobals.IssueFileName)
        issue_path = utilities._get_data('data/dictionaries',
                                         PETRglobals.IssueFileName)
        PETRreader.read_issue_list(issue_path)
    '''

def run(filepaths, out_file, s_parsed):
    # this is the routine called from main()
    events = PETRreader.read_xml_input(filepaths, s_parsed)
    if not s_parsed:
        events = utilities.stanford_parse(events)
    updated_events = do_coding(events, out_file)
    PETRwriter.write_events(updated_events, 'evts.' + out_file)
    
if __name__ == '__main__':
    main()
