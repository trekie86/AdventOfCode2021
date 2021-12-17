import numpy as np

from util.fileutil import read_file_to_string_list

ver_length = 3
type_length = 3
literal_type = 4


class Packet:
    def __init__(self, version: int, type_id: int):
        self.version = version
        self.type_id = type_id

    def get_version_sum(self):
        return self.version

    def get_value(self):
        pass


class LiteralPacket(Packet):
    def __init__(self, version: int, type_id: int, value: int):
        super(LiteralPacket, self).__init__(version, type_id)
        self.value = value

    def get_value(self):
        return self.value


class OperatorPacket(Packet):
    def __init__(self, version: int, type_id: int):
        super(OperatorPacket, self).__init__(version, type_id)
        self.sub_packets = []

    def add_sub_packet(self, p: Packet):
        self.sub_packets.append(p)

    def get_version_sum(self):
        return self.version + sum([packet.get_version_sum() for packet in self.sub_packets])

    def get_value(self):
        if self.type_id == 0:
            return sum([p.get_value() for p in self.sub_packets])
        elif self.type_id == 1:
            return np.product([p.get_value() for p in self.sub_packets])
        elif self.type_id == 2:
            return np.min([p.get_value() for p in self.sub_packets])
        elif self.type_id == 3:
            return np.max([p.get_value() for p in self.sub_packets])
        elif self.type_id == 5:
            return int(self.sub_packets[0].get_value() > self.sub_packets[1].get_value())
        elif self.type_id == 6:
            return int(self.sub_packets[0].get_value() < self.sub_packets[1].get_value())
        elif self.type_id == 7:
            return int(self.sub_packets[0].get_value() == self.sub_packets[1].get_value())


def hex_to_binary(hex_str: str) -> str:
    # Note this will not work if there are leading zeros in the HEX number.
    # I'm assuming there won't be, we'll see how that works out.
    return bin(int(hex_str, 16))[2:].zfill(4 * len(hex_str))


def bin_to_int(bin_str: str) -> int:
    return int(bin_str, 2)


def parse_literal(bin_val: str, version: int, type_id: int, idx: int, sub_packet: bool = False):
    value_str = ""
    last_group = False
    while not last_group:
        if bin_val[idx] == '1':
            value_str += bin_val[idx + 1:idx + 5]
            idx += 5
        else:
            last_group = True
            value_str += bin_val[idx + 1:idx + 5]
            idx += 5
            # # If it's a sub-packet we don't want to go to the end of the hex bits because they are subsequent bits
            # if not sub_packet:
            #     idx += 4 - idx % 4

    p = LiteralPacket(version=version, type_id=type_id, value=bin_to_int(value_str))
    return p, idx


def parse_operator(bin_val: str, version: int, type_id: int, idx: int):
    p = OperatorPacket(version=version, type_id=type_id)
    length_type_id = int(bin_val[idx])
    idx += 1
    if length_type_id:
        # If the length type id is 1, then the number of sub-packets is 11 bits
        sub_packet_count = int(bin_val[idx:idx + 11], 2)
        idx += 11
        for _ in range(sub_packet_count):
            version = bin_to_int(bin_val[idx:idx + ver_length])
            idx += ver_length
            type_id = bin_to_int(bin_val[idx:idx + type_length])
            idx += ver_length
            if type_id == literal_type:
                packet, idx = parse_literal(bin_val, version, type_id, idx)
                p.add_sub_packet(packet)
            else:
                packet, idx = parse_operator(bin_val, version, type_id, idx)
                p.add_sub_packet(packet)
    else:
        # If the length type id is 1, then the number of sub-packets is 15 bits
        total_sub_packet_bits = int(bin_val[idx:idx + 15], 2)
        idx += 15
        sub_packets_idx = idx + total_sub_packet_bits
        while idx < sub_packets_idx:
            version = bin_to_int(bin_val[idx:idx + ver_length])
            idx += ver_length
            type_id = bin_to_int(bin_val[idx:idx + type_length])
            idx += ver_length
            if type_id == literal_type:
                packet, idx = parse_literal(bin_val, version, type_id, idx)
                p.add_sub_packet(packet)
            else:
                packet, idx = parse_operator(bin_val, version, type_id, idx)
                p.add_sub_packet(packet)

    return p, idx


def parse_packets(bin_val: str, idx: int) -> [Packet]:
    packets = []
    while bin_to_int(bin_val[idx:len(bin_val)]) > 0:
        version = bin_to_int(bin_val[idx:idx + ver_length])
        idx += ver_length
        type_id = bin_to_int(bin_val[idx:idx + type_length])
        idx += ver_length
        if type_id == literal_type:
            packet, idx = parse_literal(bin_val, version, type_id, idx)
            packets.append(packet)
        else:
            packet, idx = parse_operator(bin_val, version, type_id, idx)
            packets.append(packet)

    return packets


def part1() -> None:
    hex_val = read_file_to_string_list("data.txt")[0]
    bin_val = hex_to_binary(hex_val)
    current_idx = 0
    packets = parse_packets(bin_val, current_idx)
    version_sum = sum([packet.get_version_sum() for packet in packets])
    print(f"Total version numbers is {version_sum}")


def part2() -> None:
    hex_val = read_file_to_string_list("data.txt")[0]
    bin_val = hex_to_binary(hex_val)
    current_idx = 0
    packet = parse_packets(bin_val, current_idx)[0]
    value = packet.get_value()
    print(f"Total value is {value}")


if __name__ == "__main__":
    part1()
    part2()
