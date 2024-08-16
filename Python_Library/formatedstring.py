# format a simple string
firstname = 'Lucas'
secondname = 'Dewsnap'
# trying to print 'lucas dewsnap is a coder
notformattedmsg = firstname + \
    ' [' + secondname + '] is a coder'  # no formatting
formattedmsg = f'{firstname} [{secondname}] is a coder'  # formatted
print(notformattedmsg + '\n' + formattedmsg)
