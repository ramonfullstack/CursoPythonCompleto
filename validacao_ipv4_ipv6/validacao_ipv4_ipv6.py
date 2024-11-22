def validIPAddress(proxy: str) -> str:
    def is_valid_ipv4(segment):
        if not segment.isdigit():
            return False
        if not 0 <= int(segment) <= 255:
            return False
        if len(segment) > 1 and segment[0] == '0':
            return False
        return True

    def is_valid_ipv6(segment):
        if len(segment) == 0 or len(segment) > 4:
            return False
        for char in segment:
            if char not in "0123456789abcdefABCDEF":
                return False
        return True
    
    if proxy.count('.') == 3:
        segments = proxy.split('.')
        if len(segments) == 4 and all(is_valid_ipv4(seg) for seg in segments):
            return "IPv4"
    
    if proxy.count(':') == 7:
        segments = proxy.split(':')
        if len(segments) == 8 and all(is_valid_ipv6(seg) for seg in segments):
            return "IPv6"

    return "Neither"

print(validIPAddress("172.16.254.1"))
print(validIPAddress("1990:0db8:85a3:0:0:8A2E:0370:7334"))
print(validIPAddress("256.256.256.256"))
print(validIPAddress("172.16:254.1"))
print(validIPAddress("1990:0db8:85a3:0:0:8A2E:0370:7890"))
print(validIPAddress("1990:0db8:85a3:0:0:8A2E:0370:89z0"))
