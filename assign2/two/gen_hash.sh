#!/bin/bash

openssl dgst -sha256 -hmac "$(cat ./key128)" file.txt > 128_256
openssl dgst -sha256 -hmac "$(cat ./key160)" file.txt > 160_256
openssl dgst -sha256 -hmac "$(cat ./key256)" file.txt > 256_256

openssl dgst -sha512 -hmac "$(cat ./key128)" file.txt > 128_512
openssl dgst -sha512 -hmac "$(cat ./key160)" file.txt > 160_512
openssl dgst -sha512 -hmac "$(cat ./key256)" file.txt > 256_512
