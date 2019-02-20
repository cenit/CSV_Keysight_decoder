#!/usr/bin/env python

# -*- coding: utf8 -*-

import argparse
import keysight

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Analyse Keysight CSV files and extracts maximum and bandwidth values')
  parser.add_argument('file', type=argparse.FileType('r'), nargs='+', help='Input files (Keysight CSV)')
  args = parser.parse_args()
  if args.file is not None:
    for f in args.file:
      a = keysight.custom_csv(f)
      a.run_stats()
  else:
    parser.print_help()
