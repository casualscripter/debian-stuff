#!/usr/bin/env python2
#===============================================================================
# DIRECTORY:
#   /usr/local/bin
#
# FILE:
#   print_plist_entry.py
#
# USAGE:
#   print_plist_entry.py <plist> <key>
#
# OPTIONS:
#   none
#
# DESCRIPTION:
#   Prints key-value pair of key in plist
#
# REQUIREMENTS:
#   python2,...
#
# BUGS:
#   ---
#
# NOTES:
#   Tested on:
#   - Debian 8 and
#   - OS X 10.11.4
#
# AUTHOR:
#   Patrick Neumann, patrick@neumannsland.de
#
# COMPANY:
#   (privately)
#
# VERSION:
#   0.9 (beta)
#
# LINK TO THE MOST CURRENT VERSIONS:
#   https://raw.githubusercontent.com/casualscripter/debian-stuff/master/print_plist_entry.py
#
# CREATED:
#   23.03.2016
#
# COPYRIGHT (C):
#   2015-2016 - Patrick Neumann
#
# LICENSE:
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
# WARRANTY:
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# TODO:
#   ---
#
# HISTORY:
#   0.9 - Patrick Neumann - Initial (public) release
#
#===============================================================================

import os.path
import plistlib
import sys

# short help for new users
def usage():
  print "\nUsage: python print_plist_entry.py <plist> <key>\n"
  print "  (use the <key> \"ALL\" to list all entries.)\n"

# check for first parameter
try:
  plist = sys.argv[1]
except IndexError:
  print "\nError: No <plist> (file) given!"
  usage()
  sys.exit( 1 )

# check if first parameter is a file
if not os.path.isfile( plist ):
  print "\nError: plist (file) does not exist!\n"
  sys.exit( 1 )

# check for second parameter
try:
  key = sys.argv[2]
except IndexError:
  print "\nError: No <key> (string) given!"
  usage()
  sys.exit( 1 )

# plist has to be a XML file
try:
  content = plistlib.readPlist( plist )
except:
  print "\nError: plist is not a XML file!\n"
  sys.exit( 1 )

# simple function (incl. iteration)
def print_entry( c ):
  for k, v in c.iteritems():
    if isinstance( v, dict ):
      print_entry( v )
    else:
      if key == "ALL":
        try:
          print "{0}: {1}".format( k, v ) 
        except UnicodeEncodeError:
          print "{0}: {1}".format( k, v.encode( "utf-8" ) )
      else:
        if k == key:
          try:
            print "{0}: {1}".format( k, v ) 
          except UnicodeEncodeError:
            print "{0}: {1}".format( k, v.encode( "utf-8" ) )

# the wonder
print_entry( content )

sys.exit( 0 )
