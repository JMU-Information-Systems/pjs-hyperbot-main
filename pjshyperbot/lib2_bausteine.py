def a_edge_browser_start (xaml, url):
    xaml.write("    <ui:OpenBrowser BrowserType=\"Edge\" DisplayName=\"Open Browser\" Url=\""+url+"\">")
    xaml.write("      <ui:OpenBrowser.Body>")
    xaml.write("        <ActivityAction x:TypeArguments=\"x:Object\">")
    xaml.write("          <Sequence DisplayName=\"Do\">")


def a_edge_browser_end (xaml):
    xaml.write("          </Sequence>")
    xaml.write("        </ActivityAction>")
    xaml.write("      </ui:OpenBrowser.Body>")
    xaml.write("    </ui:OpenBrowser>")

#Klickaktivitäten, Mouseclicklogs

#Im Browser:

def a_sequence_browser_click_start(xaml, name):
    xaml.write("          <Sequence DisplayName=\"Click on "+name+"\" sap:VirtualizedContainerService.HintSize="418,728" sap2010:WorkflowViewState.IdRef=\"Sequence_3\">")
    xaml.write("              <sap:WorkflowViewStateService.ViewState>")
    xaml.write("                <scg:Dictionary x:TypeArguments="x:String, x:Object">")
    xaml.write("                  <x:Boolean x:Key="IsExpanded">False</x:Boolean>")
    xaml.write("                  <x:Boolean x:Key="IsPinned">False</x:Boolean>")
    xaml.write("                </scg:Dictionary>")
    xaml.write("              </sap:WorkflowViewStateService.ViewState>")

def a_sequence_end (xaml):
    xaml.write("            </Sequence>")
    xaml.write("          </Sequence>")


#Standard Baustein mit Test auf AutomationID
def a_click_left_browser_schaltfläche (xaml,application_name,url, aaname, id):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id='"+id+"\'/&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

#Variante 2 mit Tag=Button, Type=Button & Name des Feldes, kann abgefragt werden als Variante 1, wenn automationID leer sein sollte

def a_click_left_browser_schaltfläche_var_2 (xaml,application_name,url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'BUTTON\' type=\'button\' aaname=\'"+aaname+"\'/&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

#Variante 3 mit Tag=Button & Type=Submit + Name des Feldes

def a_click_left_browser_schaltfläche_var_3 (xaml,application_name,url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'BUTTON\' type=\'submit\' aaname=\'"+aaname+"\'/&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

#Variante 4,  Abfrage auf name und Tag A (kommt häufig vor)
def a_click_left_browser_schaltfläche_var_4 (xaml,application_name,url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'A\' aaname=\'"+aaname+"\'/&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

def a_click_left_browser_schaltfläche_var_5 (xaml,application_name,url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+aaname+"\'/&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

def a_click_left_browser_schaltfläche_var_6 (xaml,application_name,url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'SPAN\' aaname=\'"+aaname+"\'/&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

def a_click_right_browser_schaltfläche (xaml,application_name,url, aaname, id):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id=\'"+id+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")


def a_click_left_browser_checkbox (xaml,application_name,url, aaname, id):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click Checkbox+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'" + application_name + ".exe\' url=\'" + url + "\' /&gt;&lt;webctrl id=\'"+id+"\' tag=\'INPUT\' type=\'checkbox\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

def a_click_left_browser_checkbox_var2 (xaml,application_name,url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click Checkbox+" +aanamename+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'" + application_name + ".exe\' url=\'" + url + "\' /&gt;&lt;webctrl aaname=\'"+aaname+"\' tag=\'INPUT\' type=\'checkbox\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")



def a_click_single_browser_optionsfeld (xaml,application_name,url, aaname):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click Optionsfeld+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+aaname+"\' aria-role=\'option'\'/&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")




def a_click_option (xaml, application_name, name, id):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click\" KeyModifiers=\"None\" MouseButton=\"BTN_Left\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt; app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aria-role=\'option\' aaname=\'"+name+"\' id=\'"+id+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\"/>")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

def a_click_kombinationsfeld (xaml, application_name, url, aaname, id):
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_Left\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag='SELECT' id=\'"+id+"\'/&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\"/>")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")


def a_scroll_down (xaml): #runterscrollen
    xaml.write("    <ui:SendHotkey Activate=\"True\" DisplayName=\"Scroll down\" Key=\"pgdn\" KeyModifiers=\"None\" SpecialKey=\"True\">")
    xaml.write("      <ui:SendHotkey.Target>")
    xaml.write("        <ui:Target Selector=\"&lt;html app=\'chrome.exe' /&gt;\" WaitForReady=\"COMPLETE\">")
    xaml.write("        </ui:Target>")
    xaml.write("      </ui:SendHotkey.Target>")
    xaml.write("    </ui:SendHotkey>")


#Applikation


def a_click_single_in_application_element (xaml,application_name, title, aaname, id): #für alle Anwendungen außer Browser
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+id+"\' role=\'Element\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

def a_click_right_in_application_element (xaml,application_name, title, id): #für alle Anwendungen außer Browser
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+id+"\' role=\'Element\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")


def a_click_single_in_application (xaml,application_name, title, automationid, name, role): #für alle Anwendungen außer Browser
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+automationid+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

def a_click_single_in_application_var2 (xaml,application_name, title, name): #für alle Anwendungen außer Browser
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +aaname+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")


def a_click_right_in_application (xaml,application_name, title, automationid, name, role): #für alle Anwendungen außer Browser
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+automationid+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

def a_click_right_in_application_var2 (xaml,application_name, title, name, role): #für alle Anwendungen außer Browser
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

#Explorer

def a_click_left_in_explorer (xaml,application_name, title, name, role): 
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")

def a_click_left_in_explorer_var_2 (xaml,application_name, title, name): 
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_LEFT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")


def a_click_right_in_explorer (xaml,application_name, title, name, role): 
    xaml.write("            <ui:Click AlterIfDisabled=\"{x:Null}\" DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SimulateClick=\"{x:Null}\" ClickType=\"CLICK_SINGLE\" ContinueOnError=\"True\" DisplayName=\"Click+" +name+"\" KeyModifiers=\"None\" MouseButton=\"BTN_RIGHT\">")
    xaml.write("              <ui:Click.CursorPosition>")
    xaml.write("                <ui:CursorPosition Position=\"Center\">")
    xaml.write("                  <ui:CursorPosition.OffsetX>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetX>")
    xaml.write("                  <ui:CursorPosition.OffsetY>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:CursorPosition.OffsetY>")
    xaml.write("                </ui:CursorPosition>")
    xaml.write("              </ui:Click.CursorPosition>")
    xaml.write("              <ui:Click.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                  <ui:Target.TimeoutMS>")
    xaml.write("                    <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("                  </ui:Target.TimeoutMS>")
    xaml.write("                  <ui:Target.WaitForReady>")
    xaml.write("                    <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("                  </ui:Target.WaitForReady>")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:Click.Target>")
    xaml.write("            </ui:Click>")


    #wenn keytroke strg + c ist, einfügen


    #über ID
def a_send_hotkey_strg_c_browser (xaml, application_name, url,name, id): 
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+C in: "+name"\"  EmptyField=\"True\" Key=\"c\" KeyModifiers=\"Ctrl\">")
    xaml.write("        <ui:SendHotkey.Target>")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id=\'"+id+"\' tag=\'INPUT\' type=\'text\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("            <ui:Target.TimeoutMS>")
    xaml.write("              <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("            </ui:Target.TimeoutMS>")
    xaml.write("            <ui:Target.WaitForReady>")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("            </ui:Target.WaitForReady>")
    xaml.write("          </ui:Target>")
    xaml.write("        </ui:SendHotkey.Target>")
    xaml.write("      </ui:SendHotkey>")

   #wenn keine ID über name
def a_send_hotkey_strg_c_browser_var2 (xaml, application_name, url, name): 
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+C in: "+name"\"  EmptyField=\"True\" Key=\"c\" KeyModifiers=\"Ctrl\">")
    xaml.write("        <ui:SendHotkey.Target>")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+name+"\' tag=\'INPUT\' type=\'text\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("            <ui:Target.TimeoutMS>")
    xaml.write("              <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("            </ui:Target.TimeoutMS>")
    xaml.write("            <ui:Target.WaitForReady>")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("            </ui:Target.WaitForReady>")
    xaml.write("          </ui:Target>")
    xaml.write("        </ui:SendHotkey.Target>")
    xaml.write("      </ui:SendHotkey>")

#wenn weder ID noch name, über tyg input, type text
def a_send_hotkey_strg_c_browser_var3 (xaml, application_name, url, name): 
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+C in: "+name"\"  EmptyField=\"True\" Key=\"c\" KeyModifiers=\"Ctrl\">")
    xaml.write("        <ui:SendHotkey.Target>")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'INPUT\' type='text' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("            <ui:Target.TimeoutMS>")
    xaml.write("              <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("            </ui:Target.TimeoutMS>")
    xaml.write("            <ui:Target.WaitForReady>")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("            </ui:Target.WaitForReady>")
    xaml.write("          </ui:Target>")
    xaml.write("        </ui:SendHotkey.Target>")
    xaml.write("      </ui:SendHotkey>")

#wenn weder ID noch name, über tag input

def a_send_hotkey_strg_c_browser_var4 (xaml, application_name, url, name): 
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+C in: "+name"\" ContinueOnError=\"True\" EmptyField=\"True\" Key=\"c\" KeyModifiers=\"Ctrl\">")
    xaml.write("        <ui:SendHotkey.Target>")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'INPUT\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("            <ui:Target.TimeoutMS>")
    xaml.write("              <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("            </ui:Target.TimeoutMS>")
    xaml.write("            <ui:Target.WaitForReady>")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("            </ui:Target.WaitForReady>")
    xaml.write("          </ui:Target>")
    xaml.write("        </ui:SendHotkey.Target>")
    xaml.write("      </ui:SendHotkey>")



def a_send_hotkey_strg_v_browser (xaml, application_name, url, name, id):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+V in: "+name"\" ContinueOnError=\"True\" EmptyField=\"True\" Key=\"v\" KeyModifiers=\"Ctrl\">")
    xaml.write("        <ui:SendHotkey.Target>")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag='INPUT' type=\'text\' id=\'"+id+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("            <ui:Target.TimeoutMS>")
    xaml.write("              <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("            </ui:Target.TimeoutMS>")
    xaml.write("            <ui:Target.WaitForReady>")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("            </ui:Target.WaitForReady>")
    xaml.write("          </ui:Target>")
    xaml.write("        </ui:SendHotkey.Target>")
    xaml.write("      </ui:SendHotkey>")


def a_send_hotkey_strg_v_browser_var2 (xaml, application_name, url, name):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+V in: "+name"\" ContinueOnError=\"True\" EmptyField=\"True\" Key=\"v\" KeyModifiers=\"Ctrl\">")
    xaml.write("        <ui:SendHotkey.Target>")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag='INPUT' type=\'text\' aaname=\'"+name+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("            <ui:Target.TimeoutMS>")
    xaml.write("              <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("            </ui:Target.TimeoutMS>")
    xaml.write("            <ui:Target.WaitForReady>")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("            </ui:Target.WaitForReady>")
    xaml.write("          </ui:Target>")
    xaml.write("        </ui:SendHotkey.Target>")
    xaml.write("      </ui:SendHotkey>")

def a_send_hotkey_strg_v_browser_var3 (xaml, application_name, url, name):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+V in: "+name"\" EmptyField=\"True\" Key=\"v\" KeyModifiers=\"Ctrl\">")
    xaml.write("        <ui:SendHotkey.Target>")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag='INPUT' type='text' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("            <ui:Target.TimeoutMS>")
    xaml.write("              <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("            </ui:Target.TimeoutMS>")
    xaml.write("            <ui:Target.WaitForReady>")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("            </ui:Target.WaitForReady>")
    xaml.write("          </ui:Target>")
    xaml.write("        </ui:SendHotkey.Target>")
    xaml.write("      </ui:SendHotkey>")


def a_send_hotkey_strg_v_browser_var4 (xaml, application_name, url, name):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey Strg+V in: "+name"\"  EmptyField=\"True\" Key=\"v\" KeyModifiers=\"Ctrl\">")
    xaml.write("        <ui:SendHotkey.Target>")
    xaml.write("          <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag='INPUT' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("            <ui:Target.TimeoutMS>")
    xaml.write("              <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("            </ui:Target.TimeoutMS>")
    xaml.write("            <ui:Target.WaitForReady>")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("            </ui:Target.WaitForReady>")
    xaml.write("          </ui:Target>")
    xaml.write("        </ui:SendHotkey.Target>")
    xaml.write("      </ui:SendHotkey>")

#Keystroke Logs
#Browser:


def a_sequence_browser_typeinto_start(xaml, name):
    xaml.write("          <Sequence DisplayName=\"Type Into "+name+"\" sap:VirtualizedContainerService.HintSize="418,728" sap2010:WorkflowViewState.IdRef=\"Sequence_3\">")
    xaml.write("              <sap:WorkflowViewStateService.ViewState>")
    xaml.write("                <scg:Dictionary x:TypeArguments="x:String, x:Object">")
    xaml.write("                  <x:Boolean x:Key="IsExpanded">False</x:Boolean>")
    xaml.write("                  <x:Boolean x:Key="IsPinned">False</x:Boolean>")
    xaml.write("                </scg:Dictionary>")
    xaml.write("              </sap:WorkflowViewStateService.ViewState>")


#über automationid 
def a_type_into_browser (xaml,application_name, url, name, id):
    xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into+"+ name+"\" EmptyField=\"True\" Text=\"gewünschten Text eintragen\">")
    xaml.write("              <ui:TypeInto.Target>")
    xaml.write("               <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl id=\'"+id+"\' tag=\'INPUT\' type=\'text\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:TypeInto.Target>")
    xaml.write("            </ui:TypeInto>")

#wenn keine automationID
def a_type_into_browser_var2 (xaml,application_name, url, name): 
    xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into+"+ name+"\" EmptyField=\"True\" Text=\"gewünschten Text eintragen\">")
    xaml.write("              <ui:TypeInto.Target>")
    xaml.write("               <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl aaname=\'"+name+"\' tag=\'INPUT\' type=\'text\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:TypeInto.Target>")
    xaml.write("            </ui:TypeInto>")

#wenn weder automationID noch Name, tag Input, type Text
def a_type_into_browser_var3 (xaml,application_name, url, name): 
    xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into+"+ name+"\" EmptyField=\"True\" Text=\"gewünschten Text eintragen\">")
    xaml.write("              <ui:TypeInto.Target>")
    xaml.write("               <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'INPUT\' type=\'text\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:TypeInto.Target>")
    xaml.write("            </ui:TypeInto>")

#wenn weder automationID noch Name, nur Tag=Input
def a_type_into_browser_var4 (xaml,application_name, url, name): 
    xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into+"+ name+"\" EmptyField=\"True\" Text=\"gewünschten Text eintragen\">")
    xaml.write("              <ui:TypeInto.Target>")
    xaml.write("               <ui:Target Selector=\"&lt;html app=\'"+application_name+".exe\' url=\'"+url+"\' /&gt;&lt;webctrl tag=\'INPUT\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:TypeInto.Target>")
    xaml.write("            </ui:TypeInto>")


#Applikation

def a_type_into_application (xaml,application_name, title, name, automationid):
    xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into+"+ name+"\" EmptyField=\"True\" Text=\"gewünschten Text eintragen\">")
    xaml.write("              <ui:TypeInto.Target>")
    xaml.write("               <ui:Target Selector==\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+automationid+"\' role=\'Element\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:TypeInto.Target>")
    xaml.write("            </ui:TypeInto>")

#Explorer

def a_type_into_explorer (xaml,application_name, title, id, name, role):
    xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into+"+ name+"\" EmptyField=\"True\" Text=\"gewünschten Text eintragen\">")
    xaml.write("              <ui:TypeInto.Target>")
    xaml.write("               <ui:Target Selector==\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+id+"\' name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:TypeInto.Target>")
    xaml.write("            </ui:TypeInto>")

def a_type_into_explorer_var2 (xaml,application_name, title, name, role):
    xaml.write("            <ui:TypeInto DelayBefore=\"{x:Null}\" DelayMS=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Type Into+"+ name+"\" EmptyField=\"True\" Text=\"gewünschten Text eintragen\">")
    xaml.write("              <ui:TypeInto.Target>")
    xaml.write("               <ui:Target Selector==\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia name=\'"+name+"\' role=\'"+role+"\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:TypeInto.Target>")
    xaml.write("            </ui:TypeInto>")

def a_press_enter (xaml): #Enter
    xaml.write("            <ui:SendHotkey Activate=\"True\" DisplayName=\"Enter drücken\" Key=\"enter\" KeyModifiers=\"None\" SpecialKey=\"True\">")
    xaml.write("              <ui:SendHotkey.Target>")
    xaml.write("                <ui:Target  Element=\"{x:Null}\" >")
    xaml.write("                </ui:Target>")
    xaml.write("              </ui:SendHotkey.Target>")
    xaml.write("            </ui:SendHotkey>")


def a_send_hotkey_strg_c_in_application (xaml,application_name, title, name, id):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey STRG+C in "+name+"\" EmptyField=\"True\" Key=\"c\" KeyModifiers=\"Ctrl\">")
    xaml.write("        <ui:SendHotkey.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+id+"\' role=\'Element\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("            <ui:Target.TimeoutMS>")
    xaml.write("              <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("            </ui:Target.TimeoutMS>")
    xaml.write("            <ui:Target.WaitForReady>")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("            </ui:Target.WaitForReady>")
    xaml.write("          </ui:Target>")
    xaml.write("        </ui:SendHotkey.Target>")
    xaml.write("      </ui:SendHotkey>")

def a_send_hotkey_strg_v_in_application (xaml,application_name, title, id):
    xaml.write("      <ui:SendHotkey DelayBefore=\"{x:Null}\" SendWindowMessages=\"{x:Null}\" SpecialKey=\"{x:Null}\" Activate=\"True\" ClickBeforeTyping=\"True\" ContinueOnError=\"True\" DisplayName=\"Send Hotkey STRG+V in "+name+"\" EmptyField=\"True\" Key=\"v\" KeyModifiers=\"Ctrl\">")
    xaml.write("        <ui:SendHotkey.Target>")
    xaml.write("                <ui:Target Selector=\"&lt;wnd app=\'"+application_name+".exe\' title=\'"+title+"\' &lt;uia automationid=\'"+id+"\' role=\'Element\' /&gt;\" TimeoutMS=\"1000\">")
    xaml.write("            <ui:Target.TimeoutMS>")
    xaml.write("              <InArgument x:TypeArguments=\"x:Int32\" />")
    xaml.write("            </ui:Target.TimeoutMS>")
    xaml.write("            <ui:Target.WaitForReady>")
    xaml.write("              <InArgument x:TypeArguments=\"ui:WaitForReady\" />")
    xaml.write("            </ui:Target.WaitForReady>")
    xaml.write("          </ui:Target>")
    xaml.write("        </ui:SendHotkey.Target>")
    xaml.write("      </ui:SendHotkey>")


#Application Activities Excel
def a_open_excel(xaml):
    xaml.write("    <ui:OpenApplication DisplayName=\"Open Application Excel\" FileName=\"C:\Program Files (x86)\Microsoft Office\root\Office16\excel.exe\" Selector=\"&lt;wnd app='excel.exe' /&gt;\">")
    xaml.write("      <ui:OpenApplication.Body>")
    xaml.write("        <ActivityAction x:TypeArguments=\"x:Object\">")
    xaml.write("          <ActivityAction.Argument>")
    xaml.write("            <DelegateInArgument x:TypeArguments=\"x:Object\" Name=\"ContextTarget\" />")
    xaml.write("          </ActivityAction.Argument>")
    xaml.write("          <Sequence DisplayName=\"Do\">")
    xaml.write("          </Sequence>")
    xaml.write("        </ActivityAction>")
    xaml.write("      </ui:OpenApplication.Body>")
    xaml.write("    </ui:OpenApplication>")

def a_excel_application_scope (xaml, workbook_path): #Excel öffnen
    xaml.write("    <ui:ExcelApplicationScope DisplayName=\"Excel Öffnen\" InstanceCachePeriod=\"3000\" WorkbookPath=\""+workbook_path+"\">")
    xaml.write("      <ui:ExcelApplicationScope.Body>")
    xaml.write("        <ActivityAction x:TypeArguments=\"ui:WorkbookApplication\">")
    xaml.write("          <ActivityAction.Argument>")
    xaml.write("            <DelegateInArgument x:TypeArguments=\"ui:WorkbookApplication\" Name=\"ExcelWorkbookScope\" />")
    xaml.write("          </ActivityAction.Argument>")
    xaml.write("          <Sequence DisplayName=\"Do\">")
    xaml.write("          </Sequence>")
    xaml.write("        </ActivityAction>")
    xaml.write("      </ui:ExcelApplicationScope.Body>")
    xaml.write("    </ui:ExcelApplicationScope>")


def a_write_cell(xaml, cell, sheet_name,text, workbook_path ):
    xaml.write("    <ui:WriteCell Cell=\""+cell+"\" DisplayName=\"Write Cell\" SheetName=\""+sheet_name+"\" Text=\""+text+"\" WorkbookPath=\""+workbook_path+"\" />")


#Excel Aktivitäten, müssen im Body der Excel Application Scope sein

def a_read_range(xaml, outputtable_name, range, sheet_name, workbook_path): #Bereich aus Excel Datei auslesen und in Outputtabelle_name speichern
    xaml.write("    <ui:ReadRange AddHeaders=\"True\" DataTable=\""+outputtable_name+"\" DisplayName=\"Read Range\" Range=\""+range+"\" SheetName=\""+sheet_name+"\" WorkbookPath=\""+workbook_path+"\" />")

def a_read_cell (xaml, output_var, cell, sheet_name): #Excel Zelle auslesen
    #Zelle steht in automationId
    xaml.write("    <ui:ExcelReadCell Result=\""+output_var+"\" SheetName=\""+sheet_name+"\" Cell=\""+cell+"\" DisplayName=\"Read Cell\"/>")

def a_for_each_row (xaml, outputtable_name): #For Schleife, für jede Zeile bestimmte Aktivität ausführen
    xaml.write("            <ui:ForEachRow ColumnNames=\"{x:Null}\"  DataTable=\""+[outputtable_name]+"\" DisplayName=\"For Each Row\" >")
    xaml.write("              <ui:ForEachRow.Body>")
    xaml.write("                <ActivityAction x:TypeArguments=\"sd:DataRow\">")
    xaml.write("                  <ActivityAction.Argument>")
    xaml.write("                    <DelegateInArgument x:TypeArguments=\"sd:DataRow\" Name=\"row\" />")
    xaml.write("                  </ActivityAction.Argument>")
    xaml.write("                  <Sequence DisplayName=\"Body\">")
    xaml.write("                  </Sequence>")
    xaml.write("                </ActivityAction>")
    xaml.write("              </ui:ForEachRow.Body>")
    xaml.write("            </ui:ForEachRow>")

def a_excel_auto_save (xaml): #speichert excel automatisch, einfach immer einfügen
    xaml.write("            <ui:ExcelSaveWorkbook DisplayName=\"Save Workbook\"/>")

#Sonstige
def a_find_element (xaml, position_x, position_y): #element finden
    xaml.write("    <ui:FindRelative RelativeElement=\"{x:Null}\" DisplayName=\"Find Element\">")
    xaml.write("      <ui:FindRelative.CursorPosition>")
    xaml.write("        <ui:CursorPosition OffsetX=\""+position_x+"\" OffsetY=\""+position_y+"\" Position=\"TopLeft\"/>")
    xaml.write("      </ui:FindRelative.CursorPosition>")
    xaml.write("      <ui:FindRelative.Target>")
    xaml.write("        <ui:Target ClippingRegion=\"{x:Null}\" Element=\"{x:Null}\" Selector=\"&lt;html app=\'chrome.exe' /&gt;\" WaitForReady=\"COMPLETE\">")
    xaml.write("    </ui:Target>")
    xaml.write("  </ui:FindRelative.Target>")
    xaml.write("    </ui:FindRelative>")

def a_select_item (xaml, item_name): #bei Dropdown Menü, wenn bestimmter Wert ausgewählt werden soll, z.B. Herr/Frau bei Anrede
    xaml.write("    <ui:SelectItem  ContinueOnError=\"True\" Items=\"{x:Null}\" DisplayName=\"Select Item\" Item=\""+item_name+"\">")
    xaml.write("      <ui:SelectItem.Target>")
    xaml.write("        <ui:Target ClippingRegion=\"{x:Null}\" Element=\"{x:Null}\" Selector=\"{x:Null}\"COMPLETE\">")
    xaml.write("        </ui:Target>")
    xaml.write("      </ui:SelectItem.Target>")
    xaml.write("    </ui:SelectItem>")

def a_copy_file (xaml,workbook_path, destination_path): #wenn Datei im explorer von a nach b kopiert wird
    xaml.write("    <ui:CopyFile ContinueOnError=\"True\" Destination=\""+destination_path+"\" DisplayName=\"Copy File\" Path=\""+workbook_path+"\" />")

def a_maximise_window (xaml): #sollte immmer eingebunden werden
    xaml.write("            <ui:MaximizeWindow Window=\"{x:Null}\" DisplayName=\"Maximize Window\"/>")

def a_close_window (xaml): #wird verwendet, wenn User Applikation schließt
    xaml.write("    <ui:CloseWindow Selector=\"{x:Null}\" UseWindow=\"{x:Null}\" DisplayName=\"Close Window\" WaitForReady=\"COMPLETE\" />")

def a_end_activity (xaml):
    xaml.write("  </Sequence>\n</Activity>")

def a_try_catch_try_start (xaml):
    xaml.write("    <TryCatch DisplayName=\"Try Catch\" sap:VirtualizedContainerService.HintSize=\"434,318.666666666667\" sap2010:WorkflowViewState.IdRef=\"TryCatch\">")
    xaml.write("      <TryCatch.Try>")

def a_try_catch_try_end (xaml):
    xaml.write("      </TryCatch.Try>")

def a_try_catch_all_catches_start (xaml):
    xaml.write("      <TryCatch.Catches>")

def a_try_catch_all_catches_end (xaml):
    xaml.write("      </TryCatch.Catches>")

def a_try_catch_catch_start (xaml):
    xaml.write("        <Catch x:TypeArguments=\"s:Exception\" sap:VirtualizedContainerService.HintSize=\"400,22\" sap2010:WorkflowViewState.IdRef=\"Catch1\">")
    xaml.write("          <sap:WorkflowViewStateService.ViewState>")
    xaml.write("            <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">")
    xaml.write("              <x:Boolean x:Key=\"IsExpanded\">False</x:Boolean>")
    xaml.write("              <x:Boolean x:Key=\"IsPinned\">False</x:Boolean>")
    xaml.write("            </scg:Dictionary>")
    xaml.write("          </sap:WorkflowViewStateService.ViewState>")
    xaml.write("          <ActivityAction x:TypeArguments=\"s:Exception\">")
    xaml.write("            <ActivityAction.Argument>")
    xaml.write("              <DelegateInArgument x:TypeArguments=\"s:Exception\" Name=\"exception\" />")
    xaml.write("            </ActivityAction.Argument>")

def a_try_catch_catch_end (xaml):
    xaml.write("        </Catch>")




