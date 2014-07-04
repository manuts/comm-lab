#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Wed Jul  2 17:15:58 2014
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from math import pi
from optparse import OptionParser
import numpy
import wx

class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 8
        self.nfilts = nfilts = 32
        self.constellation = constellation = digital.constellation_dqpsk()
        self.ntaps = ntaps = 11*nfilts*sps
        self.excess_bw = excess_bw = 0.35
        self.bps = bps = constellation.bits_per_symbol()
        self.tx_taps = tx_taps = filter.firdes.root_raised_cosine(nfilts, nfilts, 1.0, excess_bw, ntaps)
        self.timing_max_dev = timing_max_dev = 1.5
        self.timing_bw = timing_bw = 2*pi/100
        self.samp_rate = samp_rate = 1e6
        self.rx_taps = rx_taps = filter.firdes.root_raised_cosine(nfilts, nfilts*sps, 1.0, excess_bw, ntaps)
        self.phase_bw = phase_bw = 2*pi/100
        self.freq_bw = freq_bw = 2*pi/100
        self.fll_ntaps = fll_ntaps = 55
        self.arity = arity = pow(2, bps)

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate/sps,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=True,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0.win)
        self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
        	self.GetWin(),
        	title="Constellation Plot",
        	sample_rate=samp_rate/sps,
        	frame_rate=5,
        	const_size=2048,
        	M=4,
        	theta=0,
        	loop_bw=6.28/100.0,
        	fmax=0.06,
        	mu=0.5,
        	gain_mu=0.005,
        	symbol_rate=samp_rate/sps,
        	omega_limit=0.005,
        )
        self.Add(self.wxgui_constellationsink2_0.win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  sps,
                  taps=(tx_taps),
        	  flt_size=32)
        	
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab1")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab2")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "tab3")
        self.Add(self.notebook_0)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, timing_bw, (rx_taps), nfilts, nfilts//2, timing_max_dev, 1)
        self.digital_fll_band_edge_cc_0 = digital.fll_band_edge_cc(sps, excess_bw, fll_ntaps, freq_bw)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((constellation.points()), 1)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(bps, gr.GR_MSB_FIRST)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.2, ))
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, 256, 10000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.wxgui_constellationsink2_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.digital_fll_band_edge_cc_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))


# QT sink close method reimplementation

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rx_taps(filter.firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, self.ntaps))
        self.set_ntaps(11*self.nfilts*self.sps)
        self.pfb_arb_resampler_xxx_0.set_rate(self.sps)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate/self.sps)
        self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate/self.sps)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rx_taps(filter.firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, self.ntaps))
        self.set_ntaps(11*self.nfilts*self.sps)
        self.set_tx_taps(filter.firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.excess_bw, self.ntaps))

    def get_constellation(self):
        return self.constellation

    def set_constellation(self, constellation):
        self.constellation = constellation
        self.set_bps(self.constellation.bits_per_symbol())

    def get_ntaps(self):
        return self.ntaps

    def set_ntaps(self, ntaps):
        self.ntaps = ntaps
        self.set_rx_taps(filter.firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, self.ntaps))
        self.set_tx_taps(filter.firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.excess_bw, self.ntaps))

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.set_rx_taps(filter.firdes.root_raised_cosine(self.nfilts, self.nfilts*self.sps, 1.0, self.excess_bw, self.ntaps))
        self.set_tx_taps(filter.firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.excess_bw, self.ntaps))

    def get_bps(self):
        return self.bps

    def set_bps(self, bps):
        self.bps = bps
        self.set_arity(pow(2, self.bps))

    def get_tx_taps(self):
        return self.tx_taps

    def set_tx_taps(self, tx_taps):
        self.tx_taps = tx_taps
        self.pfb_arb_resampler_xxx_0.set_taps((self.tx_taps))

    def get_timing_max_dev(self):
        return self.timing_max_dev

    def set_timing_max_dev(self, timing_max_dev):
        self.timing_max_dev = timing_max_dev

    def get_timing_bw(self):
        return self.timing_bw

    def set_timing_bw(self, timing_bw):
        self.timing_bw = timing_bw
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_bw)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate/self.sps)
        self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate/self.sps)

    def get_rx_taps(self):
        return self.rx_taps

    def set_rx_taps(self, rx_taps):
        self.rx_taps = rx_taps
        self.digital_pfb_clock_sync_xxx_0.set_taps((self.rx_taps))

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw

    def get_freq_bw(self):
        return self.freq_bw

    def set_freq_bw(self, freq_bw):
        self.freq_bw = freq_bw
        self.digital_fll_band_edge_cc_0.set_loop_bandwidth(self.freq_bw)

    def get_fll_ntaps(self):
        return self.fll_ntaps

    def set_fll_ntaps(self, fll_ntaps):
        self.fll_ntaps = fll_ntaps

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = top_block()
    tb.Start(True)
    tb.Wait()

