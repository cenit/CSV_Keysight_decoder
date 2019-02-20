#!/usr/bin/env python

# -*- coding: utf8 -*-

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
class custom_csv():
  def __init__(self, f, outputFileName=None, showPlot=False, deltaBW=3.0):
    self.f = f
    self.outputFileName = outputFileName
    self.showPlot = showPlot
    self.df = None
    self.deltaBW = deltaBW
    self.F_R = None
    self.bandwidth = None

  def read_csv(self):
    csv_data = []
    for line in self.f:
      line = line.rstrip('\n')
      if line[0] != '!':
        data = line.split(',')
        if len(data) == 2:
          data_float = [float(i) for i in data]
          csv_data.append(data_float)
    self.df = pd.DataFrame(csv_data, columns=["Frequency", "Amplitude"])

  def close_inputFile(self):
    self.f.close()

  def save_tsv(self):
    print("Opening ", self.outputFileName, " to write TSV data")
    self.df.to_csv(self.outputFileName, index=False, sep='\t')
    print('Done!')

  def show_plots(self):
    #self.df.plot(x='Frequency', y='Amplitude', style='o')
    self.df.plot(x='Frequency', y='Amplitude', style='-')
    plt.show()

  def create_stats(self):
    self.id_pos = self.f.name.split(os.sep)[-1].split('.')[0]
    maxval = self.df[self.df['Amplitude'] == self.df['Amplitude'].max()]
    maxvalAmpl = maxval.iloc[0]['Amplitude']
    self.F_R = maxval.iloc[0]['Frequency']
    reqvalAmpl = abs(maxvalAmpl)+self.deltaBW
    minus3db_val = self.df.iloc[(self.df['Amplitude'].abs()-reqvalAmpl).abs().argsort()[:4]].sort_index()
    left_minus3db_val = minus3db_val[0:2]
    y1a = left_minus3db_val.iloc[0]['Frequency']
    y1b = left_minus3db_val.iloc[1]['Frequency']
    x1a = left_minus3db_val.iloc[0]['Amplitude']
    x1b = left_minus3db_val.iloc[1]['Amplitude']
    y1 = y1a + (-reqvalAmpl - x1a) * (y1b - y1a) / (x1b - x1a)
    right_minus3db_val = minus3db_val[2:4]
    y3a = right_minus3db_val.iloc[0]['Frequency']
    y3b = right_minus3db_val.iloc[1]['Frequency']
    x3a = right_minus3db_val.iloc[0]['Amplitude']
    x3b = right_minus3db_val.iloc[1]['Amplitude']
    y3 = y3a + (-reqvalAmpl - x3a) * (y3b - y3a) / (x3b - x3a)
    self.bandwidth = y3-y1
    return (self.id_pos, np.int64(self.F_R), np.int64(self.bandwidth))

  def print_stats(self):
    id, fr, bw = self.create_stats()
    print("%s, %i, %i" % (id, fr, bw))
    #print("%s, %i, %i" % (self.id_pos, np.int64(self.F_R), np.int64(self.bandwidth)))

  def run_converter(self):
    self.read_csv()
    self.close_inputFile()
    self.save_tsv()
    if self.showPlot:
      self.show_plots()

  def run_stats(self):
    self.read_csv()
    #self.create_stats()
    self.print_stats()
