#!/bin/bash

#openssl enc -aes-128-cbc -e -in Tux.bmp -out cipherTux.bmp -K 00112233445566778889aabbccddeeff \
        #-iv 0102030405060708

#openssl enc -aes-128-ecb -e -in Tux.bmp -out cipherTux.bmp -K 00112233445566778889aabbccddeeff \
        #-iv 0102030405060708

openssl enc -aes-128-cbc -in plain.txt -out encrypt3.bin -K 123456789 \
        -iv 987654321
