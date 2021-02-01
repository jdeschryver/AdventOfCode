Imports System.IO
Imports System.Text.RegularExpressions

Friend Module Module8

    Dim filePath = "C:\Users\desch\Documents\Repositories\AdventOfCode\python\AOC20\input\day8-ex1.txt"

    Sub Main()
        Dim BootCode()() = Lees8()
        Dim Frequenties(BootCode.Length \ 2 - 1) As Integer
        Dim intAcc = Controleoponeindigelus(BootCode, Frequenties)

        Console.WriteLine(intAcc)
        Console.ReadLine()
    End Sub

    Private Function Lees8() As String()()
        Dim lines = File.ReadLines(FilePath)
        Dim hlpBootcode(lines.Count)()

        Dim lineNr = 0
        For Each line In lines
            hlpBootcode(lineNr) = Regex.Split(line, "\s")
            lineNr += 1
        Next

        Return hlpBootcode
    End Function

    Private Function Controleoponeindigelus(pBootcode As String()(), pFrequenties As Integer()) As Integer
        Dim i = 0
        Do Until pFrequenties(i) = 2
            Select Case pBootcode(i)(0)
                Case "nop"
                    i += 1
                Case "acc"
                    Controleoponeindigelus += pBootcode(i)(1)
                    i += 1
                Case "jmp"
                    i += CInt(pBootcode(i)(1))

            End Select
            pFrequenties(i) += 1
        Loop
        Return Controleoponeindigelus
    End Function
End Module
