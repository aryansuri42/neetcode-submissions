class Solution:

    def encode(self, strs: List[str]) -> str:
        string_out = ""
        for string in strs:
            string_out = string_out+string+"|"
        self.decode(string_out)
        return string_out

    def decode(self, s: str) -> List[str]:
        string_list = []
        new_string = ""
        for string in s:
            if string=="|":
                string_list.append(new_string)
                new_string=""
            else:
                new_string+=string
        return string_list