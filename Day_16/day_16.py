import sys
sys.path.insert(1, '../util')
from profiler import profile
from bitarray import bitarray
from functools import reduce

class BitBuffer:
    def __init__(self, bitarry):
        self.bitarray = bitarry
        self.p = 0
        self.len = len(self.bitarray)

    def read(self, n):
        if self.p > len(self.bitarray) or self.p + n > len(self.bitarray):
            raise SystemError("Requested bits beyond range of bitbuffer")
        val = self.to_int(''.join(self.bitarray[self.p:self.p+n]))
        self.p += n
        return val

    def trailing_zeros(self):
        return all(x=='0' for x in self.bitarray[self.p:])

    def tell(self):
        return self.p

    def is_empty(self):
        return self.p >= len(self.bitarray)
    
    def to_int(self,b):
        return int(b, 2)

def parse_literal(bb):
    num = 0
    while True:       
        tmp = bb.read(5)
        num = (num << 4) | (tmp & 0xF)
        if (tmp & 0x10) == 0:
            break
    return num

def parse_operator(bb):
    I = bb.read(1)
    if I == 1:
        num_subpackets = bb.read(11)
        vals = []
        for _ in range(num_subpackets):
            vals.append(parse_packet(bb))
        return vals
    elif I == 0:
        len_subpackets = bb.read(15)
        pos = bb.tell()
        vals = []
        while bb.tell() < pos + len_subpackets:
            vals.append(parse_packet(bb))
        return vals

def parse_packet(bb):
    version = bb.read(3)
    pid = bb.read(3)
    if pid == 0:
        return sum(parse_operator(bb))
    elif pid == 1:
        return reduce(lambda x,y: x*y, parse_operator(bb))
    elif pid == 2:
        return min(parse_operator(bb))
    elif pid == 3:
        return max(parse_operator(bb))
    elif pid==4:
        return parse_literal(bb)
    elif pid == 5:
        a,b = parse_operator(bb)
        return 1 if a > b else 0
    elif pid == 6:
        a,b = parse_operator(bb)
        return 1 if a < b else 0
    elif pid == 7:
        a,b = parse_operator(bb)
        return 1 if a==b else 0

@profile
def part_one(data):
    bb = BitBuffer(data)
    versions = []
    while not bb.is_empty():
        if bb.trailing_zeros():
            break
        versions.append(bb.read(3))
        pid = bb.read(3)
        if pid==4:
            parse_literal(bb)    
        else:
            I = bb.read(1)
            if I == 1:
                bb.read(11)
                continue
            elif I == 0:
                bb.read(15)
                continue
    return sum(versions)

@profile
def part_two(data):
    bb = BitBuffer(data)
    while not bb.is_empty():
        if bb.trailing_zeros():
            break
        val = parse_packet(bb)
    return val

with open("day_16_input.txt") as f:
    data = [f for x in f.read() for f in (format(int(x,16), '0>4b'))]
    print(f"Part One: {part_one(data.copy())}") # 1014
    print(f"Part Two: {part_two(data.copy())}") # 1922490999789