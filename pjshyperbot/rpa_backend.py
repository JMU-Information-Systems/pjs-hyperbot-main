# Test 
# Generate UIPath XAML from Logger DB
import sys
import sqlite3

def writehead(xaml):   #write header of UIPath XAML file
    xaml.write("<Activity mc:Ignorable=\"sap sap2010\" x:Class=\"Main\" mva:VisualBasic.Settings=\"{x:Null}\" sap:VirtualizedContainerService.HintSize=\"968,2533\" sap2010:WorkflowViewState.IdRef=\"ActivityBuilder_1\" ")
    xaml.write("xmlns=\"http://schemas.microsoft.com/netfx/2009/xaml/activities\" xmlns:mc=\"http://schemas.openxmlformats.org/markup-compatibility/2006\" ")
    xaml.write("xmlns:mva=\"clr-namespace:Microsoft.VisualBasic.Activities;assembly=System.Activities\" xmlns:sap=\"http://schemas.microsoft.com/netfx/2009/xaml/activities/presentation\" ")
    xaml.write("xmlns:ui=\"http://schemas.uipath.com/workflow/activities\" ")
    xaml.write("xmlns:sap2010=\"http://schemas.microsoft.com/netfx/2010/xaml/activities/presentation\" xmlns:scg=\"clr-namespace:System.Collections.Generic;assembly=mscorlib\" ")
    xaml.write("xmlns:sco=\"clr-namespace:System.Collections.ObjectModel;assembly=mscorlib\" xmlns:uix=\"http://schemas.uipath.com/workflow/activities/uix\" xmlns:x=\"http://schemas.microsoft.com/winfx/2006/xaml\">\n")
    xaml.write("  <TextExpression.NamespacesForImplementation>\n    <sco:Collection x:TypeArguments=\"x:String\">\n      <x:String>System.Activities</x:String>\n")
    xaml.write("      <x:String>System.Activities.Statements</x:String>\n      <x:String>System.Activities.Expressions</x:String>\n      <x:String>System.Activities.Validation</x:String>\n      <x:String>System.Activities.XamlIntegration</x:String>\n")
    xaml.write("      <x:String>Microsoft.VisualBasic</x:String>\n      <x:String>Microsoft.VisualBasic.Activities</x:String>\n      <x:String>System</x:String>\n      <x:String>System.Collections</x:String>\n")
    xaml.write("      <x:String>System.Collections.Generic</x:String>\n      <x:String>System.Data</x:String>\n      <x:String>System.Diagnostics</x:String>\n      <x:String>System.Drawing</x:String>\n")
    xaml.write("      <x:String>System.IO</x:String>\n      <x:String>System.Linq</x:String>\n      <x:String>System.Net.Mail</x:String>\n      <x:String>System.Xml</x:String>\n      <x:String>System.Xml.Linq</x:String>\n")
    xaml.write("      <x:String>UiPath.Core</x:String>\n      <x:String>UiPath.Core.Activities</x:String>\n      <x:String>System.Windows.Markup</x:String>\n      <x:String>System.Runtime.Serialization</x:String>\n")
    xaml.write("      <x:String>UiPath.Orchestrator.Client.Models</x:String>\n      <x:String>UiPath.Core.Activities.Orchestrator</x:String>\n      <x:String>System.Collections.ObjectModel</x:String>\n")
    xaml.write("      <x:String>System.Activities.DynamicUpdate</x:String>\n      <x:String>UiPath.UIAutomationNext.Enums</x:String>\n      <x:String>UiPath.UIAutomationCore.Contracts</x:String>\n")
    xaml.write("      <x:String>UiPath.UIAutomationNext.Activities</x:String>\n      <x:String>UiPath.Platform.ObjectLibrary</x:String>\n      <x:String>UiPath.Shared.Activities</x:String>\n")
    xaml.write("      <x:String>UiPath.UIAutomationNext.Contracts</x:String>\n      <x:String>System.Security</x:String>\n      <x:String>System.ComponentModel</x:String>\n")
    xaml.write("    </sco:Collection>\n  </TextExpression.NamespacesForImplementation>\n")
    xaml.write("  <TextExpression.ReferencesForImplementation>\n    <sco:Collection x:TypeArguments=\"AssemblyReference\">\n      <AssemblyReference>System.Activities</AssemblyReference>\n")
    xaml.write("      <AssemblyReference>Microsoft.VisualBasic</AssemblyReference>\n      <AssemblyReference>mscorlib</AssemblyReference>\n      <AssemblyReference>System.Data</AssemblyReference>\n")
    xaml.write("      <AssemblyReference>System</AssemblyReference>\n      <AssemblyReference>System.Drawing</AssemblyReference>\n      <AssemblyReference>System.Core</AssemblyReference>\n")
    xaml.write("      <AssemblyReference>System.Xml</AssemblyReference>\n      <AssemblyReference>System.Xml.Linq</AssemblyReference>\n      <AssemblyReference>PresentationFramework</AssemblyReference>\n")
    xaml.write("      <AssemblyReference>WindowsBase</AssemblyReference>\n      <AssemblyReference>PresentationCore</AssemblyReference>\n      <AssemblyReference>System.Xaml</AssemblyReference>\n")
    xaml.write("      <AssemblyReference>UiPath.System.Activities</AssemblyReference>\n      <AssemblyReference>UiPath.UiAutomation.Activities</AssemblyReference>\n      <AssemblyReference>System.Data.DataSetExtensions</AssemblyReference>\n")
    xaml.write("      <AssemblyReference>System.Runtime.Serialization</AssemblyReference>\n      <AssemblyReference>UiPath.OrchestratorClient</AssemblyReference>\n      <AssemblyReference>UiPath.UIAutomationNext</AssemblyReference>\n")
    xaml.write("      <AssemblyReference>UiPath.UIAutomationCore</AssemblyReference>\n      <AssemblyReference>UiPath.UIAutomationNext.Activities</AssemblyReference>\n      <AssemblyReference>UiPath.Platform</AssemblyReference>\n")
    xaml.write("      <AssemblyReference>UiPath.Excel.Activities</AssemblyReference>\n      <AssemblyReference>UiPath.Mail.Activities</AssemblyReference>\n      <AssemblyReference>UiPath.OCR.Activities</AssemblyReference>\n")
    xaml.write("      <AssemblyReference>System.ServiceModel</AssemblyReference>\n      <AssemblyReference>Microsoft.Bcl.AsyncInterfaces</AssemblyReference>\n      <AssemblyReference>System.ValueTuple</AssemblyReference>\n")
    xaml.write("      <AssemblyReference>System.ComponentModel.Composition</AssemblyReference>\n      <AssemblyReference>System.Memory</AssemblyReference>\n      <AssemblyReference>NPOI</AssemblyReference>\n")
    xaml.write("      <AssemblyReference>System.Runtime.WindowsRuntime</AssemblyReference>\n    </sco:Collection>\n  </TextExpression.ReferencesForImplementation>\n")
    xaml.write("  <Sequence sap2010:WorkflowViewState.IdRef=\"Sequence_16\">\n    <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("      <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n        <x:Boolean x:Key=\"IsExpanded\">True</x:Boolean>\n      </scg:Dictionary>\n    </sap:WorkflowViewStateService.ViewState>\n")

def writefoot(xaml):   # write footer of UIPath XAML file
    xaml.write("  </Sequence>\n</Activity>")

def a_comment(xaml,id,txt):
    xaml.write("    <ui:Comment sap2010:WorkflowViewState.IdRef=\"Comment_" + id + "\" Text=\"" + txt + "\" />\n")

def a_chrome(xaml,url,id):
    xaml.write("    <uix:NApplicationCard WebDriverMode=\"{x:Null}\" AttachMode=\"ByInstance\" DisplayName=\"Chrome\" sap2010:WorkflowViewState.IdRef=\"NApplicationCard_" + id + "\"")
    xaml.write(" IsIncognito=\"True\" OpenMode=\"IfNotOpen\"  WindowResize=\"Maximize\">\n")
    xaml.write("      <uix:NApplicationCard.Body>\n        <ActivityAction x:TypeArguments=\"x:Object\">\n          <ActivityAction.Argument>\n")
    xaml.write("            <DelegateInArgument x:TypeArguments=\"x:Object\" Name=\"WSSessionData\" />\n          </ActivityAction.Argument>\n")
    xaml.write("        </ActivityAction>\n      </uix:NApplicationCard.Body>\n      <uix:NApplicationCard.TargetApp>\n")
    xaml.write("        <uix:TargetApp BrowserType=\"Chrome\" Selector=\"&lt;html app='chrome.exe' title='blabla' /&gt;\" Url=\"" + url + "\" />\n")
    xaml.write("      </uix:NApplicationCard.TargetApp>\n    </uix:NApplicationCard>\n")

def main(dbname):    # argument is the name of the database as produced by the recorder plus additional table for input/output links
    filename =  dbname[0:dbname.find(".")] + ".xaml"   # filename for XAML file like db with extension .xaml
    xaml = open(filename,"w", encoding="utf-8")
    writehead(xaml)
    try:
        con = sqlite3.connect(dbname)
        cur = con.cursor()
        cur.execute("SELECT * FROM ApplicationMonitorLogs;")  # read main table of recorder
        row = cur.fetchone()
        while row:                                            # process actions as recorded 
           rowstr = ','.join(str(v) for v in row)
           if row[2] == "chrome" and row[0] == 3:
              a_chrome(xaml,"https://www.bahn.de",str(row[0]))        
           else:
              a_comment(xaml,str(row[0]),rowstr)       

           #xaml.write(rowstr + '\n')
           row = cur.fetchone()
        writefoot(xaml)
        xaml.close()
    except sqlite3.Error as error:
        print("DB-Error ", error)
    finally:
        if con:
            con.close()
if __name__ == '__main__':
    main(sys.argv[1])
