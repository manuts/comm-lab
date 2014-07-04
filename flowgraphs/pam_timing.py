#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Pam Timing
# Generated: Wed Jul  2 10:28:36 2014
##################################################

from gnuradio import blocks
from gnuradio import channels
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.filter import pfb
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import numpy
import wx

class pam_timing(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Pam Timing")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.time_bw = time_bw = 0
        self.spb = spb = 4.2563
        self.sig_amp = sig_amp = 1
        self.samp_rate = samp_rate = 32000
        self.rolloff = rolloff = .35
        self.noise_amp = noise_amp = 0
        self.nfilts = nfilts = 32
        self.interpratio = interpratio = 1.00
        self.freq_offset = freq_offset = 0
        self.const = const = digital.qpsk_constellation()

        ##################################################
        # Blocks
        ##################################################
        _time_bw_sizer = wx.BoxSizer(wx.VERTICAL)
        self._time_bw_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_time_bw_sizer,
        	value=self.time_bw,
        	callback=self.set_time_bw,
        	label="Timing Loop BW",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._time_bw_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_time_bw_sizer,
        	value=self.time_bw,
        	callback=self.set_time_bw,
        	minimum=0,
        	maximum=0.1,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_time_bw_sizer, 1, 2, 1, 1)
        self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "error")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "phase")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "freq")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Resampled Signal")
        self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Scope")
        self.GridAdd(self.notebook_0, 1, 1, 5, 1)
        _noise_amp_sizer = wx.BoxSizer(wx.VERTICAL)
        self._noise_amp_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_noise_amp_sizer,
        	value=self.noise_amp,
        	callback=self.set_noise_amp,
        	label="Channel Noise",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._noise_amp_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_noise_amp_sizer,
        	value=self.noise_amp,
        	callback=self.set_noise_amp,
        	minimum=0,
        	maximum=1.0,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_noise_amp_sizer, 3, 2, 1, 1)
        _interpratio_sizer = wx.BoxSizer(wx.VERTICAL)
        self._interpratio_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_interpratio_sizer,
        	value=self.interpratio,
        	callback=self.set_interpratio,
        	label="Timing Offset",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._interpratio_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_interpratio_sizer,
        	value=self.interpratio,
        	callback=self.set_interpratio,
        	minimum=0.99,
        	maximum=1.01,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_interpratio_sizer, 2, 2, 1, 1)
        _freq_offset_sizer = wx.BoxSizer(wx.VERTICAL)
        self._freq_offset_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_freq_offset_sizer,
        	value=self.freq_offset,
        	callback=self.set_freq_offset,
        	label="Frequency Offset",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._freq_offset_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_freq_offset_sizer,
        	value=self.freq_offset,
        	callback=self.set_freq_offset,
        	minimum=-0.5,
        	maximum=0.5,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.GridAdd(_freq_offset_sizer, 4, 2, 1, 1)
        self.wxgui_scopesink2_0_0_1 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(3).GetWin(),
        	title="Error",
        	sample_rate=samp_rate,
        	v_scale=.5,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(3).Add(self.wxgui_scopesink2_0_0_1.win)
        self.wxgui_scopesink2_0_0_0_0 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(2).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=1.25,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(2).Add(self.wxgui_scopesink2_0_0_0_0.win)
        self.wxgui_scopesink2_0_0_0 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(1).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=9,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(1).Add(self.wxgui_scopesink2_0_0_0.win)
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_f(
        	self.notebook_0.GetPage(0).GetWin(),
        	title="Error",
        	sample_rate=samp_rate,
        	v_scale=3,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(0).Add(self.wxgui_scopesink2_0_0.win)
        self.wxgui_scopesink2_0 = scopesink2.scope_sink_c(
        	self.notebook_0.GetPage(4).GetWin(),
        	title="Scope Plot",
        	sample_rate=samp_rate,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.notebook_0.GetPage(4).Add(self.wxgui_scopesink2_0.win)
        self.pfb_arb_resampler_xxx_0 = pfb.arb_resampler_ccf(
        	  spb,
                  taps=(firdes.root_raised_cosine(nfilts, nfilts, 1.0, rolloff, 44*nfilts)),
        	  flt_size=32)
        	
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(spb, time_bw, (firdes.root_raised_cosine(nfilts, nfilts*spb, 1.0, rolloff, 44*nfilts)), nfilts, 16, 1.5, 1)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((const.points()), 1)
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise_amp,
        	frequency_offset=freq_offset,
        	epsilon=interpratio,
        	taps=(1.0, ),
        	noise_seed=42,
        	block_tags=False
        )
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((sig_amp, ))
        self.analog_random_source_x = blocks.vector_source_b(map(int, numpy.random.randint(0, const.arity(), 10000000)), True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_throttle_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 2), (self.wxgui_scopesink2_0_0_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.wxgui_scopesink2_0_0_1, 0))
        self.connect((self.pfb_arb_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.pfb_arb_resampler_xxx_0, 0))
        self.connect((self.analog_random_source_x, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 3), (self.wxgui_scopesink2_0_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 1), (self.wxgui_scopesink2_0_0, 0))
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.wxgui_scopesink2_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.channels_channel_model_0, 0))


# QT sink close method reimplementation

    def get_time_bw(self):
        return self.time_bw

    def set_time_bw(self, time_bw):
        self.time_bw = time_bw
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.time_bw)
        self._time_bw_slider.set_value(self.time_bw)
        self._time_bw_text_box.set_value(self.time_bw)

    def get_spb(self):
        return self.spb

    def set_spb(self, spb):
        self.spb = spb
        self.digital_pfb_clock_sync_xxx_0.set_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts*self.spb, 1.0, self.rolloff, 44*self.nfilts)))
        self.pfb_arb_resampler_xxx_0.set_rate(self.spb)

    def get_sig_amp(self):
        return self.sig_amp

    def set_sig_amp(self, sig_amp):
        self.sig_amp = sig_amp
        self.blocks_multiply_const_vxx_0.set_k((self.sig_amp, ))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0_1.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0_0_0_0.set_sample_rate(self.samp_rate)
        self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.digital_pfb_clock_sync_xxx_0.set_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts*self.spb, 1.0, self.rolloff, 44*self.nfilts)))
        self.pfb_arb_resampler_xxx_0.set_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.rolloff, 44*self.nfilts)))

    def get_noise_amp(self):
        return self.noise_amp

    def set_noise_amp(self, noise_amp):
        self.noise_amp = noise_amp
        self.channels_channel_model_0.set_noise_voltage(self.noise_amp)
        self._noise_amp_slider.set_value(self.noise_amp)
        self._noise_amp_text_box.set_value(self.noise_amp)

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.digital_pfb_clock_sync_xxx_0.set_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts*self.spb, 1.0, self.rolloff, 44*self.nfilts)))
        self.pfb_arb_resampler_xxx_0.set_taps((firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0, self.rolloff, 44*self.nfilts)))

    def get_interpratio(self):
        return self.interpratio

    def set_interpratio(self, interpratio):
        self.interpratio = interpratio
        self.channels_channel_model_0.set_timing_offset(self.interpratio)
        self._interpratio_slider.set_value(self.interpratio)
        self._interpratio_text_box.set_value(self.interpratio)

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)
        self._freq_offset_slider.set_value(self.freq_offset)
        self._freq_offset_text_box.set_value(self.freq_offset)

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const

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
    tb = pam_timing()
    tb.Start(True)
    tb.Wait()

