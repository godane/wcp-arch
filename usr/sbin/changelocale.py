#!/usr/bin/env python
#
# Program to install Wolvix to hard disk
#
# License:	GNU General Public license
# Author: 	Chris Gallienne
#
# Note: This script was wholly written by me, but I have lifted ideas
# from various other installer shell scripts, principally the following:
#
# DamnSmallLinux dsl-hdinstall script, which was itself a modification 
# of the KNOPPIX knx-hdinstall 0.37 by Christian Perle; the knoppix
# scripts 'knoppix-installer' by Fabian Franz and 'mkboot' by Guy Maor;
# and the 'slax-installer' scripts by Thomas Matejicek. Thomas' slax-liloconfig
# shell script has been translated almost in its entirety and adapted here
# as the function 'lilo_config'. Thanks, Thomas!
#

import pygtk
pygtk.require('2.0')
import gtk, gobject, os, sys, time

def change_locale(data=None):
	
	def close_window (self):
		window.destroy()
	
	def locale_change (self):
		file = open ('/etc/profile.d/lang.sh')
		lang = file.read()
		file.close()
		os.unlink("/etc/profile.d/lang.sh")
		file = open("/etc/profile.d/lang.sh", 'w')
		lines = lang.split("\n", sys.maxint)
		for line in lines:
			word = line.split(None, sys.maxint)
			if word.count('export'):
				phrase = word[1].split("=", sys.maxint)
				print "Found export line; phrase = %s" %phrase
				if phrase.count('LANG'):
					line = "export LANG=%s" %localesel.get_active_text()
					print "Changing line to %s" %line
					file.write("%s\n" % line)
					line = "export LANGUAGE=%s" %localesel.get_active_text()
					file.write("%s\n" % line)
					line = "export LINGUAS=%s" %localesel.get_active_text()
					file.write("%s\n" % line)
					line = "export LC_ALL=%s" %localesel.get_active_text()
					file.write("%s\n" % line)
				else:
					file.write("%s\n" % line)
			else:
				file.write("%s\n" % line)
		file.close()
		message = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK,
			"Locale has been changed")
		resp = message.run()
		message.destroy()
		close_window(self)
			
	window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        #window.set_size_request(380, 380)
        window.set_position(gtk.WIN_POS_CENTER)
        window.set_resizable(True)

        window.connect("destroy", close_window)
        window.set_title("Wolvix - Locale Setup")
        window.set_border_width(10)

        mainbox = gtk.VBox(False, 10)
        topbox = gtk.HBox(False, 10)
	leftbox = gtk.VBox(False, 10)
	rightbox = gtk.VBox(False, 10)
	bottombox = gtk.HBox(False, 10)
	image = gtk.Image()
        image.set_from_file("/usr/share/pixmaps/wolvix-menu.png")
        leftbox.pack_start(image, False, False, 10)
        image.show()
               
        label1 = gtk.Label("Select locale:")
        label1.set_line_wrap(True)
        localesel = gtk.combo_box_new_text()
        localesel.set_size_request(120, 30)
	os.system("locale -a >/tmp/locale.txt")
	file = open('/tmp/locale.txt')
	locales = file.read()
	file.close()
	lines = locales.split("\n", sys.maxint)
	for line in lines:
		localesel.append_text(line)
	localesel.set_active(34)
	rightbox.pack_start(label1, False, False, 10)
        rightbox.pack_start(localesel, False, False, 10)
        button2 = gtk.Button("Change")
        button2.set_size_request(120, 30)
        button2.connect("clicked", locale_change)
        bottombox.pack_start(button2, True, False, 10)
        button2.show()
	button3 = gtk.Button("Close")
        button3.set_size_request(120, 30)
        button3.connect("clicked", close_window)
        bottombox.pack_start(button3, True, False, 10)
        button3.show()
	label1.show()
	localesel.show()
	mainbox.show()
	leftbox.show()
	rightbox.show()
	topbox.pack_start(leftbox, False, False, 10)
	topbox.pack_start(rightbox, False, False, 10)
	mainbox.pack_start(topbox, False, False, 10)
	mainbox.pack_start(bottombox, False, False, 10)
	leftbox.show()
	rightbox.show()
	topbox.show()
	bottombox.show()
	window.add(mainbox)
        mainbox.show()         
        window.show()
	
	return True