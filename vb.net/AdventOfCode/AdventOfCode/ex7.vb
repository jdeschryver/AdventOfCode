Imports System.IO
Imports System.Text.RegularExpressions

Module ex7
    Dim FilePath As String = "C:\Users\desch\Documents\Repositories\AdventOfCode\python\AOC20\input\day7-ex1.txt"

    Structure BagContentElement
        Public bagName As String
        Public numberOfBags As Integer
    End Structure

    Sub Main()
        Dim bags = ReadBags()
        Dim numberOfInnerBags = CountAllInnerBags("shiny gold", bags)
        Console.WriteLine(numberOfInnerBags)
        Console.Read()
    End Sub

    Function CountAllInnerBags(bagColor As String, bags As Dictionary(Of String, List(Of BagContentElement))) As Integer
        Dim numberOfInnerBags = 0
        Dim innerBags As List(Of BagContentElement)

        If Not bags.ContainsKey(bagColor) Then
            Return 0
        End If

        bags.TryGetValue(bagColor, innerBags)
        For Each innerBag In innerBags
            numberOfInnerBags += innerBag.numberOfBags
            numberOfInnerBags += innerBag.numberOfBags * CountAllInnerBags(innerBag.bagName, bags)
        Next

        Return numberOfInnerBags
    End Function

    Function ReadBags() As Dictionary(Of String, List(Of BagContentElement))
        Dim bagToContent As New Dictionary(Of String, List(Of BagContentElement))
        For Each line As String In File.ReadLines(FilePath)
            Dim outerAndInnerBags() = Regex.Split(line, "contain")
            Dim rawOurBag = outerAndInnerBags(0)
            Dim rawInnerBag = outerAndInnerBags(1)

            Dim outerBag = Regex.Replace(rawOurBag, "bag(s)?[\s.]?", "").Trim
            Dim innerBags = ParseInnerBags(rawInnerBag)
            bagToContent.Add(outerBag, innerBags)
        Next
        Return bagToContent
    End Function

    Function ParseInnerBags(rawInnerBags As String) As List(Of BagContentElement)
        If rawInnerBags = " no other bags." Then
            Return New List(Of BagContentElement)
        End If

        Dim innerBags As String = Regex.Replace(rawInnerBags, "bag(s)?[\s.]?", "").Trim
        Dim innerBagsList = New List(Of BagContentElement)
        For Each innerBag As String In Regex.Split(innerBags, ",\s")
            Dim bagInfoDetails As String() = New Regex("\s").Split(innerBag, 2, 0)
            Dim bagInfo As BagContentElement = New BagContentElement()
            bagInfo.bagName = bagInfoDetails(1).Trim
            bagInfo.numberOfBags = bagInfoDetails(0)
            innerBagsList.Add(bagInfo)
        Next
        Return innerBagsList
    End Function

End Module
