#############################################################################
# Generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#  Jan 12, 2022 09:21:12 AM CET  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set desc "-family {Segoe UI} -size 9"
set vTcl(actual_gui_font_dft_desc) $desc
set vTcl(actual_gui_font_dft_name) [font create {*}$desc]
set desc "-family {Segoe UI} -size 9"
set vTcl(actual_gui_font_text_desc) $desc
set vTcl(actual_gui_font_text_name) [font create {*}$desc]
set desc "-family {Courier New} -size 10"
set vTcl(actual_gui_font_fixed_desc) $desc
set vTcl(actual_gui_font_fixed_name) [font create {*}$desc]
set desc "-family {Segoe UI} -size 9"
set vTcl(actual_gui_font_menu_desc) $desc
set vTcl(actual_gui_font_menu_name) [font create {*}$desc]
set desc "-family {Segoe UI} -size 9"
set vTcl(actual_gui_font_tooltip_desc) $desc
set vTcl(actual_gui_font_tooltip_name) [font create {*}$desc]
set desc "-family {Segoe UI} -size 9"
set vTcl(actual_gui_font_treeview_desc) $desc
set vTcl(actual_gui_font_treeview_name) [font create {*}$desc]
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Absolute
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1317x467+-40+87
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 2110 1418
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Station météo"
    vTcl:DefineAlias "$top" "MainWindow" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra45 \
        -borderwidth 2 -relief sunken -background $vTcl(actual_gui_bg) \
        -height 25 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 1095 
    vTcl:DefineAlias "$top.fra45" "FrameEtat" vTcl:WidgetProc "MainWindow" 1
    set site_3_0 $top.fra45
    message $site_3_0.mes46 \
        -background $vTcl(actual_gui_bg) -font {-family {Segoe UI} -size 9} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {État :} -width 60 
    vTcl:DefineAlias "$site_3_0.mes46" "MsgEtat" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab47 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Mesures en cours ...} 
    vTcl:DefineAlias "$site_3_0.lab47" "Etat" vTcl:WidgetProc "MainWindow" 1
    place $site_3_0.mes46 \
        -in $site_3_0 -x 3 -y 2 -width 40 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $site_3_0.lab47 \
        -in $site_3_0 -x 40 -y 4 -width 468 -relwidth 0 -height 17 \
        -relheight 0 -anchor nw -bordermode ignore 
    labelframe $top.lab66 \
        \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground black -text {Mesures électriques} \
        -background $vTcl(actual_gui_bg) -height 405 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 500 
    vTcl:DefineAlias "$top.lab66" "FrameEMes" vTcl:WidgetProc "MainWindow" 1
    set site_3_0 $top.lab66
    message $site_3_0.mes77 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Girouette -width 80 
    vTcl:DefineAlias "$site_3_0.mes77" "MsgEGirouette" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab78 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text {9,999 V} 
    vTcl:DefineAlias "$site_3_0.lab78" "EGirouette" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes79 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Anémomètre -width 80 
    vTcl:DefineAlias "$site_3_0.mes79" "MsgEAnemometre" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab81 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text 0 
    vTcl:DefineAlias "$site_3_0.lab81" "EAnemometre" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes82 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Thermomètre -width 80 
    vTcl:DefineAlias "$site_3_0.mes82" "MsgEThermometre" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab83 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text {9,999 V} 
    vTcl:DefineAlias "$site_3_0.lab83" "EThermometre" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes84 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Luxmètre -width 80 
    vTcl:DefineAlias "$site_3_0.mes84" "MsgELuxmetre" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab85 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text {9,999 V} 
    vTcl:DefineAlias "$site_3_0.lab85" "ELuxmetre" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes87 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Humidimètre -width 80 
    vTcl:DefineAlias "$site_3_0.mes87" "MsgEHumidimetre" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab88 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text {999 Hz} 
    vTcl:DefineAlias "$site_3_0.lab88" "EHumidimetre" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes89 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Pluviomètre -width 80 
    vTcl:DefineAlias "$site_3_0.mes89" "MsgEPluviometre" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab90 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text 0 
    vTcl:DefineAlias "$site_3_0.lab90" "EPluviometre" vTcl:WidgetProc "MainWindow" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $site_3_0.tBu91 \
        -takefocus {} -text 0 
    vTcl:DefineAlias "$site_3_0.tBu91" "BtnReset" vTcl:WidgetProc "MainWindow" 1
    bind $site_3_0.tBu91 <Button-1> {
        lambda e: GUIBtnReset(e)
    }
    message $site_3_0.mes92 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Encodeur -width 80 
    vTcl:DefineAlias "$site_3_0.mes92" "MsgEEncodeur" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab93 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text 0 
    vTcl:DefineAlias "$site_3_0.lab93" "EEncodeur" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab94 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief raised 
    vTcl:DefineAlias "$site_3_0.lab94" "EP1_0" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab95 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief raised 
    vTcl:DefineAlias "$site_3_0.lab95" "EP1_3" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab96 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief raised 
    vTcl:DefineAlias "$site_3_0.lab96" "EP1_2" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab97 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font $vTcl(actual_gui_font_dft_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief raised 
    vTcl:DefineAlias "$site_3_0.lab97" "EP1_1" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes98 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Durée mesures} -width 90 
    vTcl:DefineAlias "$site_3_0.mes98" "MsgEDureeMesures" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab99 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text {9999 ms} 
    vTcl:DefineAlias "$site_3_0.lab99" "EDureeMesures" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes102 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Temps de boucle rapide} -width 140 
    vTcl:DefineAlias "$site_3_0.mes102" "MsgETempsBoucleR" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab103 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text {9999 ms} 
    vTcl:DefineAlias "$site_3_0.lab103" "ETempsBoucleR" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes104 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Temps de boucle lente} -width 140 
    vTcl:DefineAlias "$site_3_0.mes104" "MsgETempsBoucleL" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab105 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text {9999 ms} 
    vTcl:DefineAlias "$site_3_0.lab105" "ETempsBoucleL" vTcl:WidgetProc "MainWindow" 1
    canvas $site_3_0.can107 \
        -background #ffffff -borderwidth 2 -closeenough 1.0 -height 143 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 253 
    vTcl:DefineAlias "$site_3_0.can107" "EChartGirouette" vTcl:WidgetProc "MainWindow" 1
    canvas $site_3_0.can108 \
        -background #ffffff -borderwidth 2 -closeenough 1.0 -height 153 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 253 
    vTcl:DefineAlias "$site_3_0.can108" "EGraphHumidite" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes109 \
        -anchor w -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text >>>>>> -width 61 
    vTcl:DefineAlias "$site_3_0.mes109" "Msg1" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes110 \
        -anchor w -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text >>>>>> -width 61 
    vTcl:DefineAlias "$site_3_0.mes110" "Msg2" vTcl:WidgetProc "MainWindow" 1
    entry $site_3_0.ent45 \
        -background white -disabledforeground #a3a3a3 \
        -font $vTcl(actual_gui_font_fixed_desc) \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 10 
    vTcl:DefineAlias "$site_3_0.ent45" "Entry1" vTcl:WidgetProc "MainWindow" 1
    place $site_3_0.mes77 \
        -in $site_3_0 -x 20 -y 30 -width 80 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab78 \
        -in $site_3_0 -x 100 -y 30 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes79 \
        -in $site_3_0 -x 20 -y 70 -width 80 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab81 \
        -in $site_3_0 -x 100 -y 70 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes82 \
        -in $site_3_0 -x 20 -y 110 -width 80 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab83 \
        -in $site_3_0 -x 100 -y 110 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes84 \
        -in $site_3_0 -x 20 -y 150 -width 80 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab85 \
        -in $site_3_0 -x 100 -y 150 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes87 \
        -in $site_3_0 -x 20 -y 190 -width 80 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab88 \
        -in $site_3_0 -x 100 -y 190 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes89 \
        -in $site_3_0 -x 20 -y 230 -width 80 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab90 \
        -in $site_3_0 -x 100 -y 230 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tBu91 \
        -in $site_3_0 -x 150 -y 230 -width 26 -relwidth 0 -height 25 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes92 \
        -in $site_3_0 -x 20 -y 270 -width 80 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab93 \
        -in $site_3_0 -x 100 -y 270 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab94 \
        -in $site_3_0 -x 185 -y 270 -width 10 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab95 \
        -in $site_3_0 -x 155 -y 270 -width 10 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab96 \
        -in $site_3_0 -x 165 -y 270 -width 10 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab97 \
        -in $site_3_0 -x 175 -y 270 -width 10 -relwidth 0 -height 21 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes98 \
        -in $site_3_0 -x 10 -y 310 -width 90 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab99 \
        -in $site_3_0 -x 100 -y 310 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes102 \
        -in $site_3_0 -x 10 -y 370 -width 140 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab103 \
        -in $site_3_0 -x 150 -y 370 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes104 \
        -in $site_3_0 -x 280 -y 370 -width 140 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab105 \
        -in $site_3_0 -x 420 -y 370 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.can107 \
        -in $site_3_0 -x 230 -y 30 -width 253 -relwidth 0 -height 143 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.can108 \
        -in $site_3_0 -x 230 -y 190 -width 253 -relwidth 0 -height 143 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.mes109 \
        -in $site_3_0 -x 160 -y 30 -width 61 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes110 \
        -in $site_3_0 -x 160 -y 190 -width 61 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent45 \
        -in $site_3_0 -x 180 -y 340 -anchor nw -bordermode ignore 
    labelframe $top.lab46 \
        \
        -font {-family {Segoe UI} -size 10 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground black -text {Mesures Physique} \
        -background $vTcl(actual_gui_bg) -height 405 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -width 710 
    vTcl:DefineAlias "$top.lab46" "MesureP" vTcl:WidgetProc "MainWindow" 1
    set site_3_0 $top.lab46
    message $site_3_0.mes77 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text DirectVent -width 80 
    vTcl:DefineAlias "$site_3_0.mes77" "DirectVent" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab78 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text {9,999 } 
    vTcl:DefineAlias "$site_3_0.lab78" "PDirection" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes79 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Vitesse Vent} -width 80 
    vTcl:DefineAlias "$site_3_0.mes79" "VVent" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab81 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text 0 
    vTcl:DefineAlias "$site_3_0.lab81" "PVitesse" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes82 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Temperature -width 80 
    vTcl:DefineAlias "$site_3_0.mes82" "Temp" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab83 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text {9,999 } 
    vTcl:DefineAlias "$site_3_0.lab83" "PTemperature" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes84 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Luminosite -width 80 
    vTcl:DefineAlias "$site_3_0.mes84" "Lumi" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab85 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text {9,999 } 
    vTcl:DefineAlias "$site_3_0.lab85" "PLuminosite" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes87 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Humidite -width 80 
    vTcl:DefineAlias "$site_3_0.mes87" "Humi" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab88 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text {999 } 
    vTcl:DefineAlias "$site_3_0.lab88" "PHumidite" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes89 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Pluviometrie -width 80 
    vTcl:DefineAlias "$site_3_0.mes89" "Pluvi" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab90 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text 0 
    vTcl:DefineAlias "$site_3_0.lab90" "PPluviometrie" vTcl:WidgetProc "MainWindow" 1
    message $site_3_0.mes92 \
        -anchor e -background $vTcl(actual_gui_bg) \
        -font {-family {Segoe UI} -size 9} -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {No Station} -width 80 
    vTcl:DefineAlias "$site_3_0.mes92" "NoStation" vTcl:WidgetProc "MainWindow" 1
    label $site_3_0.lab93 \
        -activebackground #f9f9f9 -activeforeground black -anchor e \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -relief sunken -text 0 
    vTcl:DefineAlias "$site_3_0.lab93" "PStation" vTcl:WidgetProc "MainWindow" 1
    ttk::progressbar $site_3_0.tPr45 \
        -length 100 
    vTcl:DefineAlias "$site_3_0.tPr45" "BVVent" vTcl:WidgetProc "MainWindow" 1
    ttk::progressbar $site_3_0.tPr46 \
        -length 100 
    vTcl:DefineAlias "$site_3_0.tPr46" "BTemp" vTcl:WidgetProc "MainWindow" 1
    ttk::progressbar $site_3_0.tPr47 \
        -length 100 
    vTcl:DefineAlias "$site_3_0.tPr47" "BLumi" vTcl:WidgetProc "MainWindow" 1
    ttk::progressbar $site_3_0.tPr48 \
        -length 100 
    vTcl:DefineAlias "$site_3_0.tPr48" "BHumi" vTcl:WidgetProc "MainWindow" 1
    ttk::progressbar $site_3_0.tPr49 \
        -length 100 
    vTcl:DefineAlias "$site_3_0.tPr49" "BPluvi" vTcl:WidgetProc "MainWindow" 1
    canvas $site_3_0.can51 \
        -background #ffffff -borderwidth 2 -closeenough 1.0 -height 203 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 393 
    vTcl:DefineAlias "$site_3_0.can51" "EChartPeak" vTcl:WidgetProc "MainWindow" 1
    text $site_3_0.tex54 \
        -background #cacaca -font {-family {Segoe UI} -size 9 -weight bold} \
        -foreground black -height 154 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 384 -wrap word 
    $site_3_0.tex54 configure -font "-family {Segoe UI} -size 9 -weight bold"
    $site_3_0.tex54 insert end text
    vTcl:DefineAlias "$site_3_0.tex54" "TextPeak" vTcl:WidgetProc "MainWindow" 1
    place $site_3_0.mes77 \
        -in $site_3_0 -x 20 -y 30 -width 80 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab78 \
        -in $site_3_0 -x 100 -y 30 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes79 \
        -in $site_3_0 -x 20 -y 70 -width 80 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab81 \
        -in $site_3_0 -x 100 -y 70 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes82 \
        -in $site_3_0 -x 20 -y 110 -width 80 -height 23 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab83 \
        -in $site_3_0 -x 100 -y 110 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes84 \
        -in $site_3_0 -x 20 -y 150 -width 80 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab85 \
        -in $site_3_0 -x 100 -y 150 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes87 \
        -in $site_3_0 -x 20 -y 190 -width 80 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab88 \
        -in $site_3_0 -x 100 -y 190 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes89 \
        -in $site_3_0 -x 20 -y 230 -width 80 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab90 \
        -in $site_3_0 -x 100 -y 230 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.mes92 \
        -in $site_3_0 -x 20 -y 270 -width 80 -height 22 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab93 \
        -in $site_3_0 -x 100 -y 270 -width 54 -height 21 -anchor nw \
        -bordermode ignore 
    place $site_3_0.tPr45 \
        -in $site_3_0 -x 180 -y 70 -anchor nw -bordermode ignore 
    place $site_3_0.tPr46 \
        -in $site_3_0 -x 180 -y 110 -anchor nw -bordermode ignore 
    place $site_3_0.tPr47 \
        -in $site_3_0 -x 180 -y 150 -anchor nw -bordermode ignore 
    place $site_3_0.tPr48 \
        -in $site_3_0 -x 180 -y 190 -anchor nw -bordermode ignore 
    place $site_3_0.tPr49 \
        -in $site_3_0 -x 180 -y 230 -anchor nw -bordermode ignore 
    place $site_3_0.can51 \
        -in $site_3_0 -x 300 -y 30 -width 393 -relwidth 0 -height 203 \
        -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.tex54 \
        -in $site_3_0 -x 300 -y 240 -width 384 -relwidth 0 -height 154 \
        -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra45 \
        -in $top -x 0 -y 440 -width 1095 -relwidth 0 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab66 \
        -in $top -x 10 -y 10 -width 500 -relwidth 0 -height 405 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 550 -y 10 -width 710 -relwidth 0 -height 405 -relheight 0 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}



set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

