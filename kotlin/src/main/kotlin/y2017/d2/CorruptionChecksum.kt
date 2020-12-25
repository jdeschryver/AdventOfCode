import java.io.File

/**
 * @author Jan De Schryver <Jan.DeSchryver@bucephalus.be>
 */


fun minMaxLine(line: List<Int>) = (line.max() ?: 0) - (line.min() ?: 0)

fun divisibleLine(line: List<Int>) = line.asSequence().flatMap { i ->
               line.asSequence().filter {i > it && i % it == 0 }.map { i / it }
    }.first()



fun main(args: Array<String>) {
    val input = File( "src\\main\\kotlin\\y2017\\d2\\input.txt")
            .inputStream()
            .use { it.bufferedReader().readLines() }

    println(input.sumBy { minMaxLine(it.split(" ", "\t").map(String::toInt)) })
    println(input.sumBy { divisibleLine(it.split(" ", "\t").map(String::toInt)) })
}