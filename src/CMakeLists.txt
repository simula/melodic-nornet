#############################################################################
#### PROGRAMS                                                            ####
#############################################################################



#############################################################################
#### CONFIGURATION FILES                                                 ####
#############################################################################

INSTALL(PROGRAMS system-info.d/15-melodic DESTINATION ${CMAKE_INSTALL_FULL_SYSCONFDIR}/system-info.d)

INSTALL(PROGRAMS system-maintenance.d/15-melodic DESTINATION ${CMAKE_INSTALL_FULL_SYSCONFDIR}/system-maintenance.d)



#############################################################################
#### SOURCE DIRECTORIES                                                  ####
#############################################################################

ADD_SUBDIRECTORY(background)
ADD_SUBDIRECTORY(cloud-init)
ADD_SUBDIRECTORY(grub)
