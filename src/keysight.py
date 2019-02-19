#!/usr/bin/env python

# -*- coding: utf8 -*-

import struct
import numpy as np
import array
import struct
import matplotlib.pyplot as plt
import os
import sys
import time

class convert():
  def __init__(self, inputFileName, outputFileName, showPlot=False):
    self.inputFileName = inputFileName
    self.outputFileName = outputFileName
    self.showPlot = showPlot
    self.vpos = [[], []]
    self.hpos = [[], []]

  def read_csv(self):
    self.info = [[], []]
    print("Opening ", self.inputFileName, " to read LSF data")
    f = open(self.inputFileName, 'r')
    f.close()

  def save_tsv(self):
    print("Opening ", self.outputFileName, " to write TSV data")
    f = open(self.outputFileName, 'w')
    f.close()
    print('Done!')

  def show_plots(self):
    plt.plot()
    plt.show()

  def run(self):
    self.read_csv()
    self.save_tsv()
    if self.showPlot:
      self.show_plots()
