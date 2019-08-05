#!/usr/bin/env python

import gdown
import os
import os.path


download_namuwiki = lambda to, url='https://drive.google.com/uc?id=1dR4CsClnw2S2QQidWGO5AKGr-OLT4dS-': gdown.download(url, to, quiet=False)
download_kowiki = lambda to, url='https://drive.google.com/uc?id=1rmBYaWk1Zm5ImEZU634iUu2HedIbhAVM': gdown.download(url, to, quiet=False)


def main():
    output_dir = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'data')

    try:
        os.mkdir(output_dir)
    except:
        pass

    download_kowiki(os.path.join(output_dir, 'kowiki.txt.zst'))
    download_namuwiki(os.path.join(output_dir, 'namuwiki.txt.zst'))


if __name__ == '__main__':
    main()
