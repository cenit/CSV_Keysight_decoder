#!/usr/bin/env python

# -*- coding: utf8 -*-

import argparse
import keysight

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Convert Keysight CSV to TSV files and plot them')
  parser.add_argument('input_file', help='Input file (Keysight CSV)')
  parser.add_argument('output_file', help='Output file (TSV format)')
  parser.add_argument('--showPlot', dest='showPlot', default=False, action='store_true', help='Show the plot in a windows after conversion', required=False)
  args = parser.parse_args()
  if args.input_file is not None and args.output_file is not None:
    a = keysight.convert(inputFileName=args.input_file, outputFileName=args.output_file, showPlot=args.showPlot)
  else:
    parser.print_help()
  a.run()
