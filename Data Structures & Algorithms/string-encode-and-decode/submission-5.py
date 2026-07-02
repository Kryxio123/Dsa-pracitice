class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "False"
        encoded = ""
        for y in strs:
            for x in y:
                encoded += chr((ord(x) + 10))
            encoded += "#"
        encoded = encoded[:-1]
        return encoded



    def decode(self, s: str) -> List[str]:
        if s == "False":
            return []
        decoded = ""
        for x in s:
            decoded += chr(ord(x) - 10)
        sep = chr(ord("#") - 10)
        result = decoded.split(sep)
        return result