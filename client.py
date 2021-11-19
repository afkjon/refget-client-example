#!/usr/bin/python
import sys, requests, json

# Settings
API_ENDPOINT     = "https://www.ebi.ac.uk/ena/cram/sequence/"
METADATA_QUERY   = "/metadata"

def construct_query(id):
    return API_ENDPOINT + id + METADATA_QUERY

def main(argv):
    # Default to displaying help window when not enough arguments
    if (len(argv) != 1): 
        return print("Usage: client.py <id>")

    response = requests.get(construct_query(argv[0]))

    # Display error code if request does not succeed
    if (response.status_code != 200):
        return print("Error! Response from server: \n" + 
            str(response.status_code) + ": " + response.reason)

    response_dict = response.json()
    print(json.dumps(response_dict, indent = 4, sort_keys = True))

if __name__ == "__main__":
    main(sys.argv[1:])
