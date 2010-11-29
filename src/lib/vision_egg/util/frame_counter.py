__copyright__ = """ Copyright (c) 2010 Torsten Schmits

This program is free software; you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation; either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.
"""

from threading import Thread

import pygame

class FrameCounter(Thread):
    """ Runs a thread that calls flip() repeatedly, which waits for
    vsync and thus indicates real display redraws. """
    def __init__(self, flag):
        Thread.__init__(self)
        self._flag = flag
        self.frame = 0
        self._locked_frame = 0
        
    def run(self):
        while self._flag:
            pygame.display.flip()
            self.frame += 1

    def lock(self):
        self._locked_frame = self.frame

    @property
    def last_interval(self):
        return self.frame - self._locked_frame
