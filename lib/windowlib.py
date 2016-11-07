# -*- coding: utf-8 -*-
#interfaces graficas de syncloud
import wx
import wx.xrc

###########################################################################
## Class Frame1
###########################################################################

class logonwindow(wx.Frame):

    def __init__(self, parent, title, size):
        super(logonwindow, self).__init__(parent, title=title, size=size,
            style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)
#        self.barmenu()
        self.centrar()
        self.mostrar()

    def centrar(self):
        self.Centre()

    def mostrar(self):
        self.Show()

    def barmenu(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Salir de la aplicación')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnQuit, fitem)



    def OnQuit(self, e):
        self.Close()
