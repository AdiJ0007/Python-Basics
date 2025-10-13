import argparse as ap
import requests as rq

def download_file(url,local_filename):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with rq.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename

parser = ap.ArgumentParser()

parser.add_argument("URL",help = "URL of file to download")
parser.add_argument("output",help = "Name by which file to be saved")

args = parser.parse_args()

print(args.URL)
print(args.output)
download_file(args.URL,args.output)

