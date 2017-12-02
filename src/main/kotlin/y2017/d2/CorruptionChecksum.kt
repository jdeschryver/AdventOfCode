import y2015.calculatePaper
import java.io.File
import java.lang.Integer.MAX_VALUE
import java.lang.Integer.MIN_VALUE

/**
 * @author Jan De Schryver <Jan.DeSchryver@bucephalus.be>
 */


fun minMaxLine(line: String) =
    line.split(" ", "\t")
            .map(String::toInt)
            .fold( MAX_VALUE to MIN_VALUE){ acc, i ->  minOf(acc.first, i) to maxOf(acc.second, i)}
            .difference()

fun Pair<Int, Int>.difference() = this.second - this.first

fun divisibleLine(line: String): Int{
    val ints = line.split(" ", "\t").map(String::toInt)

    return ints.map { i -> ints.map { j -> i to j } }
            .flatten()
            .first { it.divisible() }.divide()
}

fun Pair<Int, Int>.divisible() =
        this.second != this.first && (this.second % this.first == 0 || this.first % this.second == 0)

fun Pair<Int, Int>.divide() = maxOf(this.first, this.second) / minOf(this.first, this.second)

fun main(args: Array<String>) {
    val input = File( "src\\main\\kotlin\\y2017\\d2\\input.txt")
            .inputStream()
            .use { it.bufferedReader().readLines() }

    println(input.sumBy { minMaxLine(it) })
    println(input.sumBy { divisibleLine(it) })
}