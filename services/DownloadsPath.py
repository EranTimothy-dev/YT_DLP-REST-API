import ctypes 
from ctypes import windll, wintypes
from uuid import UUID
import os

# ctypes GUID copied from MSDN sample code
class GUID(ctypes.Structure):
    """
    Represents a GUID structure required by the Windows API.

    Attributes:
        Data1: 32-bit unsigned integer.
        Data2: 16-bit unsigned integer.
        Data3: 16-bit unsigned integer.
        Data4: Array of 8 bytes.
    """
    _fields_ = [
        ("Data1", wintypes.DWORD),
        ("Data2", wintypes.WORD),
        ("Data3", wintypes.WORD),
        ("Data4", wintypes.BYTE * 8)
    ] 

    def __init__(self, uuidstr):
        """
        Initializes the GUID structure using a UUID string.

        Args:
            uuidstr (str): A string representation of a UUID.
        """
        uuid = UUID(uuidstr)
        ctypes.Structure.__init__(self)
        self.Data1, self.Data2, self.Data3, \
            self.Data4[0], self.Data4[1], rest = uuid.fields
        for i in range(2, 8):
            self.Data4[i] = rest>>(8-i-1)*8 & 0xff

SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
SHGetKnownFolderPath.argtypes = [
    ctypes.POINTER(GUID), wintypes.DWORD,
    wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)
]

def _get_known_folder_path(uuidstr):
    """
    Retrieves the full path of a known folder identified by its GUID.

    Args:
        uuidstr (str): A string representation of a UUID for the known folder.

    Returns:
        str: The full path of the known folder.

    Raises:
        WindowsError: If the SHGetKnownFolderPath API call fails.
    """
    pathptr = ctypes.c_wchar_p()
    guid = GUID(uuidstr)
    if SHGetKnownFolderPath(ctypes.byref(guid), 0, 0, ctypes.byref(pathptr)):
        raise ctypes.WinError()
    return pathptr.value

FOLDERID_Download = '{374DE290-123F-4565-9164-39C4925E467B}'

def get_windows_download_folder():
    """
    Returns the path to the Downloads folder for windows user.

    Returns:
        str: The path to the Downloads folder.
    """
    return _get_known_folder_path(FOLDERID_Download)



def get_non_windows_download_folder():
    """
    Returns the path to the Downloads folder for linux or MacOS user.

    Returns:
        str: The path to the Downloads folder.
    """
    home = os.path.expanduser("~")
    return os.path.join(home, "Downloads")



if __name__ == "__main__":
    if os.name == "nt":
        downloads_folder = get_windows_download_folder()
        print(downloads_folder)
    else:
        downloads_folder = get_non_windows_download_folder()
        print(downloads_folder)
    