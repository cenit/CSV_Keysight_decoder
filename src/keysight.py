#!/usr/bin/env python

# -*- coding: utf8 -*-

import pandas as pd
import matplotlib.pyplot as plt

class convert():
  def __init__(self, inputFileName, outputFileName, showPlot=False):
    self.inputFileName = inputFileName
    self.outputFileName = outputFileName
    self.showPlot = showPlot
    self.df = pd.DataFrame()

  def read_csv(self):
    csv_data = []
    print("Opening ", self.inputFileName, " to read LSF data")
    f = open(self.inputFileName, 'r')
    for line in f:
      line = line.rstrip('\n')
      if line[0] != '!':
        data = line.split(',')
        if len(data) == 2:
          data_float = [float(i) for i in data]
          csv_data.append(data_float)
    f.close()
    self.df = pd.DataFrame(csv_data, columns=["Frequency", "Amplitude"])

  def save_tsv(self):
    print("Opening ", self.outputFileName, " to write TSV data")
    self.df.to_csv(self.outputFileName, index=False, sep='\t')
    print('Done!')

  def show_plots(self):
    self.df.plot(x='Frequency', y='Amplitude', style='o')
    plt.show()

  def run(self):
    self.read_csv()
    self.save_tsv()
    if self.showPlot:
      self.show_plots()
