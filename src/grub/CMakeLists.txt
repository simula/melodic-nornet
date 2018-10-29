#############################################################################
# BOOTLOADER CONFIGURATION FILES
#############################################################################

FILE(GLOB themeFiles  "[0-9][0-9]_*_theme")

INSTALL(FILES ${themeFiles} DESTINATION /etc/grub.d)
INSTALL(FILES grub-defaults DESTINATION ${CMAKE_INSTALL_DATADIR}/melodic-nornet)
