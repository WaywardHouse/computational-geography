#!/usr/bin/env python3
"""Per-figure layout fixes that need judgment (idempotent: each edit asserts old text present or already applied)."""
import re,sys
H=' paint-order="stroke" stroke="%s" stroke-width="5" stroke-linejoin="round"'
def patch(path, edits):
    t=open(path,encoding="utf8").read(); o=t
    for old,new in edits:
        if old.startswith("re:"):
            if re.search(old[3:],t): t=re.sub(old[3:],new,t,count=1)
            continue
        if new in t and old not in t: continue
        if old not in t: print("MISSING in",path,":",old[:70]); continue
        t=t.replace(old,new,1)
    if t!=o: open(path,"w",encoding="utf8").write(t); print("patched",path)
def sub(path, pairs):  # regex subs
    t=open(path,encoding="utf8").read(); o=t
    for pat,rep in pairs: t=re.sub(pat,rep,t,count=1)
    if t!=o: open(path,"w",encoding="utf8").write(t); print("patched",path)

# earth-as-rotating-sphere: move explanatory sentences to a caption block below the sphere
p="foundations/earth-as-rotating-sphere.qmd"
patch(p,[
 ('viewBox="0 0 560 320"','viewBox="0 0 560 416"'),
 ('<rect x="24" y="18" width="512" height="284"','<rect x="24" y="18" width="512" height="382"'),
 ('viewBox="0 0 560 400"','viewBox="0 0 560 416"'),
 ('<rect x="24" y="18" width="512" height="364"','<rect x="24" y="18" width="512" height="382"'),
 ('<text x="350" y="72" font-size="15" fill="#5a5a56">north pole','<text x="240" y="40" font-size="15" fill="#5a5a56">north pole'),
 ('<text x="126" y="116" font-size="15"','<text x="34" y="92" font-size="14"'),
 ('<text x="111" y="118" font-size="16"','<text x="48" y="324" font-size="15"'),
 ('<text x="245" y="150" font-size="16"','<text x="48" y="344" font-size="15"'),
 ('<text x="325" y="182" font-size="16"','<text x="48" y="364" font-size="15"'),
 ('<text x="206" y="214" font-size="16"','<text x="48" y="384" font-size="15"'),
])
# sar-fundamentals
p="advanced-remote-sensing/sar-fundamentals.qmd"
patch(p,[
 ('<line x1="120" y1="45" x2="138" y2="45"','<line x1="330" y1="45" x2="348" y2="45"'),
 ('<text x="145" y="50" font-size="16" fill="#a64b2a">','<text x="355" y="50" font-size="16" fill="#a64b2a">'),
 ('<line x1="120" y1="120" x2="438" y2="120"','<line x1="120" y1="140" x2="438" y2="140"'),
 ('points="120,120 132,114 132,126"','points="120,140 132,134 132,146"'),
 ('points="438,120 426,114 426,126"','points="438,140 426,134 426,146"'),
 ('<text x="188" y="114" font-size="17"','<text x="188" y="134" font-size="17"'),
 ('<text x="420" y="150" font-size="16" fill="#1f6f66">','<text x="420" y="166" font-size="16" fill="#1f6f66">'),
 ('<text x="92" y="96" font-size="14"','<text x="122" y="96" text-anchor="end" font-size="14"'),
 ('<text x="192" y="96" font-size="14"','<text x="240" y="96" text-anchor="end" font-size="14"'),
 ('<text x="292" y="96" font-size="14"','<text x="322" y="96" text-anchor="end" font-size="14"'),
 ('<text x="392" y="96" font-size="14"','<text x="412" y="96" text-anchor="end" font-size="14"'),
])
# boundary-layer-turbulence
p="atmospheric-hazards/boundary-layer-turbulence.qmd"
patch(p,[
 ('<text x="423" y="72" font-size="18"','<text x="140" y="70" font-size="18"'),
 ('<text x="486" y="95" font-size="16"','<text x="140" y="94" font-size="16"'),
 ('<text x="338" y="110" font-size="18"','<text x="330" y="44" font-size="18"'),
 ('<text x="647" y="135"','<text x="612" y="123"'),
 ('<text x="656" y="210"','<text x="612" y="230"'),
 ('<text x="545" y="228" font-size="15"','<text x="500" y="250" font-size="15"'),
])
# thunderstorm-dynamics
p="atmospheric-hazards/thunderstorm-dynamics.qmd"
patch(p,[
 ('viewBox="0 0 560 300"','viewBox="0 0 560 318"'),
 ('width="560" height="300" rx="22"','width="560" height="318" rx="22"'),
 ('<text x="208" y="78" font-size="19"','<text x="290" y="34" font-size="19"'),
 ('<text x="188" y="98" font-size="15"','<text x="290" y="53" font-size="15"'),
 ('<text x="354" y="64" font-size="17"','<text x="405" y="80" font-size="17"'),
 ('<text x="66" y="62" font-size="17" fill="#224f9c" font-weight="700">winds strengthen and turn with height</text>',
  '<text x="26" y="30" font-size="17" fill="#224f9c" font-weight="700"><tspan x="26">winds strengthen and turn</tspan><tspan x="26" dy="1.2em">with height</tspan></text>'),
 ('<text x="78" y="280"','<text x="78" y="276"'),
])

# thunderstorm caption nudge
patch("atmospheric-hazards/thunderstorm-dynamics.qmd",[('<text x="290" y="53" font-size="15"','<text x="290" y="57" font-size="15"')])

# prospect-leaf-optical-properties: widen frame, shorten exit arrows, labels beside arrows
patch("advanced-remote-sensing/prospect-leaf-optical-properties.qmd",[
 ('viewBox="0 0 560 320"','viewBox="0 0 640 320"'),
 ('width="560" height="320" rx="22" fill="#f4f8ef"','width="640" height="320" rx="22" fill="#f4f8ef"'),
 ('<line x1="404" y1="142" x2="486" y2="102"','<line x1="404" y1="142" x2="440" y2="114"'),
 ('<line x1="404" y1="208" x2="486" y2="242"','<line x1="404" y1="208" x2="440" y2="228"'),
 ('<text x="420" y="84" font-size="15" fill="#92400e">','<text x="180" y="82" font-size="14" fill="#92400e">'),
 ('<text x="420" y="122" font-size="15"','<text x="456" y="144" font-size="15"'),
 ('<text x="420" y="178" font-size="15"','<text x="456" y="182" font-size="15"'),
 ('<text x="420" y="244" font-size="15" fill="#92400e">','<text x="180" y="243" font-size="14" fill="#92400e">'),
 ('<text x="412" y="92" font-size="14"','<text x="448" y="112" font-size="14"'),
 ('<text x="436" y="262" font-size="14"','<text x="448" y="238" font-size="14"'),
])
# hail
patch("atmospheric-hazards/hail-formation-forecasting.qmd",[
 ('viewBox="0 0 560 300"','viewBox="0 0 560 322"'),
 ('width="560" height="300" rx="22"','width="560" height="322" rx="22"'),
 ('<text x="278" y="147" font-size="15"','<text x="316" y="122" font-size="15"'),
])
# tornado
patch("atmospheric-hazards/tornado-formation-intensity.qmd",[
 ('<text x="224" y="92" font-size="18" fill="#1f6f66" font-weight="700">updraft tilts rotation upright</text>',
  '<text x="228" y="190" font-size="16" fill="#1f6f66" font-weight="700"><tspan x="228">updraft tilts</tspan><tspan x="228" dy="1.2em">rotation upright</tspan></text>'),
 ('<text x="374" y="48"','<text x="340" y="36"'),
 ('<text x="349" y="66" font-size="18"','<text x="372" y="56" font-size="18"'),
])
# avalanche
patch("cryosphere-and-mountain-systems/avalanche-terrain-analysis.qmd",[
 ('<text x="247" y="270" font-size="16"','<text x="74" y="290" font-size="16"'),
 ('<text x="418" y="234" font-size="18"','<text x="322" y="236" font-size="18"'),
])

patch("advanced-remote-sensing/prospect-leaf-optical-properties.qmd",[
 ('re:<text x="420" y="244" font-size="15" fill="#92400e"([^>]*)>', r'<text x="180" y="243" font-size="14" fill="#92400e"\1>'),
])
patch("atmospheric-hazards/tornado-formation-intensity.qmd",[
 ('re:<text x="224" y="92"[^>]*>updraft tilts rotation upright</text>',
  '<text x="228" y="190" font-size="16" fill="#1f6f66" font-weight="700"><tspan x="228">updraft tilts</tspan><tspan x="228" dy="1.2em">rotation upright</tspan></text>'),
])

patch("atmospheric-hazards/tornado-formation-intensity.qmd",[
 ('re:<text x="372" y="56" font-size="18"', '<text x="546" y="56" text-anchor="end" font-size="18"'),
])
patch("atmospheric-hazards/hail-formation-forecasting.qmd",[
 ('<text x="316" y="122" font-size="15"','<text x="310" y="122" font-size="14"'),
])

# glacial-lake-outburst-floods
patch("cryosphere-and-mountain-systems/glacial-lake-outburst-floods.qmd",[
 ('<rect x="66" y="262" width="430" height="32" rx="12"','<rect x="60" y="256" width="468" height="54" rx="12"'),
 ('re:<text x="88" y="283" font-size="15"','<text x="76" y="278" font-size="14"'),
 ('re:<tspan x="88"','<tspan x="76"'),
 ('re:<tspan x="88" dy','<tspan x="76" dy'),
 ('<text x="230" y="154" font-size="16"','<text x="232" y="148" font-size="16"'),
 ('<text x="286" y="170" font-size="16"','<text x="292" y="176" font-size="16"'),
])
# glacial-meltwater-chemistry
patch("cryosphere-and-mountain-systems/glacial-meltwater-chemistry.qmd",[
 ('<rect x="72" y="262" width="270" height="32" rx="12"','<rect x="72" y="262" width="420" height="32" rx="12"'),
 ('<text x="312" y="88" font-size="18"','<text x="440" y="78" font-size="18"'),
 ('<text x="306" y="118" font-size="15"','<text x="330" y="104" font-size="15"'),
 ('<text x="289" y="246" font-size="15"','<text x="356" y="207" font-size="14"'),
])
# permafrost-thaw-geohazards
patch("cryosphere-and-mountain-systems/permafrost-thaw-geohazards.qmd",[
 ('<text x="308" y="90" font-size="15"','<text x="196" y="92" font-size="15"'),
 ('<text x="321" y="144" font-size="16"','<text x="321" y="140" font-size="16"'),
 ('<text x="74" y="206" font-size="18"','<text x="74" y="262" font-size="18"'),
])
# decomposition-and-soil-carbon
patch("environmental-systems/decomposition-and-soil-carbon.qmd",[
 ('<rect x="88" y="232" width="380" height="50" rx="14"','<rect x="24" y="232" width="512" height="50" rx="14"'),
 ('<text x="172" y="140" font-size="14"','<text x="112" y="208" font-size="14"'),
 ('<text x="344" y="130" font-size="14"','<text x="290" y="208" font-size="14"'),
 ('<text x="10" y="142" font-size="14"','<text x="8" y="116" font-size="14"'),
 ('re:<text x="33" y="260" font-size="16"','<text x="48" y="262" font-size="16"'),
])

patch("cryosphere-and-mountain-systems/glacial-meltwater-chemistry.qmd",[
 ('re:<text x="356" y="207" font-size="14"([^>]*)>subglacial: long contact, high solutes</text>',
  r'<text x="366" y="205" font-size="14"\1><tspan x="366">subglacial: long contact,</tspan><tspan x="366" dy="1.2em">high solutes</tspan></text>'),
 ('re:<text x="410" y="274" font-size="16"','<text x="420" y="224" font-size="16"'),
])
patch("environmental-systems/decomposition-and-soil-carbon.qmd",[
 ('re:<text x="48" y="262" font-size="16"','<text x="48" y="262" font-size="14"'),
])

# multispectral-imagery-and-band-interpretation: caption below the mapping lines
patch("environmental-systems/multispectral-imagery-and-band-interpretation.qmd",[
 ('re:<text x="239" y="88" font-size="15"','<text x="120" y="212" font-size="15"'),
])
# net-radiation-and-albedo
p="environmental-systems/net-radiation-and-albedo.qmd"
patch(p,[
 ('viewBox="0 0 560 300"','viewBox="0 0 560 320"'),
 ('width="560" height="300" rx="22"','width="560" height="320" rx="22"'),
 ('re:<text x="158" y="132" font-size="18" fill="#9b6d00" font-weight="700"([^>]*)>incoming shortwave</text>',
  r'<text x="30" y="150" font-size="16" fill="#9b6d00" font-weight="700"\1><tspan x="30">incoming</tspan><tspan x="30" dy="1.15em">shortwave</tspan></text>'),
 ('re:<text x="264" y="138" font-size="18" fill="#1f6f66" font-weight="700"([^>]*)>reflected shortwave</text>',
  r'<text x="218" y="108" font-size="16" fill="#1f6f66" font-weight="700"\1><tspan x="218">reflected</tspan><tspan x="218" dy="1.15em">shortwave</tspan></text>'),
 ('re:<text x="349" y="102" font-size="18"','<text x="372" y="60" font-size="16"'),
 ('re:<text x="292" y="218" font-size="18" fill="#8b386a" font-weight="700"([^>]*)>outgoing longwave</text>',
  r'<text x="452" y="162" font-size="16" fill="#8b386a" font-weight="700"\1><tspan x="452">outgoing</tspan><tspan x="452" dy="1.15em">longwave</tspan></text>'),
])
# nitrogen-cycling
patch("environmental-systems/nitrogen-cycling.qmd",[
 ('<text x="170" y="126" font-size="14"','<text x="190" y="98" font-size="14"'),
 ('<text x="380" y="124" font-size="14"','<text x="344" y="98" font-size="14"'),
 ('<text x="86" y="156" font-size="14" fill="#166534">soil organic matter and litter','<text x="70" y="156" font-size="14" fill="#166534">organic matter, litter'),
 ('re:<text x="240" y="284" font-size="14"','<text x="236" y="284" font-size="13"'),
])
# sensible-and-latent-heat-fluxes
patch("environmental-systems/sensible-and-latent-heat-fluxes.qmd",[
 ('re:<text x="84" y="184" font-size="18"','<text x="215" y="92" font-size="18"'),
 ('re:<text x="140" y="292" font-size="18"','<text x="116" y="292" font-size="18"'),
 ('re:<text x="528" y="292" font-size="18"','<text x="470" y="292" font-size="18"'),
 ('re:<text x="74" y="138" font-size="16"','<text x="160" y="200" text-anchor="end" font-size="16"'),
 ('re:<text x="72" y="162" font-size="16"','<text x="160" y="222" text-anchor="end" font-size="16"'),
 ('re:<text x="470" y="132" font-size="16"','<text x="742" y="34" text-anchor="end" font-size="16"'),
 ('re:<text x="488" y="156" font-size="16"','<text x="742" y="56" text-anchor="end" font-size="16"'),
 ('re:<text x="520" y="180" font-size="16"','<text x="742" y="78" text-anchor="end" font-size="16"'),
])

# soil-moisture-dynamics: caption below, drainage label beside its arrow
patch("environmental-systems/soil-moisture-dynamics.qmd",[
 ('viewBox="0 0 560 320"','viewBox="0 0 560 350"'),
 ('width="560" height="320" rx="22" fill="#eef4ef"','width="560" height="350" rx="22" fill="#eef4ef"'),
 ('re:<text x="256" y="292" font-size="18"','<text x="246" y="292" font-size="18"'),
 ('re:<text x="76" y="276" font-size="16"','<text x="76" y="322" font-size="16"'),
 ('re:<text x="76" y="296" font-size="16"','<text x="76" y="342" font-size="16"'),
])
# temperature-moisture-gradients
patch("environmental-systems/temperature-moisture-gradients.qmd",[
 ('re:<text x="214" y="124" font-size="16"','<text x="130" y="112" font-size="16"'),
 ('re:<text x="144" y="198" font-size="14" fill="#6d28d9"([^>]*)>warm lid blocks vertical mixing</text>',
  r'<text x="128" y="178" font-size="14" fill="#6d28d9"\1><tspan x="128">warm lid blocks</tspan><tspan x="128" dy="1.15em">vertical mixing</tspan></text>'),
 ('re:<text x="444" y="123" font-size="15"','<text x="520" y="228" font-size="15"'),
 ('re:<text x="548" y="114" font-size="15"','<text x="466" y="108" font-size="15"'),
 ('re:<text x="510" y="138" font-size="15" fill="#0369a1"([^>]*)>cloud base / LCL</text>',
  r'<text x="616" y="150" font-size="14" fill="#0369a1"\1><tspan x="616">cloud base</tspan><tspan x="616" dy="1.15em">/ LCL</tspan></text>'),
])
# wind-profiles-and-turbulence
patch("environmental-systems/wind-profiles-and-turbulence.qmd",[
 ('re:<text x="434" y="292" font-size="15"','<text x="466" y="254" font-size="15"'),
 ('re:<text x="112" y="286" font-size="15" fill="#35515f"([^>]*)>short grass / snow / smooth soil</text>',
  r'<text x="96" y="284" font-size="14" fill="#35515f"\1><tspan x="96">short grass / snow /</tspan><tspan x="96" dy="1.15em">smooth soil</tspan></text>'),
 ('re:<text x="296" y="286" font-size="15" fill="#35515f"([^>]*)>forest / shrubland / urban roughness</text>',
  r'<text x="296" y="284" font-size="14" fill="#35515f"\1><tspan x="296">forest / shrubland /</tspan><tspan x="296" dy="1.15em">urban roughness</tspan></text>'),
])
# gravity-models-trade-migration
patch("foundations/gravity-models-trade-migration.qmd",[
 ('re:<text x="146" y="116" font-size="16"','<text x="118" y="94" font-size="16"'),
 ('re:<text x="166" y="136" font-size="14"','<text x="118" y="112" font-size="13"'),
])
# spectral-mixing-and-sensor-response
patch("foundations/spectral-mixing-and-sensor-response.qmd",[
 ('<text x="160" y="238" font-size="16"','<text x="186" y="238" font-size="16"'),
 ('<text x="448" y="104" text-anchor="middle" font-size="16"','<text x="448" y="98" text-anchor="middle" font-size="16"'),
])
# spatial-spectral-temporal-and-radiometric-resolution (figure 2) and pca-tsne-umap (figure 3): small canvases
patch("foundations/spatial-spectral-temporal-and-radiometric-resolution.qmd",[
 ('<text x="70" y="124" text-anchor="middle" font-size="12" fill="#5a5a56">wide bands blur detail</text>',
  '<text x="62" y="120" text-anchor="middle" font-size="12" fill="#5a5a56"><tspan x="62">wide bands</tspan><tspan x="62" dy="1.2em">blur detail</tspan></text>'),
 ('re:<text x="162" y="124" text-anchor="middle" font-size="12" fill="#5a5a56"><tspan x="162">narrow bands</tspan><tspan x="162" dy="1.2em">keep features</tspan></text>',
  '<text x="160" y="120" text-anchor="middle" font-size="12" fill="#5a5a56"><tspan x="160">narrow bands</tspan><tspan x="160" dy="1.2em">keep features</tspan></text>'),
])
patch("machine-learning/dimensionality-reduction-pca-tsne-umap.qmd",[
 ('re:<text x="26" y="100" font-size="12" fill="#446b5a">local groups on a broader shape</text>',
  '<text x="20" y="88" font-size="12" fill="#446b5a"><tspan x="20">local groups on</tspan><tspan x="20" dy="1.2em">a broader shape</tspan></text>'),
])
# photosynthesis-light-response: y-axis label fully inside canvas; semi-transparent zone rects must sit under the labels
p="environmental-systems/photosynthesis-light-response.qmd"
patch(p,[('rotate(-90 28 118)','rotate(-90 28 150)'),('x="28" y="118" font-size="15"','x="28" y="150" font-size="15"')])
t=open(p,encoding="utf8").read()
m=re.search(r'(  <rect x="96" y="88"[^\n]*\n  <rect x="170" y="88"[^\n]*\n  <rect x="300" y="88"[^\n]*\n)',t)
if m:
    blk=m.group(1); t=t.replace(blk,"",1)
    anchor='stroke="#91a49a" stroke-width="3"/>\n'
    t=t.replace(anchor,anchor+blk,1); open(p,"w",encoding="utf8").write(t); print("reordered",p)

def halo(path, snippet):
    """Add a background-coloured outline to <text> elements INSIDE <svg> blocks whose content contains `snippet`
    (bg = first rect fill of that figure). Prose outside <svg> is never touched."""
    t=open(path,encoding="utf8").read(); n=[0]
    def fig(m):
        s=m.group(0); mm=re.search(r'<rect[^>]*fill="(#[0-9a-fA-F]{3,6})"',s); bg=mm[1] if mm else "#ffffff"
        def txt(m2):
            if snippet in m2[2] and "paint-order" not in m2[1]:
                n[0]+=1
                return m2[1][:-1]+f' paint-order="stroke" stroke="{bg}" stroke-width="5" stroke-linejoin="round">'+m2[2]+"</text>"
            return m2[0]
        return re.sub(r"(<text\b[^>]*>)(.*?)</text>",txt,s,flags=re.S)
    t2=re.sub(r"<svg\b.*?</svg>",fig,t,flags=re.S)
    if t2!=t: open(path,"w",encoding="utf8").write(t2); print("halo",path,snippet[:30],n[0])
halo("advanced-remote-sensing/sail-canopy-reflectance.qmd","hotspot when view aligns")
halo("atmospheric-hazards/fire-weather-ignition.qmd","ignition + spread")
halo("atmospheric-hazards/tornado-formation-intensity.qmd","updraft tilts<")
halo("environmental-systems/nitrogen-cycling.qmd","mineralization")
halo("environmental-systems/soil-heat-diffusion.qmd","much smaller")
patch("cryosphere-and-mountain-systems/glacial-meltwater-chemistry.qmd",[
 ('re:<text x="420" y="224" font-size="16"','<text x="530" y="236" text-anchor="end" font-size="16"'),
])
patch("environmental-systems/temperature-moisture-gradients.qmd",[
 ('re:<text x="616" y="150" font-size="14"','<text x="616" y="126" font-size="14"'),
 ('re:<tspan x="616">cloud base','<tspan x="616">cloud base'),
])

# soil-heat-diffusion: wider canvas/panels, curve labels at curve ends, two-line captions
patch("environmental-systems/soil-heat-diffusion.qmd",[
 ('viewBox="0 0 760 360"','viewBox="0 0 800 360"'),
 ('width="760" height="360" fill="#fbfcff"','width="800" height="360" fill="#fbfcff"'),
 ('<rect x="54" y="70" width="318" height="230" rx="18"','<rect x="54" y="70" width="344" height="252" rx="18"'),
 ('<rect x="410" y="70" width="296" height="230" rx="18"','<rect x="410" y="70" width="350" height="252" rx="18"'),
 ('re:<text x="256" y="150" font-size="15"','<text x="348" y="210" font-size="15"'),
 ('re:<text x="278" y="205" font-size="15"','<text x="348" y="229" font-size="15"'),
 ('re:<text x="286" y="235" font-size="15"','<text x="348" y="248" font-size="15"'),
 ('re:<text x="126" y="284" font-size="15" fill="#475569"([^>]*)>same cycle, smaller amplitude, later peak</text>',
  r'<text x="78" y="288" font-size="14" fill="#475569"\1><tspan x="78">same cycle, smaller amplitude,</tspan><tspan x="78" dy="1.2em">later peak</tspan></text>'),
 ('re:<text x="654" y="220" font-size="14"','<text x="678" y="220" font-size="14"'),
 ('re:<text x="401" y="286" font-size="15" fill="#475569"([^>]*)>depth increases downward as the wave damps out</text>',
  r'<text x="436" y="288" font-size="14" fill="#475569"\1><tspan x="436">depth increases downward</tspan><tspan x="436" dy="1.2em">as the wave damps out</tspan></text>'),
])

patch("environmental-systems/soil-heat-diffusion.qmd",[
 ('re:<text x="348" y="229" font-size="15"','<text x="348" y="232" font-size="15"'),
 ('re:<text x="348" y="248" font-size="15"','<text x="348" y="254" font-size="15"'),
])
patch("cryosphere-and-mountain-systems/glacial-meltwater-chemistry.qmd",[
 ('re:<text x="530" y="236" text-anchor="end"','<text x="530" y="242" text-anchor="end"'),
])

patch("environmental-systems/soil-heat-diffusion.qmd",[
 ('re:<text x="348" y="210" font-size="15"','<text x="348" y="206" font-size="15"'),
 ('re:<text x="348" y="254" font-size="15"','<text x="348" y="257" font-size="15"'),
])
