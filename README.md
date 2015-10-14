# symbian-converter
Automatically exported from code.google.com/p/symbian-converter

<h1>Description</h1>

This is a converter of VCF file exported from Google Contact to Symbian VCard format.

Google VCF file contains all contact in one file.

Symbian format uses multiple files with quoted-printable-encoded UTF8 characters.

I wrote this application to have my google contact on Symbian device.

<h1>Dependencies</h1>

To run this app you need apache commons codec package: http://commons.apache.org/codec.

I used version 1.6.

<h1>Runbook</h1>

Export needed contacts from Google Contact into VCard format.
Run this application against this file.
You will have a set of VCF files converted to Symbian format.
