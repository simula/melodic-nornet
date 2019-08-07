#############################################################################
# PROGRAMS
#############################################################################

INSTALL(FILES MELODIC-System-Info   DESTINATION ${CMAKE_INSTALL_BINDIR})
INSTALL(FILES MELODIC-System-Info.1 DESTINATION ${CMAKE_INSTALL_MANDIR}/man1)


#############################################################################
# SOURCE DIRECTORIES
#############################################################################

ADD_SUBDIRECTORY(background)
ADD_SUBDIRECTORY(cloud-init)
ADD_SUBDIRECTORY(grub)
