#!/usr/bin/python

import ipaddress
import logging
import os
from impacket import smb


# I want to eventually scan a whole ip/subnet for open smb shares

# def get_network():
#
#     ipaddress.ip_network()

def scan_smb(host, username, password):
    try:
        smb_client = smb.SMB('SMBSERVER', host)
        smb_client.login(username, password)

        shares = smb_client.get_client_name()
        for share in shares:
            print(f'Share name: {share["shi1_netname"]}, Type: {share["shi1_type"]}')

    except smb.SessionError as e:
        print(f"Failed to connect to {host}: {str(e)}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def main():
    pass


if __name__ == "__main__":
    main()
