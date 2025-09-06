import json
class Solution:

    def encode(self, strs: List[str]) -> str:
        return json.dumps(strs, separators=(',',':'))

    def decode(self, s: str) -> List[str]:
        return json.loads(s)