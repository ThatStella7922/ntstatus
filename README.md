# ntstatus
Quick Win32 exit code to NTStatus code converter

## Introduction
**ntstatus** is a quick and easy to use utility to convert Win32 exit codes to NTStatus codes that can be looked up for guidance.

I've seen that these Win32 exit codes are often seen when programs crash from some external or NT-related event. Usually they're in the high negatives.

## Usage
Using **ntstatus** is very simple. See the below output of ntstatus.py when run with no arguments, or with the `-h`/`--help` arguments:

```
ntstatus.py v1.0.1 - Quick Win32 exit code to NTStatus code converter 
ThatStella7922 (https://thatstel.la)

Help for ntstatus.py v1.0.1:
Usage: ntstatus.py exit_code [silent]

    exit_code: Standard Win32 program exit code
    [silent]: Optional argument to clean up output (often for use in scripts)
    
    Example: ntstatus.py -1073741654
    Example 2: ntstatus.py -1073741654 silent

    You can also show this help again by running with no arguments or with --help or -h.

    Notes:
    - Adding the silent argument will supress error messages, exiting with code 1 if an error does occur. Run without silent mode to see error messages.
    - I've seen that these Win32 exit codes are often seen when programs crash from some external or NT-related event. Usually they're in the high negatives.
    - You can look up the resulting NTStatus hex code at
      - Microsoft's website: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55
      - ntstatus.h listing on GitHub: https://github.com/tpn/winsdk-10/blob/master/Include/10.0.14393.0/shared/ntstatus.h
```
---
It takes an exit code as the first argument, then prints it out to the console, as shown:
```
PS C:\Users\Stella\Desktop>python NTStatus.py -1073741654
ntstatus.py v1.0.1 - Quick Win32 exit code to NTStatus code converter 
ThatStella7922 (https://thatstel.la)

[√] Program exit code -1073741654 corresponds to NTSTATUS value 0xC00000AA.
This value can be looked up at https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55?redirectedfrom=MSDN
```

If you enable the silent mode by appending the `silent` argument, it will clean up the output for use in scripting:
```
PS C:\Users\Stella\Desktop>python NTStatus.py -1073741654 silent
0xC00000AA
```

## Requirements and Compatibility
Requires Python 3.10 or newer, and should run on any OS that runs Python 3.10.
