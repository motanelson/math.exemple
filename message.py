var1="Display.ShowMessageDialog.ShowMessage"

values=[ "Title:", "Message:","Icon:","Buttons:","DefaultButton:","IsTopMost:"]
valuesv=[ "","","Display.Icon.None","Display.Buttons.OK","Display.DefaultButton.Button1","False"]
c="ButtonPressed=> ButtonPressed"

print("\033c\033[40;37m\n give me title string? ")
a=input()
print("\033[40;37m\n give me value string ? ")
b=input()
var2=var1+" "+values[0]+" $'''"+a+"''' "+values[1]+" $'''"+b+"''' "+values[2]+" "+valuesv[2]+" "+values[3]+" "+valuesv[3]+" "+values[4]+" "+valuesv[4]+" "+values[5]+" "+valuesv[5]+" "+c
print("\n"+"-"*80 +"\n")
print(var2)