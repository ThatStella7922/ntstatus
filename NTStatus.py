# NTStatus.py 1.0
# ThatStella7922 - https://thatstel.la

name = "ntstatus.py"
ver = "1.0"

import sys

# Colors
class colors:
    pink = '\033[38;5;206m'
    end = '\033[0m'
    ok = "\033[96m[*]\033[0m"
    success = "\033[92m[√]\033[0m"
    warn = "\033[93m[!]\033[0m"
    question = "\033[94m[?]\033[0m"
    fail = "\033[91m[x]\033[0m"
## End of colors

helpStr = """Usage: ntstatus.py exit_code [silent]

    exit_code: Standard Win32 program exit code
    [silent]: Optional argument to clean up output (often for use in scripts)
    
    Example: ntstatus.py -1073741654
    Example 2: ntstatus.py -1073741654 silent
    
    Notes: 
    - I've seen that these Win32 exit codes are often seen when programs crash from some external or NT-related event. Usually they're in the high negatives.
    - You can look up the resulting NTStatus hex code at
      - Microsoft's website: https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55
      - ntstatus.h listing on GitHub: https://github.com/tpn/winsdk-10/blob/master/Include/10.0.14393.0/shared/ntstatus.h"""

def decimal_to_32bit_signed_hex(number):
    # Ensure the number is within the 32-bit signed integer range
    if not (-2**31 <= number < 2**31):
        raise ValueError("Number out of range for 32-bit signed integer.")
    
    # Convert to hexadecimal and format to 32-bit
    if number < 0:
        # For negative numbers, find the two's complement
        hex_number = hex((1 << 32) + number)
    else:
        hex_number = hex(number)
    
    # Format the hex string to ensure it is 32-bit
    return hex_number.upper().replace('0X', '0x').zfill(10)

def convert_exitstatus_to_ntstatus(exit_status):
    # Convert the exit status to a signed 32-bit integer
    exit_status = int(exit_status)
    # Convert to NTSTATUS value
    return decimal_to_32bit_signed_hex(exit_status)

def do_output(decimal_number, hex_representation, silent=False):
    if not silent:
        print()
        print(f'{colors.success} Program exit code {decimal_number} corresponds to NTSTATUS value {colors.pink}{hex_representation}{colors.end}.' + '\nThis value can be looked up at https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/596a1078-e883-4972-9bbc-49e60bebca55?redirectedfrom=MSDN')
    else:
        print(hex_representation)

# Main script
if len(sys.argv) != 3:
    shouldSilent=False
    print(f"{name} v{ver} - Quick Win32 exit code to NTStatus code converter \n{colors.pink}ThatStella7922{colors.end} (https://thatstel.la)")

if len(sys.argv) <= 1:
    print()
    print(f"Help for {name} v{ver}:")
    print(helpStr)
    print()
    sys.exit(0)
elif len(sys.argv) == 3 and sys.argv[2] == "silent":
    shouldSilent=True
    pass
elif len(sys.argv) != 2:
    print()
    print(f"Error while processing arguments.\nSee the help below:")
    print()
    print(helpStr)
    print()
    sys.exit(1)

decimal_number = sys.argv[1]
hex_representation = convert_exitstatus_to_ntstatus(decimal_number)
do_output(decimal_number, hex_representation, silent=shouldSilent)