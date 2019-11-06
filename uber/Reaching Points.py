class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while tx > sx and ty > sy:
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
        return tx == sx and ty >= sy and (ty - sy) % sx == 0 or ty == sy and tx >= sx and (tx - sx) % sy == 0
