def ascii2hex(self, ascii):
        pythomation.TS_Comment('Default Value: %s' % ascii)
        hexStr = ''.join([(str(hex(ord(i)))[2:4] + ' ') for i in ascii])
        return hexStr