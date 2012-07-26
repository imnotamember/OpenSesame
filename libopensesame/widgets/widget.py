#-*- coding:utf-8 -*-

"""
This file is part of openexp.

openexp is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

openexp is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with openexp.  If not, see <http://www.gnu.org/licenses/>.
"""

class widget:

	"""The base class for all other widgets"""

	def __init__(self, form):
	
		"""<DOC>
		Constructor
		
		Arguments:
		form -- the parent form
		</DOC>"""
	
		self.type = 'widget'
		self.form = form
		self.rect = None
		self.focus = False
		self.var = None
		
	def draw_frame(self, rect=None, color=None, penwidth=None):
	
		"""<DOC>
		Draws a simple frame around the widget
		
		Keyword arguments:
		rect -- a (left, top, width, height) tuple for the frame geometry or
				None to use the widget geometry (default=None)
		color -- frame color or None to use experiment default (default=None)
		penwidth -- frame width or None to use experiment default
					(default=None)		
		</DOC>"""
	
		pw = self.form.canvas.penwidth
		if penwidth != None:
			self.form.canvas.set_penwidth(penwidth)
		if rect == None:
			rect = self.rect
		x, y, w, h = rect
		self.form.canvas.rect(x, y, w, h, color=color)
		self.form.canvas.set_penwidth(pw)				
								
	def on_mouse_click(self, pos):
	
		"""<DOC>
		Is called whenever the user clicks on the widget
		
		Arguments:
		pos -- an (x, y) tuple		
		</DOC>"""
				
	def render(self):
	
		"""<DOC>
		Draws the widget
		</DOC>"""
	
		if self.focus:
			self.draw_frame(self.rect, penwidth=4)	
		else:
			self.draw_frame(self.rect)	
		
	def set_rect(self, rect):
	
		"""<DOC>
		Sets the widget geometry
		
		Arguments:
		rect -- a (left, top, width, height) tuple
		</DOC>"""
			
		self.rect = rect
		
	def set_var(self, val, var=None):
	
		"""<DOC>
		Set an experimental variable
		
		Arguments:
		val -- a value
		
		Keyword arguments:
		var -- a variable name, or None to use widget default (default=None)		
		</DOC>"""
		
		if var == None:
			var = self.var
		if var == None:
			return
		self.form.experiment.set(var, val)