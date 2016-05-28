
Debian
====================
This directory contains files used to package chilicoind/chilicoin-qt
for Debian-based Linux systems. If you compile chilicoind/chilicoin-qt yourself, there are some useful files here.

## chilicoin: URI support ##


chilicoin-qt.desktop  (Gnome / Open Desktop)
To install:

	sudo desktop-file-install chilicoin-qt.desktop
	sudo update-desktop-database

If you build yourself, you will either need to modify the paths in
the .desktop file or copy or symlink your chilicoin-qt binary to `/usr/bin`
and the `../../share/pixmaps/chilicoin128.png` to `/usr/share/pixmaps`

chilicoin-qt.protocol (KDE)

