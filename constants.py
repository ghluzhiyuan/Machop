MH_MAGIC = 0xfeedface
MH_CIGAM = 0xcefaedfe

MH_MAGIC_64 = 0xfeedfacf
MH_CIGAM_64 = 0xcffaedfe

FAT_MAGIC = 0xcafebabe
FAT_CIGAM = 0xbebafeca

# load commands
LC_REQ_DYLD = 0x80000000

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
LC_LOAD_WEAK_DYLIB = 0x18 | LC_REQ_DYLD
LC_SEGMENT_64 = 0x19
LC_ROUTINES_64 = 0x1a
LC_UUID = 0x1b
LC_RPATH = 0x1c | LC_REQ_DYLD
LC_CODE_SIGNATURE = 0x1d
LC_SEGMENT_SPLIT_INFO = 0x1e
LC_REEXPORT_DYLIB = 0x1f | LC_REQ_DYLD
LC_LAZY_LOAD_DYLIB = 0x20
LC_ENCRYPTION_INFO = 0x21
LC_DYLD_INFO = 0x22
LC_DYLD_INFO_ONLY = 0x22 | LC_REQ_DYLD
LC_LOAD_UPWARD_DYLIB = 0x23 | LC_REQ_DYLD
LC_VERSION_MIN_MACOSX = 0x24
LC_VERSION_MIN_IPHONEOS = 0x25
LC_FUNCTION_STARTS = 0x26
LC_DYLD_ENVIRONMENT = 0x27
LC_MAIN = 0x28 | LC_REQ_DYLD
LC_DATA_IN_CODE = 0x29
LC_SOURCE_VERSION = 0x2a
LC_DYLIB_CODE_SIGN_DRS = 0x2b
LC_ENCRYPTION_INFO_64 = 0x2c
LC_LINKER_OPTION = 0x2d
LC_LINKER_OPTIMIZATION_HINT = 0x2e
LC_VERSION_MIN_TVOS = 0x2f
LC_VERSION_MIN_WATCHOS = 0x30

INDIRECT_SYMBOL_LOCAL	= 0x80000000
INDIRECT_SYMBOL_ABS	= 0x40000000 

S_REGULAR = 0x0
S_ZEROFILL = 0x1
S_CSTRING_LITERALS = 0x2
S_4BYTE_LITERALS = 0x3
S_8BYTE_LITERALS = 0x4
S_LITERAL_POINTERS = 0x5
S_NON_LAZY_SYMBOL_POINTERS = 0x6
S_LAZY_SYMBOL_POINTERS = 0x7
S_SYMBOL_STUBS = 0x8
S_MOD_INIT_FUNC_POINTERS = 0x9
S_MOD_TERM_FUNC_POINTERS = 0xa
S_COALESCED	= 0xb
S_GB_ZEROFILL = 0xc
S_INTERPOSING = 0xd
S_16BYTE_LITERALS = 0xe
S_DTRACE_DOF = 0xf
S_LAZY_DYLIB_SYMBOL_POINTERS = 0x10
S_THREAD_LOCAL_REGULAR = 0x11
S_THREAD_LOCAL_ZEROFILL = 0x12
S_THREAD_LOCAL_VARIABLES = 0x13
S_THREAD_LOCAL_VARIABLE_POINTERS = 0x14
S_THREAD_LOCAL_INIT_FUNCTION_POINTERS = 0x15
SECTION_ATTRIBUTES_USR = 0xff000000
S_ATTR_PURE_INSTRUCTIONS = 0x80000000
S_ATTR_NO_TOC = 0x40000000
S_ATTR_STRIP_STATIC_SYMS = 0x20000000
S_ATTR_NO_DEAD_STRIP = 0x10000000
S_ATTR_LIVE_SUPPORT	= 0x08000000
S_ATTR_SELF_MODIFYING_CODE = 0x04000000
S_ATTR_DEBUG = 0x02000000
SECTION_ATTRIBUTES_SYS = 0x00ffff00
S_ATTR_SOME_INSTRUCTIONS = 0x00000400
S_ATTR_EXT_RELOC = 0x00000200
S_ATTR_LOC_RELOC = 0x00000100