#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Hdf5 Source Test
# Generated: Sun Oct 29 14:29:36 2017
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from hdf5.hdf5_source_x import hdf5_source_b
from hdf5.hdf5_source_x import hdf5_source_f
from hdf5.hdf5_source_x import hdf5_source_i
from hdf5.hdf5_source_x import hdf5_source_s
from optparse import OptionParser
import logging
import sip
import sys
from gnuradio import qtgui


class hdf5_source_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Hdf5 Source Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Hdf5 Source Test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "hdf5_source_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 32000
        self.data_filename = data_filename = "/tmp/dataset.hdf5"

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            4
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("")

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(4):
            self.qtgui_number_sink_0.set_min(i, -1000)
            self.qtgui_number_sink_0.set_max(i, 1000)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_0_win)
        self.hdf5_source_x_0_2 = hdf5_source_f(
        		num_outputs=1,
        		dataset_name='dataset_f',
        		data_filename=data_filename,
        		log_level=logging.NOTSET,
        		log_filename=''
        	)
        self.hdf5_source_x_0_1 = hdf5_source_i(
        		num_outputs=1,
        		dataset_name='dataset_i',
        		data_filename=data_filename,
        		log_level=logging.NOTSET,
        		log_filename=''
        	)
        self.hdf5_source_x_0_0 = hdf5_source_s(
        		num_outputs=1,
        		dataset_name='dataset_s',
        		data_filename=data_filename,
        		log_level=logging.NOTSET,
        		log_filename=''
        	)
        self.hdf5_source_x_0 = hdf5_source_b(
        		num_outputs=1,
        		dataset_name='dataset_b',
        		data_filename=data_filename,
        		log_level=logging.NOTSET,
        		log_filename=''
        	)
        self.blocks_short_to_float_0 = blocks.short_to_float(1, 255)
        self.blocks_int_to_float_0 = blocks.int_to_float(1, 1)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_char_to_float_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blocks_int_to_float_0, 0), (self.qtgui_number_sink_0, 2))
        self.connect((self.blocks_short_to_float_0, 0), (self.qtgui_number_sink_0, 1))
        self.connect((self.hdf5_source_x_0, 0), (self.blocks_char_to_float_0, 0))
        self.connect((self.hdf5_source_x_0_0, 0), (self.blocks_short_to_float_0, 0))
        self.connect((self.hdf5_source_x_0_1, 0), (self.blocks_int_to_float_0, 0))
        self.connect((self.hdf5_source_x_0_2, 0), (self.qtgui_number_sink_0, 3))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "hdf5_source_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_data_filename(self):
        return self.data_filename

    def set_data_filename(self, data_filename):
        self.data_filename = data_filename


def main(top_block_cls=hdf5_source_test, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
