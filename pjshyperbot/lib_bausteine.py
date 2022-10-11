#import xaml as xaml
# coding=utf-8

def activity(xaml):   #write header of UIPath XAML file
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
    return ("</Activity>")

def sequence(xaml): #write sequence header of UiPath XAML file
    xaml.write("  <Sequence sap2010:WorkflowViewState.IdRef=\"Sequence_Start\">\n    <sap:WorkflowViewStateService.ViewState>\n")
    xaml.write("      <scg:Dictionary x:TypeArguments=\"x:String, x:Object\">\n        <x:Boolean x:Key=\"IsExpanded\">True</x:Boolean>\n      </scg:Dictionary>\n    </sap:WorkflowViewStateService.ViewState>\n")
    return("  </Sequence>\n")

def s_varaibles(xaml):
    xaml.write("	  <Sequence.Variables>\n")
    return("	  </Sequence.Variables>\n")    

def variable(xaml, vname, vtype, vinit):
    xaml.write("		<Variable x:TypeArguments=\"x:" + vtype + "\" Name=\"" + vname + "\">\n")
    xaml.write("		  <Variable.Default>\n			<Literal x:TypeArguments=\"x:" + vtype + "\">" + vinit + "</Literal>\n		  </Variable.Default>\n")
    xaml.write("		</Variable>")

def a_comment(xaml,id,txt): #kommentar
    xaml.write("    <ui:Comment sap2010:WorkflowViewState.IdRef=\"Comment_" + id + "\" Text=\"" + txt + "\" />\n")

def a_comment_calendar_picker (xaml):
    xaml.write("            <ui:Comment Text=\"Kalender Picker: Pruefen, ob Datum manuell eingegeben werden kann. Dann ganz normal mit Type Into. Ansonsten bitte Klickaktivit?t manuell einbauen mit dynamischem Selektor, der entsprechend das gew?nschte Datum ausw?hlen kann. &#xD;&#xA;&#xD;&#xA;Wichtig: Es kann sein, dass der Monat mit dem gew?nschten Datum nicht direkt angezeigt wird, wenn der Kalender ge?ffnet ist. &#xD;&#xA;&#xD;&#xA;Dann so vorgehen:&#xD;&#xA;&#xD;&#xA;Try Catch Aktivit?t einbauen, innerhalb einer while Schleife:&#xD;&#xA;&#xD;&#xA;while Schleife: Bedingung&#xD;&#xA;&#xD;&#xA;im Try: &#xD;&#xA;Klickaktivit?t mit gew?nschtem Datum, versucht Feld zu finden&#xD;&#xA;dann: while schleifen Bedingung auf True setzen&#xD;&#xA;&#xD;&#xA;im except: Klickaktivit?t auf &quot;Weiter&quot;, bis gew?nschter Monat angezeigt wird&#xD;&#xA;&#xD;&#xA;While Schleife: L?uft solange bis Try Aktivit?t erfolgreich durchgef?hrt wurde\" />")

#def a_comment_optionsfeld (xaml):
    #xaml.write("            <ui:Comment Text=\"Optionsfeld: Hier k?nnte evtl. auch eine Select Item Aktivit?t sinnvoll sein\" />")

#Open Browser Aktivit?ten

#def a_attach_browser(xaml, url): #auf bereits ge?ffnetes Fenster zur?ckspringen, wenn User bspw. von Browser zu Excel und dann wieder zum browser wechselt
    #xaml.write("    <ui:BrowserScope BrowserType=\"Edge\" ContinueOnError=\"True\" DisplayName=\"Attach Browser\" sap:VirtualizedContainerService.HintSize=\"434,230.666666666667\" sap2010:WorkflowViewState.IdRef=\"BrowserScope_1\"  Selector=\"&lt;html app=\'msedge.exe\' url=\'"+url+"\'/&gt;\" TimeoutMS=\"1000\">\n")
    #xaml.write("      <ui:BrowserScope.Body>\n")
    #xaml.write("        <ActivityAction x:TypeArguments=\"x:Object\">\n")
    #xaml.write("          <ActivityAction.Argument>\n")
    #xaml.write("            <DelegateInArgument x:TypeArguments=\"x:Object\" Name=\"ContextTarget\" />\n")
    #xaml.write("          </ActivityAction.Argument>\n")
    #xaml.write("          <Sequence DisplayName=\"Do\">\n")
    #xaml.write("          </Sequence>\n")
    #xaml.write("        </ActivityAction>\n")
    #xaml.write("      </ui:BrowserScope.Body>\n")
    #xaml.write("    </ui:BrowserScope>\n")

def a_navigate_to (xaml, url): #muss im selben browser sein
    xaml.write("            <ui:NavigateTo Browser=\"{x:Null}\" DisplayName=\"Navigate To\" Url=\""+url+"\" />\n")