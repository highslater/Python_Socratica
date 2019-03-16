#!/usr/bin/env python3.7

"""08_Interactive_Help.py.

Eighth Program of the Socratica Sexy-Hologram-Human/Computer-Hybrid
Python Series.

"""
import logging


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="LOG_files/LOG_08.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='a')
logger = logging.getLogger()
logger.info("08_Interactive_Help.py RUN / START")


"""
>>> dir
<built-in function dir>
>>> dir()
['__builtins__','__doc__','__loader__','__name__','__package__','__spec__']
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException',
'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning',
'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning',
'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False',
'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning',
'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError',
'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError',
'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError',
'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError',
'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning',
'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration',
SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError',
'TimeoutError', 'True', 'TypeError', 'UnboundLocalError',
'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError',
'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError',
'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__',
'__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__',
'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable',
'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr',
'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter',
'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash',
'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter',
'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next',
'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range',
'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted',
'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
>>> help(pow)
Help on built-in function pow in module builtins:

pow(x, y, z=None, /)
    Equivalent to x**y (with two arguments) or x**y % z (with three arguments)

    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.


>>> help(hex)
Help on built-in function hex in module builtins:

hex(number, /)
    Return the hexadecimal representation of an integer.

    >>> hex(12648430)
    '0xc0ffee'

>>> help('modules')

Please wait a moment while I gather a list of all available modules...

CDROM               _weakref            httplib2            redshift_gtk
CommandNotFound     _weakrefset         icu                 reportlab
Crypto              _yaml               icu_docs            reprlib
DLFCN               abc                 idlelib             requests
IN                  aifc                idna                resource
IPython             antigravity         imaplib             rlcompleter
NvidiaDetector      apport              imghdr              rmagic
Onboard             apport_python_hook  imp                 runpy
PIL                 apt                 importlib           scanext
PyICU               apt_clone           inspect             sched
PyQt5               apt_inst            io                  scp
Quirks              apt_pkg             ipaddress           select
ScreenResolution    aptdaemon           ipykernel           selectors
TYPES               aptsources          ipykernel_launcher  send2trash
UbuntuDrivers       argparse            ipython_genutils    serial
UbuntuSystemService array               ipywidgets          sessioninstaller
VBoxAuth            asn1crypto          itertools           setproctitle
VBoxAuthSimple      ast                 jedi                setuptools
VBoxDD              asynchat            jinja2              shelve
VBoxDD2             asyncio             json                shlex
VBoxDDU             asyncore            jsonschema          shutil
VBoxDbg             atexit              jupyter             signal
VBoxDragAndDropSvc  audioop             jupyter_client      sip
VBoxGuestControlSvc autoreload          jupyter_console     sipconfig
VBoxGuestPropSvc    axi                 jupyter_core        sipconfig_d5
VBoxHeadless        backcall            jwt                 sipconfig_nd5
VBoxHostChannel     base64              keygen              site
VBoxKeyboard        bcrypt              keyword             sitecustomize
VBoxNetDHCP         bdb                 lib2to3             six
VBoxNetNAT          binascii            libvboxjxpcom       smtpd
VBoxOGLhostcrutil   binhex              linecache           smtplib
VBoxOGLhosterrorspu bisect              locale              sndhdr
VBoxOGLrenderspu    bleach              logging             socket
VBoxPython          blinker             louis               socketserver
VBoxPython3_5m      brlapi              lsb_release         speechd
VBoxREM             builtins            lxml                speechd_config
VBoxRT              bz2                 lzma                spwd
VBoxSDL             cProfile            macpath             sqlite3
VBoxSharedClipboard cairo               macurl2path         sre_compile
VBoxSharedCrOpenGL  calendar            mailbox             sre_constants
VBoxSharedFolders   cffi                mailcap             sre_parse
VBoxVMM             cgi                 mako                ssl
VBoxVMMPreload      cgitb               markupsafe          stat
VBoxXPCOM           chardet             marshal             statistics
VBoxXPCOMC          chunk               math                storemagic
VirtualBox          clitable            mimetypes           string
__future__          cmath               miniterm            stringprep
_ast                cmd                 mistune             struct
_bisect             code                mmap                subprocess
_bootlocale         codecs              modulefinder        sunau
_bz2                codeop              multiprocessing     symbol
_cffi_backend       collections         nacl                sympyprinting
_codecs             colorsys            nbconvert           symtable
_codecs_cn          compileall          nbformat            sys
_codecs_hk          concurrent          netmiko             sysconfig
_codecs_iso2022     configobj           netrc               syslog
_codecs_jp          configparser        nis                 tabnanny
_codecs_kr          contextlib          nntplib             tarfile
_codecs_tw          copy                notebook            tccalib
_collections        copyable_regex_object ntpath              telnetlib
_collections_abc    copyreg             nturl2path          tempfile
_compat_pickle      createfontdatachunk numbers             terminado
_compression        crypt               oauthlib            terminal
_crypt              cryptography        oneconf             termios
_csv                csv                 opcode              test
_ctypes             ctypes              operator            testpath
_ctypes_test        cups                optparse            tests
_curses             cupsext             orca                textfsm
_curses_panel       cupshelpers         os                  texttable
_datetime           curl                ossaudiodev         textwrap
_dbm                curses              painter             this
_dbus_bindings      cythonmagic         pandocfilters       threading
_dbus_glib_bindings datetime            paramiko            thresholder
_decimal            dateutil            parser              time
_dummy_thread       dbm                 parso               timeit
_elementtree        dbus                pathlib             tkinter
_functools          deb822              pcardext            token
_gdbm               debconf             pdb                 tokenize
_hashlib            debian              pexpect             tornado
_heapq              debian_bundle       pickle              trace
_icu                decimal             pickleshare         traceback
_imp                decorator           pickletools         tracemalloc
_io                 defer               pid                 traitlets
_json               defusedxml          pilconvert          tty
_locale             difflib             pildriver           turtle
_lsprof             dirspec             pilfile             types
_lzma               dis                 pilfont             typing
_markupbase         distutils           pilprint            ufw
_md5                doctest             pip                 unicodedata
_multibytecodec     dummy_threading     pipes               unittest
_multiprocessing    easy_install        piston_mini_client  uno
_opcode             email               pkg_resources       unohelper
_operator           encodings           pkgutil             urllib
_osx_support        enhancer            platform            urllib3
_pickle             ensurepip           player              uu
_posixsubprocess    entrypoints         plistlib            uuid
_pydecimal          enum                poplib              validate
_pyio               errno               posix               vboxapi
_random             explode             posixpath           vboxshell
_sha1               faulthandler        pprint              venv
_sha256             fcntl               problem_report      viewer
_sha512             filecmp             profile             virtkey
_signal             fileinput           prometheus_client   warnings
_sitebuiltins       fnmatch             prompt_toolkit      wave
_socket             formatter           pstats              wcwidth
_sqlite3            fpectl              psutil              weakref
_sre                fractions           pty                 webbrowser
_ssl                ftplib              ptyprocess          webencodings
_stat               functools           pwd                 wheel
_string             gc                  py_compile          widgetsnbextension
_strptime           genericpath         pyasn1              wsgiref
_struct             getopt              pyatspi             xapian
_symtable           getpass             pyclbr              xapp
_sysconfigdata      gettext             pycparser           xdg
_sysconfigdata_dm   gi                  pycurl              xdrlib
_sysconfigdata_m    gifmaker            pydoc               xkit
_testbuffer         glob                pydoc_data          xml
_testcapi           grp                 pyexpat             xmlrpc
_testimportmultiple gzip                pygments            xxlimited
_testmultiphase     hashlib             pygtkcompat         xxsubtype
_thread             heapq               qtconsole           yaml
_threading_local    hello               queue               zipapp
_tkinter            hmac                quopri              zipfile
_tracemalloc        hpmudext            random              zipimport
_version            html                re                  zlib
_warnings           http                readline            zmq

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

>>> import math
>>> dir()
['__builtins__', '__doc__', '__loader__', '__name__', '__package__',
 '__spec__', 'math']


>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos',
 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign',
 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs',
 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot',
 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log',
 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin',
 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']

>>> dir(math.radians)
['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__',
'__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__',
'__setattr__', '__sizeof__', '__str__', '__subclasshook__',
'__text_signature__']


>>> help(math.radians)
Help on built-in function radians in module math:

radians(...)
    radians(x)

    Convert angle x from degrees to radians.

"""
