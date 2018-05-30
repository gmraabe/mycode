#!/usr/bin/env python3
# cisco_parser.pp
# Micah Raabe

# Lab 50 - Cisco Conf Parse

from ciscoconfparse import CiscoConfParse

def standardize_intfs(parse):

    ## Search all switch interfaces and modify them
    #
    # r'^interface.+?thernet' is a regular expression, for ethernet intfs
    for intf in parse.find_objects(r'^interface.+?thernet'):

        has_stormcontrol = intf.has_child_with(r' storm-control broadcast')
        is_switchport_access = intf.has_child_with(r'switchport mode access')
        is_switchport_trunk = intf.has_child_with(r'switchport mode trunk')

        ## Add missing features
        if is_switchport_access and (not has_stormcontrol):
            intf.append_to_family(' storm-control action trap')
            intf.append_to_family(' storm-control broadcast level 0.4 0.3')

        ## Remove dot1q trunk misconfiguration...
        elif is_switchport_trunk:
            intf.delete_children_matching('port-security')

## Parse the config
parse = CiscoConfParse('ios_audit.conf') # this is our input file

## Search and standardize the interfaces...
standardize_intfs(parse)
parse.commit()     # commit() **must** be called before searching again

## regular expression usage in has_line_with() to find if the config has a matching line
if not parse.has_line_with(r'^service\stimestamp'):
    ## prepend_line() adds a line at the top of the configuration
    parse.prepend_line('service timestamps debug datetime msec localtime show-timezone')
    parse.prepend_line('service timestamps log datetime msec localtime show-timezone')

## Write the new configuration
parse.save_as('ios_audit.conf.new')
