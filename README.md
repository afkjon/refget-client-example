# Introduction

This is a basic client run from the console that allows the user to query the ENA CRAM archive server with an MD5 checksum, obtained from the [GA4GH refget standard](https://samtools.github.io/hts-specs/refget.html), for a specific reference sequence's metadata. The server replies with a json document holding the metadata if the MD5 checksum is valid. If the MD5 checksum is invalid, it will respond with a 404 Not Found error. HTTP error responses are outlined in the [refget API specification](https://samtools.github.io/hts-specs/refget.html#errors).



# Prerequisites

This client uses the `requests` package from the Python Package Index (PyPI), which supports Python 3.6+.

If you are not sure if your python installion includes the `requests` package, you may need to run the following command to install the prerequisites:

```
python3 -m pip3 install requests
```

# Usage
To use the client, we can run the `client.py` script with python with the following command:
```
python3 client.py <id>
```
Where we replace \<id\> with the MD5 checksum identifier.


# Example
We can run the client to query the ENA CRAM archive with the MD5 checksum of `3050107579885e1608e6fe50fae3f8d0` to retrieve the reference sequence's metadata with the following command:
```
python3 client.py 3050107579885e1608e6fe50fae3f8d0
```
If there is no error, the response will be output in JSON printed onto the console as follows:
```
PS C:\refget-client-example> python3 client.py 3050107579885e1608e6fe50fae3f8d0
{
    "metadata": {
        "aliases": [],
        "id": "3050107579885e1608e6fe50fae3f8d0",
        "length": 7156,
        "md5": "3050107579885e1608e6fe50fae3f8d0",
        "trunc512": null
    }
}
```

Additionally, if you would like to output the resulting metadata into a file, you may pipe it to an output file with the following command:

```
python3 client.py 3050107579885e1608e6fe50fae3f8d0 > output.json
```
