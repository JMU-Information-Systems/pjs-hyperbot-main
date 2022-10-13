# coding=utf-8

def a_sequence_click_start(xaml, name):
    xaml.write("          <Sequence DisplayName=\"Click auf "+name+"\" sap:VirtualizedContainerService.HintSize=\"418,728\" sap2010:WorkflowViewState.IdRef=\"Sequence_3\" >\n")
    xaml.write("              <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("                <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                  <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>\n")
    xaml.write("                  <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("                </scg:Dictionary>\n")
    xaml.write("              </sap:WorkflowViewStateService.ViewState>\n")


def a_sequence_send_hotkey_Strg_C_start(xaml, name):
    xaml.write("          <Sequence DisplayName=\"Send Hotkey Strg+C in "+name+"\" sap:VirtualizedContainerService.HintSize=\"418,728\" sap2010:WorkflowViewState.IdRef=\"Sequence_3\">\n")
    xaml.write("              <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("                <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                  <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>\n")
    xaml.write("                  <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("                </scg:Dictionary>\n")
    xaml.write("              </sap:WorkflowViewStateService.ViewState>\n")

def a_sequence_send_hotkey_Strg_V_start(xaml, name):
    xaml.write("          <Sequence DisplayName=\"Send Hotkey Strg+V in "+name+"\" sap:VirtualizedContainerService.HintSize=\"418,728\" sap2010:WorkflowViewState.IdRef=\"Sequence_3\">\n")
    xaml.write("              <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("                <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                  <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>\n")
    xaml.write("                  <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("                </scg:Dictionary>\n")
    xaml.write("              </sap:WorkflowViewStateService.ViewState>\n")

def a_sequence_typeinto_start(xaml, name):
    xaml.write("          <Sequence DisplayName=\"Type Into "+name+"\" sap:VirtualizedContainerService.HintSize=\"418,728\" sap2010:WorkflowViewState.IdRef=\"Sequence_3\">\n")
    xaml.write("              <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("                <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                  <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>\n")
    xaml.write("                  <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("                </scg:Dictionary>\n")
    xaml.write("              </sap:WorkflowViewStateService.ViewState>\n")


def a_sequence_click_checkbox_start(xaml, name):
    xaml.write("          <Sequence DisplayName=\"Click Checkbox "+name+"\" sap:VirtualizedContainerService.HintSize=\"418,728\" sap2010:WorkflowViewState.IdRef=\"Sequence_3\">\n")
    xaml.write("              <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("                <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                  <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>\n")
    xaml.write("                  <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("                </scg:Dictionary>\n")
    xaml.write("              </sap:WorkflowViewStateService.ViewState>\n")

def a_sequence_click_optionsfeld_start(xaml, name):
    xaml.write("          <Sequence DisplayName=\"Click Optionsfeld "+name+"\" sap:VirtualizedContainerService.HintSize=\"418,728\" sap2010:WorkflowViewState.IdRef=\"Sequence_3\">\n")
    xaml.write("              <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("                <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                  <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>\n")
    xaml.write("                  <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("                </scg:Dictionary>\n")
    xaml.write("              </sap:WorkflowViewStateService.ViewState>\n")

def a_press_enter(xaml):  # Enter
    xaml.write("            <ui:SendHotkey Activate=\"True\" DisplayName=\"Enter drücken\" Key=\"enter\" KeyModifiers=\"None\" SpecialKey=\"True\">\n")
    xaml.write("              <ui:SendHotkey.Target>\n")
    xaml.write("                <ui:Target  Element=\"{x:Null}\" >\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:SendHotkey.Target>\n")
    xaml.write("            </ui:SendHotkey>\n")


def a_sequence_end(xaml):
    xaml.write("            </Sequence>\n")


#   ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Browser:

def a_edge_browser_start(xaml, url):
    xaml.write("    <ui:OpenBrowser BrowserType=\"Edge\" DisplayName=\"Open Browser\" Url=\""+url+"\">\n")
    xaml.write("      <ui:OpenBrowser.Body>\n")
    xaml.write("        <ActivityAction x:TypeArguments=\"x:Object\">\n")
    xaml.write("          <Sequence DisplayName=\"Do\">\n")
    return("          </Sequence>\n        </ActivityAction>\n      </ui:OpenBrowser.Body>\n    </ui:OpenBrowser>\n")

def a_edge_browser_attach(xaml, a_url):
    xaml.write("    <ui:BrowserScope BrowserType=\"[BrowserType.Edge]\" DisplayName=\"Attach Browser\"  Selector=\"&lt;html app=\'msedge.exe\' url='"+a_url+" /&gt;\">\n")
    xaml.write("      <ui:BrowserScope.Body>\n")
    xaml.write("        <ActivityAction x:TypeArguments=\"x:Object\">\n")
    xaml.write("          <Sequence DisplayName=\"Do\">\n")
    return("          </Sequence>\n         </ActivityAction>\n      </ui:BrowserScope.Body>\n    </ui:BrowserScope>\n")

#Bausteine, wenn ID vorhanden ist


# Standard Baustein mit Test auf AutomationID

def a_click_left_browser_schaltfläche_id(xaml, application_name, url, aaname, id):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id='"+id+"\'/&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")


#nicht benötigt im späteren Verlauf
def a_click_left_browser_schaltfläche_id_var_2 (xaml, application_name, url, aaname, id):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag='INPUT' type='text' id='"+id+"\'/&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")




#nicht benötigt im späteren Verlauf

def a_click_left_browser_schaltfläche_id_var_3(xaml, application_name, url, aaname, parentid):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id='"+parentid+"\' aaname=\'"+aaname+"\'  \'/&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")




#Bausteine, wenn keine ID vorhanden


#nur aaname

def a_click_left_browser_schaltfläche_no_id (xaml, application_name, url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+aaname+"\'/&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

#über name und elementclass

def a_click_left_browser_schaltfläche_no_id_var2 (xaml, application_name, url, aaname, elementclass):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+aaname+"\' class=\'"+elementclass+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

#keine Verwendung im späteren Verlauf

def a_click_left_browser_schaltfläche_no_id_var3(xaml, application_name, url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'BUTTON\' type=\'button\' aaname=\'"+aaname+"\'/&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")


#keine Verwendung im späteren Verlauf

def a_click_left_browser_schaltfläche_no_id_var4(xaml, application_name, url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'BUTTON\' type=\'button\' aaname=\'"+aaname+"\'/&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")


#keine Verwendung im späteren Verlauf
# Variante 3 mit Tag=Button & Type=Submit + Name des Feldes

def a_click_left_browser_schaltfläche_no_id_var5 (xaml, application_name, url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'BUTTON\' type=\'submit\' aaname=\'"+aaname+"\'/&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")


#keine Verwendung im späteren Verlauf
#Variante 5, aaname und tag=SPAN

def a_click_left_browser_schaltfläche_no_id_var5 (xaml, application_name, url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'SPAN\' aaname=\'"+aaname+"\'/&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")


#keine Verwendung im späteren Verlauf
#Variante 6, aaname und tag=Select

def a_click_left_browser_schaltfläche_no_id_var6 (xaml, application_name, url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'SELECT\' aaname=\'"+aaname+"\'/&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")



def a_click_right_browser_schaltfläche_id(xaml, application_name, url, aaname, id):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id=\'"+id+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")


def a_click_right_browser_schaltfläche_no_id(xaml, application_name, url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+aaname+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")


def a_click_right_browser_schaltfläche_no_id_var2(xaml, application_name, url, aaname, elementclass):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+aaname+"\' class=\'"+elementclass+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

# über id, heißt in der Tabelle "Kontrollkästchen"
def a_click_left_browser_checkbox(xaml, application_name, url, aaname, id):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click Checkbox "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id=\'"+id+"\' tag=\'INPUT\' type=\'checkbox\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

    # über name


 #wenn keine ID

def a_click_left_browser_checkbox_no_id(xaml, application_name, url, name, elementclass):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click Checkbox "+name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl name=\'"+name+"\' tag=\'INPUT\' type=\'checkbox\' class=\'"+elementclass+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")


def a_click_left_browser_checkbox_no_id_var2(xaml, application_name, url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click Checkbox "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+aaname+"\' tag=\'INPUT\' type=\'checkbox\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

def a_click_left_browser_optionsfeld (xaml, application_name, url, aaname, id):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click Optionsfeld "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id=\'"+id+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

def a_click_left_browser_optionsfeld_no_id (xaml, application_name, url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click Optionsfeld "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+aaname+"\'  /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

def a_click_left_browser_optionsfeld_var_no_id_var2 (xaml, application_name, url, aaname, elementclass):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click Optionsfeld "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+aaname+"\' class=\'"+elementclass+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")


def a_click_kombinationsfeld(xaml, application_name, url, aaname, id):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_Left\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag='SELECT' id=\'"+id+"\'/&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\"/>\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

def a_click_kombinationsfeld_no_id (xaml, application_name, url, aaname, elementclass):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_Left\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag='SELECT' aaname=\'"+aaname+"\' class=\'"+elementclass+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\"/>\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

def a_click_left_browser_text (xaml, application_name, url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+aaname+"\'/&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

def a_click_browser_text_var2 (xaml, application_name, url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+aaname+"\'tag=\'LABEL\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

def a_click_gruppe(xaml, application_name, url,aaname, id):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf " +aaname+ "\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'SPAN\' id=\'"+id+"\'/&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

#tag ist IMG

def a_click_left_browser_grafik (xaml, application_name, url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+aaname+"\' tag='IMG' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")
    
    
    # über ID

def a_send_hotkey_strg_c_browser(xaml, application_name, url, name, id):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+C in "+name+"\" EmptyField=\"True\" Key=\"c\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id=\'"+id+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")


# wenn keine ID über name

def a_send_hotkey_strg_c_browser_no_id (xaml, application_name, url, name):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+C in: "+name+"\"  EmptyField=\"True\" Key=\"c\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+name+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")


# wenn weder ID noch name, über tyg input, type text
def a_send_hotkey_strg_c_browser_no_id_var2(xaml, application_name, url, name, elementclass):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+C in: "+name+"\"  EmptyField=\"True\" Key=\"c\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+name+"\' class=\'"+elementclass+"\'  /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")


# nicht gebraucht im späteren Verlauf

def a_send_hotkey_strg_c_browser_no_id_var3 (xaml, application_name, url, name):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+C in: "+name+"\" EmptyField=\"True\" Key=\"c\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'INPUT\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")


def a_send_hotkey_strg_v_browser(xaml, application_name, url, name, id):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+V in: "+name+"\" EmptyField=\"True\" Key=\"v\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id=\'"+id+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")


def a_send_hotkey_strg_v_browser_no_id(xaml, application_name, url, name):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+V in: "+name+"\" EmptyField=\"True\" Key=\"v\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag='INPUT' type=\'text\' aaname=\'"+name+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")


def a_send_hotkey_strg_v_browser_no_id_var2(xaml, application_name, url, name):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+V in: "+name+"\" EmptyField=\"True\" Key=\"v\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag='INPUT' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")


#nicht gebraucht im späteren Verlauf

def a_send_hotkey_strg_v_browser_no_id_var3(xaml, application_name, url, name):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+V in: "+name+"\"  EmptyField=\"True\" Key=\"v\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag='INPUT' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")




def a_sequence_typeinto_start(xaml, name):
    xaml.write("          <Sequence DisplayName=\"Type Into"+ name+"\" sap:VirtualizedContainerService.HintSize=\"418,728\" sap2010:WorkflowViewState.IdRef=\"Sequence_3\">\n")
    xaml.write("              <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("                <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                  <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>\n")
    xaml.write("                  <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("                </scg:Dictionary>\n")
    xaml.write("              </sap:WorkflowViewStateService.ViewState>\n")


# über automationid
def a_type_into_browser(xaml, application_name, url, name, id, input_variable):
    if input_variable=="bitte manuell anpassen":
        xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into "+name+"\" EmptyField=\"True\" Text=\"bitte manuell anpassen\">\n")
        xaml.write("              <ui:TypeInto.Target>")
        xaml.write("               <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id=\'"+id+"\' tag=\'INPUT\' /&gt;\" TimeoutMS=\"1000\">\n")
        xaml.write("            <ui:Target.WaitForReady>\n")
        xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
        xaml.write("            </ui:Target.WaitForReady>\n")
        xaml.write("                </ui:Target>\n")
        xaml.write("              </ui:TypeInto.Target>\n")
        xaml.write("            </ui:TypeInto>\n")
    else:
        xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into "+name+"\" EmptyField=\"True\" Text=\"["+input_variable+"]\">\n")
        xaml.write("              <ui:TypeInto.Target>")
        xaml.write("               <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id=\'"+id+"\' tag=\'INPUT\' /&gt;\" TimeoutMS=\"1000\">\n")
        xaml.write("            <ui:Target.WaitForReady>\n")
        xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
        xaml.write("            </ui:Target.WaitForReady>\n")
        xaml.write("                </ui:Target>\n")
        xaml.write("              </ui:TypeInto.Target>\n")
        xaml.write("            </ui:TypeInto>\n")


# wenn keine automationID, dann tag=Input, Type=Text
def a_type_into_browser_no_id(xaml, application_name, url, name, input_variable):
    xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into "+name+"\" EmptyField=\"True\" Text=\"["+input_variable+"]\">\n")
    xaml.write("              <ui:TypeInto.Target>\n")
    xaml.write("               <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+name+"\' tag=\'INPUT\' type=\'text\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:TypeInto.Target>\n")
    xaml.write("            </ui:TypeInto>\n")


# wenn weder automationID noch Name, nur Tag=Input
def a_type_into_browser_no_id_var2(xaml, application_name, url, name, input_variable):
    xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into "+name+"\" EmptyField=\"True\" Text=\"["+input_variable+"]\">\n")
    xaml.write("              <ui:TypeInto.Target>\n")
    xaml.write("               <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'INPUT\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:TypeInto.Target>\n")
    xaml.write("            </ui:TypeInto>\n")


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Applikation

def a_click_left_in_application (xaml, application_name, title, automationid, name, role):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+automationid+"\' name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")



def a_click_left_in_application_no_id(xaml, application_name, title, name, role):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

#Rechtsklick

def a_click_right_in_application(xaml, application_name, title, automationid, name, role):  # für alle Anwendungen außer Browser
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+automationid+"\' name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")


def a_click_right_in_application_no_id (xaml, application_name, title, automationid, name, role):  # für alle Anwendungen außer Browser
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")

def a_click_right_in_application_var2(xaml, application_name, title, name, role):  # für alle Anwendungen außer Browser
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>v")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")


def a_type_into_application(xaml, application_name, title, id, name, role, input_variable):
    xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into "+name+"\" EmptyField=\"True\" Text=\"["+input_variable+"]\">\n")
    xaml.write("              <ui:TypeInto.Target>\n")
    xaml.write("               <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+id+"\' name=\'"+name+"\'  role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:TypeInto.Target>\n")
    xaml.write("            </ui:TypeInto>\n")


# Abfrage über name und role
def a_type_into_application_no_id(xaml, application_name, title, name, role, input_variable):
    xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into "+name+"\" EmptyField=\"True\" Text=\"["+input_variable+"]\">\n")
    xaml.write("              <ui:TypeInto.Target>\n")
    xaml.write("               <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:TypeInto.Target>\n")
    xaml.write("            </ui:TypeInto>\n")



def a_send_hotkey_strg_c_in_application(xaml, application_name, title, id,name,  role):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey STRG+C in "+name+"\" EmptyField=\"True\" Key=\"c\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+id+"\' name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")


def a_send_hotkey_strg_c_in_application_no_id(xaml, application_name, title, name, role):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey STRG+C in "+name+"\" EmptyField=\"True\" Key=\"c\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")



def a_send_hotkey_strg_v_in_application(xaml, application_name, title, id, name, role):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey STRG+V in "+name+"\" EmptyField=\"True\" Key=\"v\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+id+"\' name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")


def a_send_hotkey_strg_v_in_application_no_id(xaml, application_name, title, name, role):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey STRG+V in "+name+"\" EmptyField=\"True\" Key=\"v\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Explorer

def a_click_left_in_explorer(xaml, application_name, title, name, role):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf " +name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt; name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")




def a_click_right_in_explorer(xaml, application_name, title, name, role):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click auf "+name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">\n")
    xaml.write("              <ui:Click.CursorPosition>\n")
    xaml.write("                <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("                  <ui:CursorPosition.OffsetX>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetX>\n")
    xaml.write("                  <ui:CursorPosition.OffsetY>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:CursorPosition.OffsetY>\n")
    xaml.write("                </ui:CursorPosition>\n")
    xaml.write("              </ui:Click.CursorPosition>\n")
    xaml.write("              <ui:Click.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:Click.Target>\n")
    xaml.write("            </ui:Click>\n")



# über ID, name und role, uia Selektor
def a_type_into_explorer(xaml, application_name, title, id, name, role, input_variable):
    xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into "+name+"\" EmptyField=\"True\" Text=\"["+input_variable+"]\">\n")
    xaml.write("              <ui:TypeInto.Target>\n")
    xaml.write("               <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+id+"\' name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:TypeInto.Target>\n")
    xaml.write("            </ui:TypeInto>\n")



def a_send_hotkey_strg_c_in_explorer(xaml, application_name, title, name, id, role):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey STRG+C in "+name+"\" EmptyField=\"True\" Key=\"c\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("               <ui:Target Selector==\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+id+"\' name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")



def a_send_hotkey_strg_v_in_explorer(xaml, application_name, title, name, id, role):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey STRG+V in "+name+"\" EmptyField=\"True\" Key=\"v\" KeyModifiers=\"Ctrl\">\n")
    xaml.write("        <ui:SendHotkey.Target>\n")
    xaml.write("               <ui:Target Selector==\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+id+"\' name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">\n")
    xaml.write("            <ui:Target.WaitForReady>\n")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("            </ui:Target.WaitForReady>\n")
    xaml.write("          </ui:Target>\n")
    xaml.write("        </ui:SendHotkey.Target>\n")
    xaml.write("      </ui:SendHotkey>\n")



# Application Activities Excel
def a_open_excel(xaml): #alte Version
    xaml.write("    <ui:OpenApplication DisplayName=\"Open Application Excel\" FileName=\"C:\Program Files (x86)\Microsoft Office\root\Office16\excel.exe\" Selector=\"&lt;wnd app='excel.exe' /&gt;\">\n")
    xaml.write("      <ui:OpenApplication.Body>\n")
    xaml.write("        <ActivityAction x:TypeArguments=\"x:Object\">\n")
    xaml.write("          <ActivityAction.Argument>\n")
    xaml.write("            <DelegateInArgument x:TypeArguments=\"x:Object\" Name=\"ContextTarget\" />\n")
    xaml.write("          </ActivityAction.Argument>\n")
    xaml.write("          <Sequence DisplayName=\"Do\">\n")
    xaml.write("          </Sequence>\n")
    xaml.write("        </ActivityAction>\n")
    xaml.write("      </ui:OpenApplication.Body>\n")
    xaml.write("    </ui:OpenApplication>\n")


def a_excel_application_scope(xaml, workbook_path):  # Excel öffnen
    xaml.write("    <ui:ExcelApplicationScope DisplayName=\"Excel Öffnen\" InstanceCachePeriod=\"3000\" WorkbookPath=\""+workbook_path+"\">\n")
    xaml.write("      <ui:ExcelApplicationScope.Body>\n")
    xaml.write("        <ActivityAction x:TypeArguments=\"ui:WorkbookApplication\">\n")
    xaml.write("          <ActivityAction.Argument>\n")
    xaml.write("            <DelegateInArgument x:TypeArguments=\"ui:WorkbookApplication\" Name=\"ExcelWorkbookScope\" />\n")
    xaml.write("          </ActivityAction.Argument>\n")
    xaml.write("          <Sequence DisplayName=\"Do\">\n")
    return("          </Sequence>\n        </ActivityAction>\n      </ui:ExcelApplicationScope.Body>\n    </ui:ExcelApplicationScope>\n")


def a_word_application_scope (xaml,workbook_path):
    xaml.write("    <p:WordApplicationScope FilePath=\"{x:Null}\" DisplayName=\"Word öffnen\" sap:VirtualizedContainerService.HintSize=\"434,193.333333333333\" sap2010:WorkflowViewState.IdRef=\"WordApplicationScope_1\">\n")
    xaml.write("      <p:WordApplicationScope.Body>\n")
    xaml.write("        <ActivityAction x:TypeArguments=\"ui:WordDocument\">\n")
    xaml.write("          <ActivityAction.Argument>\n")
    xaml.write("            <DelegateInArgument x:TypeArguments=\"ui:WordDocument\" Name=\"WordDocumentScope\" />\n")
    xaml.write("          </ActivityAction.Argument>\n")
    xaml.write("          <Sequence DisplayName=\"Do\" sap:VirtualizedContainerService.HintSize=\"200,84.6666666666667\" sap2010:WorkflowViewState.IdRef=\"Sequence_20\">\n")
    xaml.write("            <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("              <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                <x:Boolean x:Key=\"IsExpanded\">True</x:Boolean>\n")
    xaml.write("              </scg:Dictionary>\n")
    xaml.write("            </sap:WorkflowViewStateService.ViewState>\n")
    return("          </Sequence>\n        </ActivityAction>\n      </p:WordApplicationScope.Body>\n    </p:WordApplicationScope>\n")
    
def a_open_application (xaml, application_name, windowtitle, root):
    xaml.write("    <ui:OpenApplication ApplicationWindow=\"{x:Null}\" Arguments=\"{x:Null}\" TimeoutMS=\"{x:Null}\" WorkingDirectory=\"{x:Null}\" DisplayName=\"Open "+application_name+"\" FileName=\'"+root+"\' Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+windowtitle+"\' /&gt;\" >\n")
    xaml.write("      <ui:OpenApplication.Body>\n")
    xaml.write("        <ActivityAction x:TypeArguments=\"x:Object\">\n")
    xaml.write("          <ActivityAction.Argument>\n")
    xaml.write("            <DelegateInArgument x:TypeArguments=\"x:Object\" Name=\"ContextTarget\" />\n")
    xaml.write("          </ActivityAction.Argument>\n")
    xaml.write("          <Sequence DisplayName=\"Do\" sap:VirtualizedContainerService.HintSize=\"200,84.6666666666667\" sap2010:WorkflowViewState.IdRef=\"Sequence_21\">\n")
    xaml.write("            <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("              <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                <x:Boolean x:Key=\"IsExpanded\">True</x:Boolean>\n")
    xaml.write("              </scg:Dictionary>\n")
    xaml.write("            </sap:WorkflowViewStateService.ViewState>\n")
    return("          </Sequence>\n        </ActivityAction>\n      </ui:OpenApplication.Body>\n    </ui:OpenApplication>\n")

def a_attach_application (xaml, application_name, windowtitle):
    xaml.write("    <ui:WindowScope DisplayName=\"Attach "+application_name+"\" Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+windowtitle+"\' /&gt;\">\n")
    xaml.write("      <ui:WindowScope.Body>\n")
    xaml.write("        <ActivityAction x:TypeArguments=\"x:Object\">\n")
    xaml.write("          <Sequence DisplayName=\"Do\">\n")
    xaml.write("            <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("              <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                <x:Boolean x:Key=\"IsExpanded\">True</x:Boolean>\n")
    xaml.write("              </scg:Dictionary>\n")
    xaml.write("            </sap:WorkflowViewStateService.ViewState>\n")
    return("          </Sequence>\n        </ActivityAction>\n      </ui:WindowScope.Body>\n    </ui:WindowScope>\n")


def a_write_cell(xaml, cell, sheet_name, text, workbook_path):
    xaml.write("    <ui:WriteCell Cell=\""+cell+"\" DisplayName=\"Write Cell\" SheetName=\""+sheet_name+"\" Text=\""+text+"\" WorkbookPath=\""+workbook_path+"\" />\n")


# Excel Aktivitäten, müssen im Body der Excel Application Scope sein

def a_read_range(xaml):  # Bereich aus Excel Datei auslesen und in Outputtabelle_name speichern
    xaml.write("    <ui:ReadRange AddHeaders=\"True\" DataTable=\"Name der Datenbank eintragen\" DisplayName=\"Read Range\" Range=\"gewünschten Bereich eintragen\" SheetName=\"Name des Datenblatts eintragen\" WorkbookPath=\"Hier Pfad der gewünschten Datei eingeben\" />\n")

def a_comment_read_range (xaml):
    xaml.write("            <ui:Comment Text=\"Read Range: Im Prozessablauf wurde öfters per STRG+C etwas aus einer ExcelDatei kopiert. In diesem automatisch generierten XAML wird dies über die Aktivität 'Send Hotkey Strg+C' gelöst, sinnvoll wäre zur Optimierung auch eine 'read range' Aktivität, die den gewünschten Bereich einer Excel Tabelle ausliest und in einer neuen Datentabelle speichert, auf die in folgenden Aktivitäten zugegriffen werden kann. Die Aktivität wurde bereits eingefügt, hier muss noch die Variable manuell eingeben werden, in der die Datentabelle abgespeichert werden muss  \" />\n")

def a_sequence_read_range_start (xaml):
    xaml.write("          <Sequence DisplayName=\"Read Range\" >\n")
    xaml.write("              <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("                <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                  <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>\n")
    xaml.write("                  <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("                </scg:Dictionary>\n")
    xaml.write("              </sap:WorkflowViewStateService.ViewState>\n")




def a_sequence_data_scraping_start (xaml):
    xaml.write("          <Sequence DisplayName=\"Data Scraping\" sap:VirtualizedContainerService.HintSize=\"418,728\" sap2010:WorkflowViewState.IdRef=\"Sequence_3\" >\n")
    xaml.write("              <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("                <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                  <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>\n")
    xaml.write("                  <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("                </scg:Dictionary>\n")
    xaml.write("              </sap:WorkflowViewStateService.ViewState>\n")


def a_comment_data_scraping (xaml): #Abfrage über Frontend
    xaml.write("            <ui:Comment Text=\"Data Scraping: Im Prozessablauf sollen Daten aus dem Browser gescrapet und in eine andere Applikation (z.B. Excel) übertragen werden. Hierzu bietet UiPath die Option 'Tabellenextraktion' die in der oberen Menüleiste ausgewählt werden kann. In einer Schritt für Schritt Anleitung werden die zu scrapteten Elemente direkt mit UiPath ausgewählt und die Ergebnisse in einer separaten Datentabelle abgespeichert. Diese können anschließend mittels der Aktivität 'Write Range' in Excel übertragen werden. Diese Aktivität wurde ebenfalls automatisiert hinzugefügt'\" />\n")



def a_read_cell(xaml, output_var, cell, sheet_name):  # Excel Zelle auslesen
    # Zelle steht in automationId
    xaml.write("    <ui:ExcelReadCell Result=\""+output_var+"\" SheetName=\""+sheet_name+"\" Cell=\""+cell+"\" DisplayName=\"Read Cell\"/>\n")


def a_for_each_row(xaml, outputtable_name):  # For Schleife, für jede Zeile bestimmte Aktivität ausführen
    xaml.write("            <ui:ForEachRow ColumnNames=\"{x:Null}\"  DataTable=\""+[outputtable_name]+"\" DisplayName=\"For Each Row\" >\n")
    xaml.write("              <ui:ForEachRow.Body>\n")
    xaml.write("                <ActivityAction x:TypeArguments=\"sd:DataRow\">\n")
    xaml.write("                  <ActivityAction.Argument>\n")
    xaml.write("                    <DelegateInArgument x:TypeArguments=\"sd:DataRow\" Name=\"row\" />\n")
    xaml.write("                  </ActivityAction.Argument>")
    xaml.write("                  <Sequence DisplayName=\"Body\">\n")
    xaml.write("                  </Sequence>\n")
    xaml.write("                </ActivityAction>\n")
    xaml.write("              </ui:ForEachRow.Body>\n")
    xaml.write("            </ui:ForEachRow>\n")

def a_write_range_excel (xaml):
    xaml.write("    <ui:WriteRange StartingCell=\"{x:Null}\" AddHeaders=\"False\" DataTable=\"[Name der Datenbank]\" DisplayName=\"Write Range\"  SheetName=\"Bitte angeben\" WorkbookPath=\"Hier Pfad der gewünschten Datei eingeben\" />\n")


def a_excel_auto_save(xaml):  # speichert excel automatisch, einfach immer einfügen
    xaml.write("            <ui:ExcelSaveWorkbook DisplayName=\"Save Workbook\"/>\n")


# Sonstige
def a_find_element(xaml, position_x, position_y):  # element finden
    xaml.write("    <ui:FindRelative RelativeElement=\"{x:Null}\" DisplayName=\"Find Element\">\n")
    xaml.write("      <ui:FindRelative.CursorPosition>\n")
    xaml.write("        <ui:CursorPosition OffsetX=\""+position_x+"\" OffsetY=\""+position_y+"\" Position=\"TopLeft\"/>\n")
    xaml.write("      </ui:FindRelative.CursorPosition>\n")
    xaml.write("      <ui:FindRelative.Target>\n")
    xaml.write("        <ui:Target ClippingRegion=\"{x:Null}\" Element=\"{x:Null}\" Selector=\"&lt;html app=\'chrome.exe' /&gt;\" WaitForReady=\"COMPLETE\">\n")
    xaml.write("    </ui:Target>\n")
    xaml.write("  </ui:FindRelative.Target>\n")
    xaml.write("    </ui:FindRelative>\n")


def a_select_item(xaml,item_name):  # bei Dropdown Menü, wenn bestimmter Wert ausgewählt werden soll, z.B. Herr/Frau bei Anrede
    xaml.write("    <ui:SelectItem  ContinueOnError=\"True\" Items=\"{x:Null}\" DisplayName=\"Select Item\" Item=\""+item_name+"\">\n")
    xaml.write("      <ui:SelectItem.Target>\n")
    xaml.write("        <ui:Target ClippingRegion=\"{x:Null}\" Element=\"{x:Null}\" Selector=\"{x:Null}\"COMPLETE\">\n")
    xaml.write("        </ui:Target>\n")
    xaml.write("      </ui:SelectItem.Target>\n")
    xaml.write("    </ui:SelectItem>\n")


def a_copy_file(xaml, workbook_path, destination_path):  # wenn Datei im explorer von a nach b kopiert wird
    xaml.write("    <ui:CopyFile ContinueOnError=\"True\" Destination=\""+destination_path+"\" DisplayName=\"Copy File\" Path=\""+workbook_path+"\" />\n")


def a_maximise_window(xaml):  
    xaml.write("            <ui:MaximizeWindow Window=\"{x:Null}\" DisplayName=\"Maximize Window\"/>\n")


def a_close_window(xaml):  # wird verwendet, wenn User Applikation schließt
    xaml.write("    <ui:CloseWindow Selector=\"{x:Null}\" UseWindow=\"{x:Null}\" DisplayName=\"Close Window\" WaitForReady=\"COMPLETE\" />\n")


def a_end_activity(xaml):
    xaml.write("  </Sequence>\n</Activity>\n")


def a_try_catch_try_start_einmal(xaml):
    xaml.write("    <TryCatch DisplayName=\"Try Catch\" sap:VirtualizedContainerService.HintSize=\"474,571.333333333333\" sap2010:WorkflowViewState.IdRef=\"TryCatch_3\">\n")
    xaml.write("      <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("        <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("          <x:Boolean x:Key=\"IsExpanded\">True</x:Boolean>\n")
    xaml.write("          <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("        </scg:Dictionary>\n")
    xaml.write("      </sap:WorkflowViewStateService.ViewState>\n")

def a_try_catch_try_sonst (xaml):
    xaml.write("            <TryCatch DisplayName=\"Try Catch\" sap:VirtualizedContainerService.HintSize=\"434,328.666666666667\" sap2010:WorkflowViewState.IdRef=\"TryCatch_4\">\n")

def a_try_catch_try (xaml):
    xaml.write("      <TryCatch.Try>\n")


def a_try_catch_try_end(xaml):
    xaml.write("      </TryCatch.Try>\n")

def a_try_catch_sonst_ende (xaml):
    xaml.write("            </TryCatch>\n")



def a_try_catch_all_catches_start(xaml):
    xaml.write("      <TryCatch.Catches >\n")


def a_try_catch_all_catches_end(xaml):
    xaml.write("      </TryCatch.Catches>\n")


def a_try_catch_catch_start(xaml):
    xaml.write("        <Catch x:TypeArguments=\"s:Exception\" >\n")
    xaml.write("          <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("            <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("              <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>\n")
    xaml.write("              <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("            </scg:Dictionary>\n")
    xaml.write("          </sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("          <ActivityAction x:TypeArguments=\"s:Exception\">\n")
    xaml.write("            <ActivityAction.Argument>\n")
    xaml.write("              <DelegateInArgument x:TypeArguments=\"s:Exception\" Name=\"exception\" />\n")
    xaml.write("            </ActivityAction.Argument>\n")


def a_try_catch_catch_end(xaml):
    xaml.write("        </Catch>\n")


def a_sequence_auskommentiert(xaml):
    xaml.write("    <ui:CommentOut DisplayName=\"Auskommentiert\" sap:VirtualizedContainerService.HintSize=\"436.666666666667,274.666666666667\" sap2010:WorkflowViewState.IdRef=\"CommentOut_2\">\n")
    xaml.write("      <ui:CommentOut.Body>\n")
    xaml.write("        <Sequence DisplayName=\"Ignorierte Aktivitäten\" sap:VirtualizedContainerService.HintSize=\"400,186\" sap2010:WorkflowViewState.IdRef=\"Sequence_4\">\n")
    xaml.write("          <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("            <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("              <x:Boolean x:Key=\"IsExpanded\">True</x:Boolean>\n")
    xaml.write("            </scg:Dictionary>\n")
    xaml.write("          </sap:WorkflowViewStateService.ViewState>\n")


def a_sequence_auskommentiert_end (xaml):
    xaml.write("        </Sequence>\n")
    xaml.write("      </ui:CommentOut.Body>\n")
    xaml.write("    </ui:CommentOut>\n")


def a_sequence_variablenextraktion (xaml, task):
    xaml.write("  <Sequence DisplayName=\"Extraktion\">\n")
    xaml.write("    <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("      <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("        <x:Boolean x:Key=\"IsExpanded\">True</x:Boolean>\n")
    xaml.write("      </scg:Dictionary>\n")
    xaml.write("    </sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("    <ui:OpenBrowser AutomaticallyDownloadWebDriver=\"{x:Null}\" CommunicationMethod=\"{x:Null}\" Hidden=\"{x:Null}\" NewSession=\"{x:Null}\" Private=\"{x:Null}\" UiBrowser=\"{x:Null}\" BrowserType=\"Edge\" DisplayName=\"Open Browser\"  Url=\"http://132.187.226.138:8080/webapp/view/groupware/task/taskOverview.page?mid=22\">\n")
    xaml.write("      <ui:OpenBrowser.Body>\n")
    xaml.write("        <ActivityAction x:TypeArguments=\"x:Object\">\n")
    xaml.write("          <ActivityAction.Argument>\n")
    xaml.write("            <DelegateInArgument x:TypeArguments=\"x:Object\" Name=\"ContextTarget\" />\n")
    xaml.write("          </ActivityAction.Argument>\n")
    xaml.write("          <Sequence DisplayName=\"Do\">\n")
    xaml.write("            <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("              <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("                <x:Boolean x:Key=\"IsExpanded\">True</x:Boolean>\n")
    xaml.write("                <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("              </scg:Dictionary>\n")
    xaml.write("            </sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("            <ui:TypeInto Activate=\"True\" DisplayName=\"E-Mail eingeben\" Text=\"rpa.team22@gmail.com\">\n")
    xaml.write("              <ui:TypeInto.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;webctrl tag=\'INPUT\' type=\'text\' id=\'loginForm:username\' /&gt;\">\n")
    xaml.write("             <ui:Target.TimeoutMS>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("              </ui:Target.TimeoutMS>\n")
    xaml.write("              <ui:Target.WaitForReady>\n")
    xaml.write("                <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("              </ui:Target.WaitForReady>\n")
    xaml.write("            </ui:Target>\n")
    xaml.write("          </ui:TypeInto.Target>\n")
    xaml.write("        </ui:TypeInto>\n")
    xaml.write("            <ui:TypeInto ClickBeforeTyping=\"{x:Null}\" DisplayName=\"Passwort eingeben\" Text=\"RPA2022#\">\n")
    xaml.write("              <ui:TypeInto.Target>\n")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'msedge.exe\' title=\'Login\' /&gt;&lt;webctrl tag=\'INPUT\' type=\'password\' id=\'loginForm:password\' /&gt;\">\n")
    xaml.write("                 <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("                  </ui:Target.TimeoutMS>\n")
    xaml.write("                  <ui:Target.WaitForReady>\n")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("                  </ui:Target.WaitForReady>\n")
    xaml.write("                </ui:Target>\n")
    xaml.write("              </ui:TypeInto.Target>\n")
    xaml.write("            </ui:TypeInto>\n")
    xaml.write("        <ui:Click SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" DisplayName=\"Login Button klicken\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("          <ui:Click.CursorPosition>\n")
    xaml.write("            <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("              <ui:CursorPosition.OffsetX>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("              </ui:CursorPosition.OffsetX>\n")
    xaml.write("              <ui:CursorPosition.OffsetY>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("              </ui:CursorPosition.OffsetY>\n")
    xaml.write("            </ui:CursorPosition>\n")
    xaml.write("          </ui:Click.CursorPosition>\n")
    xaml.write("          <ui:Click.Target>\n")
    xaml.write("            <ui:Target Selector=\"&lt;webctrl tag=\'INPUT\' type=\'button\' id=\'loginForm:loginButton\' /&gt;\">\n")
    xaml.write("              <ui:Target.TimeoutMS>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("              </ui:Target.TimeoutMS>\n")
    xaml.write("              <ui:Target.WaitForReady>\n")
    xaml.write("                <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("              </ui:Target.WaitForReady>\n")
    xaml.write("            </ui:Target>\n")
    xaml.write("          </ui:Click.Target>\n")
    xaml.write("        </ui:Click>\n")
    xaml.write("        <ui:Click ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Filter anklicken\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("          <ui:Click.CursorPosition>\n")
    xaml.write("            <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("              <ui:CursorPosition.OffsetX>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("              </ui:CursorPosition.OffsetX>\n")
    xaml.write("              <ui:CursorPosition.OffsetY>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("              </ui:CursorPosition.OffsetY>\n")
    xaml.write("            </ui:CursorPosition>\n")
    xaml.write("          </ui:Click.CursorPosition>\n")
    xaml.write("          <ui:Click.Target>\n")
    xaml.write("            <ui:Target Selector=\"&lt;webctrl tag=\'A\' class=\'w-icon w-icon-small filter_list btn btn-sm btn-secondary\' /&gt;\">\n")
    xaml.write("              <ui:Target.TimeoutMS>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("              </ui:Target.TimeoutMS>\n")
    xaml.write("              <ui:Target.WaitForReady>\n")
    xaml.write("                <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("              </ui:Target.WaitForReady>\n")
    xaml.write("            </ui:Target>\n")
    xaml.write("          </ui:Click.Target>\n")
    xaml.write("          <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("            <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("              <x:Boolean x:Key=\"IsExpanded\">True</x:Boolean>\n")
    xaml.write("              <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("            </scg:Dictionary>\n")
    xaml.write("          </sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("        </ui:Click>\n")
    xaml.write("        <ui:Click ClickType=\"CLICK_SINGLE\" DisplayName=\"Filter Dienstreise auswählen\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("          <ui:Click.CursorPosition>\n")
    xaml.write("           <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("              <ui:CursorPosition.OffsetX>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("              </ui:CursorPosition.OffsetX>\n")
    xaml.write("              <ui:CursorPosition.OffsetY>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("             </ui:CursorPosition.OffsetY>\n")
    xaml.write("            </ui:CursorPosition>\n")
    xaml.write("          </ui:Click.CursorPosition>\n")
    xaml.write("          <ui:Click.Target>\n")
    xaml.write("            <ui:Target Selector=\"&lt;webctrl aaname=\'Filter: "+task+"                 Bei der Anwendung dieses Fil*\' tag=\'A\' /&gt;\">\n")
    xaml.write("             <ui:Target.TimeoutMS>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("              </ui:Target.TimeoutMS>\n")
    xaml.write("              <ui:Target.WaitForReady>\n")
    xaml.write("                <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("              </ui:Target.WaitForReady>\n")
    xaml.write("            </ui:Target>\n")
    xaml.write("          </ui:Click.Target>\n")
    xaml.write("          <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("            <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("              <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>\n")
    xaml.write("              <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("            </scg:Dictionary>\n")
    xaml.write("          </sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("        </ui:Click>\n")
    xaml.write("        <ui:Click ClickType=\"CLICK_SINGLE\" DisplayName=\"Erste Aufgabe auswählen\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">\n")
    xaml.write("          <ui:Click.CursorPosition>\n")
    xaml.write("            <ui:CursorPosition Position=\"Center\">\n")
    xaml.write("              <ui:CursorPosition.OffsetX>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("              </ui:CursorPosition.OffsetX>\n")
    xaml.write("              <ui:CursorPosition.OffsetY>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("              </ui:CursorPosition.OffsetY>\n")
    xaml.write("            </ui:CursorPosition>\n")
    xaml.write("          </ui:Click.CursorPosition>\n")
    xaml.write("          <ui:Click.Target>\n")
    xaml.write("           <ui:Target Selector=\"&lt;html app=\'msedge.exe\' title=\'Aufgaben\' /&gt;&lt;webctrl tableRow=\'3\' tag=\'TABLE\' /&gt;&lt;webctrl tableRow=\'1\' tag=\'A\' idx=\'7\' /&gt;\">\n")
    xaml.write("              <ui:Target.TimeoutMS>\n")
    xaml.write("                <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("              </ui:Target.TimeoutMS>\n")
    xaml.write("              <ui:Target.WaitForReady>\n")
    xaml.write("                <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("              </ui:Target.WaitForReady>\n")
    xaml.write("            </ui:Target>\n")
    xaml.write("          </ui:Click.Target>\n")
    xaml.write("          <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("            <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n")
    xaml.write("              <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>\n")
    xaml.write("              <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>\n")
    xaml.write("            </scg:Dictionary>\n")
    xaml.write("          </sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("        </ui:Click>\n")
    xaml.write("      </Sequence>\n")
    xaml.write("    </ActivityAction>\n")
    xaml.write("  </ui:OpenBrowser.Body>\n")
    xaml.write("</ui:OpenBrowser>\n")
    return(" <ui:CloseWindow TimeoutMS=\"{x:Null}\" UseWindow=\"{x:Null}\" DisplayName=\"Close Window 'msedge.exe Aufgabe:'\" Selector=\"&lt;html app=\'msedge.exe\' url=\'*http://132.187.226.138:8080/*\' /&gt;\" WaitForReady=\"INTERACTIVE\" />\n </Sequence>\n")
  

def a_get_text (xaml, v_id, vname):
    xaml.write("  <ui:GetValue DisplayName=\"Get Text\" >\n")
    xaml.write("    <ui:GetValue.Target>\n")
    xaml.write("      <ui:Target Selector=\"&lt;html app=\'msedge.exe\' url=\'*http://132.187.226.138:8080/*\' /&gt;&lt;webctrl tag=\'IFRAME\' idx=\'2\' /&gt;&lt;webctrl tag=\'TABLE\' /&gt;&lt;webctrl tableCol=\'2\' tableRow=\'"+v_id+"\' tag=\'TD\' /&gt;\">\n")
    xaml.write("        <ui:Target.TimeoutMS>\n")
    xaml.write("          <InArgument x:TypeArguments=\"x:Int32\" />\n")
    xaml.write("        </ui:Target.TimeoutMS>\n")
    xaml.write("        <ui:Target.WaitForReady>\n")
    xaml.write("          <InArgument x:TypeArguments=\"ui:WaitForReady\" />\n")
    xaml.write("        </ui:Target.WaitForReady>\n")
    xaml.write("      </ui:Target>\n")
    xaml.write("    </ui:GetValue.Target>\n")
    xaml.write("  <ui:GetValue.Value>\n")
    xaml.write("        <OutArgument x:TypeArguments=\"x:String\">[" + vname + "]</OutArgument>")
    xaml.write("      </ui:GetValue.Value>\n")
    xaml.write("    </ui:GetValue>\n")


def a_maximise_window (xaml):
    xaml.write("    <ui:MaximizeWindow Window=\"{x:Null}\" DisplayName=\"Maximize Window\" />")