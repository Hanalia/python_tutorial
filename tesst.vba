Sub VisualizeFactoryData()
    Dim ws As Worksheet
    Dim chartObj As ChartObject
    Dim rng As Range

    ' Set the worksheet
    Set ws = ThisWorkbook.Sheets("FactoryData")

    ' Define the range of data to be visualized
    Set rng = ws.Range("A1:B10") ' Adjust the range as needed

    ' Add a new chart
    Set chartObj = ws.ChartObjects.Add(Left:=100, Width:=375, Top:=50, Height:=225)
    With chartObj.Chart
        .SetSourceData Source:=rng
        .ChartType = xlColumnClustered ' Change the chart type as needed
        .HasTitle = True
        .ChartTitle.Text = "Factory Data Visualization"
        .Axes(xlCategory, xlPrimary).HasTitle = True
        .Axes(xlCategory, xlPrimary).AxisTitle.Text = "Category"
        .Axes(xlValue, xlPrimary).HasTitle = True
        .Axes(xlValue, xlPrimary).AxisTitle.Text = "Values"
    End With
End Sub