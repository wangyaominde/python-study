# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import argparse
import socket
import struct

BROADCAST_IP = '255.255.255.255'
DEFAULT_PORT = 9

def create_magic_packet(macaddress):
    if len(macaddress) == 12:
        pass
    elif len(macaddress) == 17:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, '')
    else:
        raise ValueError('Incorrect MAC address format')

    # Pad the synchronization stream
    data = b'FFFFFFFFFFFF' + (macaddress * 16).encode()
    send_data = b''

    # Split up the hex values in pack
    for i in range(0, len(data), 2):
        send_data += struct.pack(b'B', int(data[i: i + 2], 16))
    return send_data

def send_magic_packet(*macs, **kwargs):
    packets = []
    ip = kwargs.pop('ip_address', BROADCAST_IP)
    port = kwargs.pop('port', DEFAULT_PORT)
    for k in kwargs:
        raise TypeError('send_magic_packet() got an unexpected keyword '
                        'argument {!r}'.format(k))

    for mac in macs:
        packet = create_magic_packet(mac)
        packets.append(packet)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.connect((ip, port))
    for packet in packets:
        sock.send(packet)
    sock.close()

def main(argv=None):
    parser = argparse.ArgumentParser(
        description='Wake one or more computers using the wake on lan'
                    ' protocol.')
    parser.add_argument(
        'macs',
        metavar='mac address',
        nargs='+',
        help='The mac addresses or of the computers you are trying to wake.')
    parser.add_argument(
        '-i',
        metavar='ip',
        default=BROADCAST_IP,
        help='The ip address of the host to send the magic packet to.'
             ' (default {})'.format(BROADCAST_IP))
    parser.add_argument(
        '-p',
        metavar='port',
        type=int,
        default=DEFAULT_PORT,
        help='The port of the host to send the magic packet to (default 9)')
    args = parser.parse_args(argv)
    send_magic_packet(*args.macs, ip_address=args.i, port=args.p)

if __name__ == '__main__':  # pragma: nocover
    main()