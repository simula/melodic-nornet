#############################################################################
# PROGRAMS
#############################################################################

INSTALL(FILES MELODIC-System-Info DESTINATION ${CMAKE_INSTALL_BINDIR})


#############################################################################
# SOURCE DIRECTORIES
#############################################################################

ADD_SUBDIRECTORY(background)
ADD_SUBDIRECTORY(cloud-init)
ADD_SUBDIRECTORY(grub)
