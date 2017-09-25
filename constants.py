MH_MAGIC = 0xfeedface
MH_CIGAM = 0xcefaedfe

MH_MAGIC_64 = 0xfeedfacf
MH_CIGAM_64 = 0xcffaedfe

FAT_MAGIC = 0xcafebabe
FAT_CIGAM = 0xbebafeca

# load commands
LC_SEGMENT = 0x1
LC_SYMTAB = 0x2
LC_SYMSEG = 0x3
LC_THREAD = 0x4
LC_UNIXTHREAD = 0x5
LC_LOADFVMLIB = 0x6
LC_IDFVMLIB = 0x7
LC_IDENT = 0x8
LC_FVMFILE = 0x9
LC_PREPAGE = 0xa
LC_DYSYMTAB = 0xb
LC_LOAD_DYLIB = 0xc
LC_ID_DYLIB = 0xd
LC_LOAD_DYLINKER = 0xe
LC_ID_DYLINKER = 0xf
LC_PREBOUND_DYLIB = 0x10
LC_ROUTINES = 0x11
LC_SUB_FRAMEWORK = 0x12
LC_SUB_UMBRELLA = 0x13
LC_SUB_CLIENT = 0x14
LC_SUB_LIBRARY = 0x15
LC_TWOLEVEL_HINTS = 0x16
LC_PREBIND_CKSUM = 0x17
LC_SEGMENT_64 = 0x19